# 🔧 Environment Variables Reference

## 🚀 **Railway Backend Environment Variables**

Add these in Railway dashboard under "Variables" tab:

```
MONGO_URL=mongodb+srv://username:password@cluster.mongodb.net/portfolio_db
DB_NAME=portfolio_db
EMAIL_USER=your-email@gmail.com
EMAIL_PASS=your-gmail-app-password
EMAIL_TO=your-email@gmail.com
CORS_ORIGINS=*
```

## 🌐 **Vercel Frontend Environment Variables**

Add these in Vercel dashboard under "Environment Variables":

```
REACT_APP_BACKEND_URL=https://your-backend-name.railway.app
```

## 📧 **Gmail App Password Setup**

1. Go to Google Account → Security
2. Enable 2-Factor Authentication
3. Go to App passwords
4. Generate password for "Mail"
5. Use this password in EMAIL_PASS

## 📝 **Example Values**

**MongoDB Connection String Example:**
```
mongodb+srv://santhos:mypassword123@cluster0.abc123.mongodb.net/portfolio_db
```

**Railway Backend URL Example:**
```
https://santhos-portfolio-backend-production.railway.app
```

**Vercel Frontend URL Example:**
```
https://santhos-portfolio.vercel.app
```