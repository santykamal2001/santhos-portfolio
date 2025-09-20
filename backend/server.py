from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, validator
from typing import List, Optional
import uuid
from datetime import datetime
import re
from email_service import email_service


ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Create the main app without a prefix
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")


# Define Models
class StatusCheck(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    client_name: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class StatusCheckCreate(BaseModel):
    client_name: str

class ContactForm(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: str = Field(..., min_length=5, max_length=100)
    subject: str = Field(..., min_length=5, max_length=100)
    message: str = Field(..., min_length=10, max_length=1000)
    
    @validator('email')
    def validate_email(cls, v):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, v):
            raise ValueError('Invalid email format')
        return v
    
    @validator('name', 'subject', 'message')
    def validate_text_fields(cls, v):
        if not v.strip():
            raise ValueError('Field cannot be empty or contain only whitespace')
        return v.strip()

class ContactResponse(BaseModel):
    success: bool
    message: str

# Add your routes to the router instead of directly to app
@api_router.get("/")
async def root():
    return {"message": "Hello World"}

@api_router.post("/status", response_model=StatusCheck)
async def create_status_check(input: StatusCheckCreate):
    status_dict = input.dict()
    status_obj = StatusCheck(**status_dict)
    _ = await db.status_checks.insert_one(status_obj.dict())
    return status_obj

@api_router.get("/status", response_model=List[StatusCheck])
async def get_status_checks():
    status_checks = await db.status_checks.find().to_list(1000)
    return [StatusCheck(**status_check) for status_check in status_checks]

@api_router.post("/contact", response_model=ContactResponse)
async def send_contact_email(contact_data: ContactForm):
    """Send contact form email"""
    try:
        # Convert to dict for email service
        contact_dict = {
            "name": contact_data.name,
            "email": contact_data.email,
            "subject": contact_data.subject,
            "message": contact_data.message
        }
        
        # Attempt to send email
        email_sent = await email_service.send_contact_email(contact_dict)
        
        if email_sent:
            # Store contact form submission in database
            contact_record = {
                "id": str(uuid.uuid4()),
                "name": contact_data.name,
                "email": contact_data.email,
                "subject": contact_data.subject,
                "message": contact_data.message,
                "timestamp": datetime.utcnow(),
                "email_sent": True
            }
            await db.contact_submissions.insert_one(contact_record)
            
            return ContactResponse(
                success=True,
                message="Thank you for your message! I'll get back to you soon."
            )
        else:
            logger.warning("Email service failed, but storing contact submission")
            # Still store the submission even if email fails
            contact_record = {
                "id": str(uuid.uuid4()),
                "name": contact_data.name,
                "email": contact_data.email,
                "subject": contact_data.subject,
                "message": contact_data.message,
                "timestamp": datetime.utcnow(),
                "email_sent": False
            }
            await db.contact_submissions.insert_one(contact_record)
            
            return ContactResponse(
                success=True,
                message="Message received! I'll get back to you soon."
            )
            
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Contact form error: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to process contact form")

# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
