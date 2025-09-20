import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Dict
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

logger = logging.getLogger(__name__)

class EmailService:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.email_user = os.environ.get('EMAIL_USER', 'santykamal2001@gmail.com')
        self.email_pass = os.environ.get('EMAIL_PASS', '')
        self.email_to = os.environ.get('EMAIL_TO', 'santykamal2001@gmail.com')
        
        # Debug logging
        logger.info(f"Email configuration loaded:")
        logger.info(f"EMAIL_USER: {self.email_user}")
        logger.info(f"EMAIL_PASS configured: {'Yes' if self.email_pass else 'No'}")
        logger.info(f"EMAIL_TO: {self.email_to}")
    
    def create_email_content(self, contact_data: Dict[str, str]) -> str:
        """Create HTML email content from contact form data"""
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 8px 8px 0 0; }}
                .content {{ background: #f9f9f9; padding: 20px; border-radius: 0 0 8px 8px; }}
                .field {{ margin-bottom: 15px; }}
                .label {{ font-weight: bold; color: #555; }}
                .value {{ background: white; padding: 10px; border-radius: 4px; margin-top: 5px; }}
                .message {{ background: white; padding: 15px; border-radius: 4px; margin-top: 5px; white-space: pre-wrap; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h2>New Contact Form Submission</h2>
                    <p>You have received a new message through your portfolio website.</p>
                </div>
                <div class="content">
                    <div class="field">
                        <div class="label">Name:</div>
                        <div class="value">{contact_data['name']}</div>
                    </div>
                    <div class="field">
                        <div class="label">Email:</div>
                        <div class="value">{contact_data['email']}</div>
                    </div>
                    <div class="field">
                        <div class="label">Subject:</div>
                        <div class="value">{contact_data['subject']}</div>
                    </div>
                    <div class="field">
                        <div class="label">Message:</div>
                        <div class="message">{contact_data['message']}</div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
        return html_content

    async def send_contact_email(self, contact_data: Dict[str, str]) -> bool:
        """Send contact form email"""
        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = f"Portfolio Contact: {contact_data['subject']}"
            msg['From'] = self.email_user
            msg['To'] = self.email_to
            msg['Reply-To'] = contact_data['email']

            # Create HTML content
            html_content = self.create_email_content(contact_data)
            html_part = MIMEText(html_content, 'html')
            
            # Create plain text version
            text_content = f"""
New Contact Form Submission

Name: {contact_data['name']}
Email: {contact_data['email']}
Subject: {contact_data['subject']}

Message:
{contact_data['message']}
            """
            text_part = MIMEText(text_content, 'plain')
            
            msg.attach(text_part)
            msg.attach(html_part)

            # Send email
            if not self.email_pass:
                logger.warning("Email password not configured. Email sending disabled.")
                return False
                
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.email_user, self.email_pass)
                server.send_message(msg)
            
            logger.info(f"Contact email sent successfully from {contact_data['email']}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send contact email: {str(e)}")
            return False

# Global email service instance
email_service = EmailService()