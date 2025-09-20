# Santhos Kamal - Portfolio Setup Guide

## 🚀 Quick Start

### Prerequisites
- Node.js (v16 or higher)
- Python (v3.8 or higher)
- MongoDB (local or cloud)

### Frontend Setup
```bash
cd frontend
npm install
# or
yarn install

# Start development server
npm start
# or
yarn start
```
The frontend will run on `http://localhost:3000`

### Backend Setup
```bash
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Start the server
uvicorn server:app --reload --host 0.0.0.0 --port 8001
```
The backend will run on `http://localhost:8001`

## 📧 Email Configuration

### Gmail Setup (Current Configuration)
1. Your Gmail is already configured: `santykamal2001@gmail.com`
2. App password is set in `.env` file
3. Emails are sent to: `santykamal2001@gmail.com`

### To Change Email Settings
Edit `backend/.env`:
```env
EMAIL_USER="your-email@gmail.com"
EMAIL_PASS="your-app-password"
EMAIL_TO="where-to-receive-emails@gmail.com"
```

## 📝 Content Editing

### Easy Content Updates
All your portfolio content is in: `frontend/src/data/mock.js`

#### Update Your Bio
```javascript
about: {
  description: "Your new bio text here..."
}
```

#### Add New Projects
```javascript
projects: [
  {
    title: "New Project Name",
    description: "Project description...",
    technologies: ["React", "Node.js", "MongoDB"],
    github: "https://github.com/yourusername/project",
    demo: "https://your-demo-url.com",
    icon: "💻",
    highlights: [
      "Key achievement 1",
      "Key achievement 2"
    ]
  }
]
```

#### Add Experience/Education
```javascript
timeline: [
  {
    type: "experience", // or "education"
    title: "Job Title",
    organization: "Company Name",
    period: "Jan 2024 - Present",
    description: "Job description...",
    achievements: [
      "Achievement 1",
      "Achievement 2"
    ]
  }
]
```

## 🌐 Deployment Options

### 1. Vercel (Frontend) + Railway (Backend)
- **Frontend**: Deploy to Vercel
- **Backend**: Deploy to Railway
- **Database**: MongoDB Atlas

### 2. Netlify + Heroku
- **Frontend**: Deploy to Netlify
- **Backend**: Deploy to Heroku
- **Database**: MongoDB Atlas

### 3. Full Stack Platforms
- **Render**: Full-stack deployment
- **DigitalOcean App Platform**: Complete solution

## 🔧 Environment Variables

### Frontend (.env)
```env
REACT_APP_BACKEND_URL=http://localhost:8001
# or your deployed backend URL
```

### Backend (.env)
```env
MONGO_URL="mongodb://localhost:27017"
DB_NAME="portfolio_database"
EMAIL_USER="your-email@gmail.com"
EMAIL_PASS="your-app-password"
EMAIL_TO="where-emails-go@gmail.com"
```

## 📱 Features

### ✅ Working Features
- Responsive design (mobile, tablet, desktop)
- Dark/Light mode toggle
- Smooth animations
- Working contact form with email
- Project showcase with GitHub links
- Experience timeline
- Certifications display
- SEO optimized

### 🎨 Customization
- Colors: Edit `frontend/tailwind.config.js`
- Fonts: Edit `frontend/src/index.css`
- Layout: Edit component files in `frontend/src/components/`

## 🐛 Troubleshooting

### Email Not Working
1. Check Gmail app password is correct
2. Verify 2-step verification is enabled
3. Ensure EMAIL_PASS has no spaces

### Frontend Not Loading
1. Check if backend is running on port 8001
2. Verify REACT_APP_BACKEND_URL in frontend/.env
3. Check browser console for errors

### Database Issues
1. Make sure MongoDB is running
2. Check MONGO_URL in backend/.env
3. Verify database permissions

## 📞 Support
- Email: santykamal2001@gmail.com
- LinkedIn: https://linkedin.com/in/santhos-kamal
- GitHub: https://github.com/santykamal2001

## 🎯 Live Version
Your portfolio is currently live at:
https://modern-devfolio-5.preview.emergentagent.com