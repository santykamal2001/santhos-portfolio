# Portfolio Deployment Guide

Your portfolio app is now ready for deployment! Here are several deployment options:

## 🚀 Quick Local Setup

Your app is already running locally:
- **Frontend**: http://localhost:3000
- **Backend**: http://127.0.0.1:8000
- **API Docs**: http://127.0.0.1:8000/docs

## 📦 Deployment Options

### 1. **Vercel (Recommended for Frontend)**
Perfect for React apps with automatic deployments from GitHub.

**Steps:**
1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Import your GitHub repository
4. Configure build settings:
   - Build Command: `cd frontend && yarn build`
   - Output Directory: `frontend/build`
   - Install Command: `cd frontend && yarn install`
5. Add environment variables:
   - `REACT_APP_BACKEND_URL=https://your-backend-url.com`

### 2. **Railway (Great for Full-Stack)**
Deploys both frontend and backend with databases.

**Steps:**
1. Push to GitHub
2. Go to [railway.app](https://railway.app)
3. Deploy from GitHub
4. Add MongoDB service
5. Configure environment variables

### 3. **Heroku (Traditional Option)**
Good for backend APIs and full-stack apps.

**Backend Deployment:**
```bash
# Install Heroku CLI
# Login and create app
heroku create your-portfolio-backend
heroku addons:create mongolab:sandbox
git subtree push --prefix backend heroku main
```

**Frontend Deployment:**
Deploy to Heroku or use Vercel for better performance.

### 4. **Netlify (Frontend Only)**
Excellent for static sites and React apps.

**Steps:**
1. Push to GitHub
2. Go to [netlify.com](https://netlify.com)
3. Import GitHub repository
4. Build settings:
   - Base directory: `frontend`
   - Build command: `yarn build`
   - Publish directory: `frontend/build`

### 5. **Docker Deployment**
Use the provided Docker configuration for any cloud provider.

```bash
# Build and run with Docker Compose
docker-compose up --build

# Or build individual services
docker build -t portfolio-frontend ./frontend
docker build -t portfolio-backend ./backend
```

### 6. **AWS/GCP/Azure**
For enterprise-grade deployment:

- **Frontend**: S3 + CloudFront (AWS) or Azure Static Web Apps
- **Backend**: ECS/Lambda (AWS), Cloud Run (GCP), or Container Instances (Azure)
- **Database**: MongoDB Atlas or cloud-native databases

## 🔧 Environment Configuration

### Frontend (.env)
```
REACT_APP_BACKEND_URL=https://your-backend-url.com
```

### Backend (.env)
```
MONGO_URL=mongodb://your-mongo-connection-string
DB_NAME=portfolio_db
EMAIL_USER=your-email@gmail.com
EMAIL_PASS=your-app-password
EMAIL_TO=your-email@gmail.com
CORS_ORIGINS=https://your-frontend-url.com
```

## 🛡️ Security Notes

1. **Never commit real credentials** - use environment variables
2. **Update CORS_ORIGINS** to your actual domain
3. **Use HTTPS** in production
4. **Set up proper email authentication** (Gmail App Passwords)

## 📧 Email Setup

For the contact form to work:
1. Enable 2-factor authentication on Gmail
2. Generate an App Password
3. Use the App Password in `EMAIL_PASS`

## 🔄 CI/CD Setup

Create `.github/workflows/deploy.yml` for automatic deployments:

```yaml
name: Deploy
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v2
      - run: cd frontend && npm install && npm run build
      # Add deployment steps
```

## 📊 Monitoring

- Set up error tracking with Sentry
- Use analytics with Google Analytics
- Monitor uptime with UptimeRobot

## 🎯 Recommended Stack

**For Beginners:**
- Frontend: Vercel
- Backend: Railway or Render
- Database: MongoDB Atlas

**For Advanced Users:**
- Frontend: Vercel or Netlify
- Backend: AWS Lambda or Google Cloud Run
- Database: MongoDB Atlas or PostgreSQL

Your portfolio is production-ready! Choose the deployment option that best fits your needs and budget.