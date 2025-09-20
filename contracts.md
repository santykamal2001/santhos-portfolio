# Portfolio Backend API Contracts

## Contact Form Email Integration

### Current Frontend Implementation
- **File**: `/app/frontend/src/components/Portfolio.jsx`
- **Component**: `ContactSection` 
- **Current Behavior**: Mock form submission with toast notification
- **Form Fields**: name, email, subject, message

### Backend API to Implement

#### POST /api/contact
**Purpose**: Send contact form email to portfolio owner

**Request Body**:
```json
{
  "name": "string (required, 2-50 chars)",
  "email": "string (required, valid email format)",
  "subject": "string (required, 5-100 chars)", 
  "message": "string (required, 10-1000 chars)"
}
```

**Response Success (200)**:
```json
{
  "success": true,
  "message": "Email sent successfully"
}
```

**Response Error (400)**:
```json
{
  "success": false,
  "error": "Validation error message"
}
```

**Response Error (500)**:
```json
{
  "success": false,
  "error": "Failed to send email"
}
```

### Email Configuration Needed
- **SMTP Service**: Gmail SMTP (recommended) or custom SMTP
- **Environment Variables**:
  - `EMAIL_USER`: sender email address
  - `EMAIL_PASS`: app-specific password or SMTP password
  - `EMAIL_TO`: recipient email (santykamal2001@gmail.com)

### Frontend Integration Changes
1. **Remove mock behavior** from `handleSubmit` function
2. **Add API call** to `POST /api/contact` endpoint
3. **Handle loading states** during email sending
4. **Show success/error messages** based on API response
5. **Keep form validation** on frontend
6. **Reset form** only on successful submission

### Email Template
- **Subject**: `Portfolio Contact: ${subject}`
- **Body**: Include all form fields formatted nicely
- **From**: Use provided email in "Reply-To" header
- **HTML formatting** for professional appearance

### Backend Dependencies to Add
- `nodemailer` for email sending
- `joi` or `zod` for request validation
- Express rate limiting for contact form

### Security Considerations
- Rate limiting (max 5 emails per IP per hour)
- Input sanitization and validation
- CORS already configured
- No sensitive data exposure in responses