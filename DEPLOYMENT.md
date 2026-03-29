# Deployment Guide: Vercel + Railway

This guide walks through deploying your Library Application to production using **Vercel** (frontend) and **Railway** (backend).

## Prerequisites

- GitHub account (with your project pushed)
- Vercel account (free at https://vercel.com)
- Railway account (free at https://railway.app)

---

## Part 1: Deploy Backend to Railway

### Step 1: Create Railway Account & Project

1. Go to https://railway.app and sign up
2. Click "Create Project"
3. Select "Deploy from GitHub"
4. Authorize Railway to access your GitHub account
5. Select your `library-app` repository
6. Click "Deploy"

### Step 2: Configure Railway Environment Variables

Once deployed, Railway will automatically detect your Python app:

1. In Railway dashboard, go to your project
2. Click on the "Variables" tab
3. Add these environment variables:

| Variable | Value |
|----------|-------|
| `ALLOWED_ORIGINS` | `https://your-frontend.vercel.app` (you'll get this URL after Vercel deployment) |
| `DATABASE_URL` | Railway provides this automatically, leave as-is |
| `SECRET_KEY` | Generate a random secure key |
| `PYTHON_VERSION` | `3.11` |

4. Click "Deploy" to apply changes

### Step 3: Get Your Railway API URL

1. In Railway, go to "Settings" → "Networking"
2. Your public URL will be something like: `https://libraryapp-production.up.railway.app`
3. **Save this URL** - you'll need it for Vercel

---

## Part 2: Deploy Frontend to Vercel

### Step 1: Connect to Vercel

1. Go to https://vercel.com and sign up with GitHub
2. Click "Import Project"
3. Select your GitHub repository
4. Vercel will auto-detect it's a React app

### Step 2: Configure Environment Variables

Before deploying, add environment variables:

1. In the "Environment Variables" section, add:

| Variable | Value |
|----------|-------|
| `REACT_APP_API_URL` | Your Railway URL from Part 1, Step 3 |

Example: `https://libraryapp-production.up.railway.app`

2. Click "Deploy"

### Step 3: Verify Deployment

1. Once deployment completes, Vercel gives you a public URL
2. Click the URL to visit your live app
3. Test creating/reading books to verify API connection

---

## Part 3: Update CORS Settings

Go back to Railway and update `ALLOWED_ORIGINS`:

1. Railway dashboard → Variables
2. Update `ALLOWED_ORIGINS` to your Vercel domain (e.g., `https://yourapp.vercel.app`)
3. Deploy/restart

---

## Troubleshooting

### Frontend shows "Cannot reach API"
- Check that `REACT_APP_API_URL` in Vercel matches your Railway URL
- Verify Railway backend is deployed and running
- Check Railway logs for backend errors

### Backend shows CORS error
- Ensure `ALLOWED_ORIGINS` in Railway includes your Vercel domain
- Format should be: `https://yourapp.vercel.app` (no trailing slash)

### Database errors on Railway
- Railway auto-provisions PostgreSQL, check "Variables" tab
- Verify `DATABASE_URL` is set correctly

### 502 Bad Gateway on Railway
- Check Railway logs: Project → Deployments → View Logs
- Ensure `Procfile` is in backend directory

---

## Future Deployments

After initial setup, deployments happen automatically:

- **Push to GitHub** (`main` branch)
- **Vercel** auto-deploys your changes
- **Railway** auto-deploys backend changes

No manual redeployment needed!

---

## Custom Domain (Optional)

Both Vercel and Railway support custom domains:
- Vercel: Settings → Domains → Add Domain
- Railway: Settings → Networking → Custom Domain

---

## Monitoring & Logs

- **Vercel**: Deployments tab shows build logs
- **Railway**: Deployments → View Logs for runtime errors

---

Questions? Check the docs:
- https://vercel.com/docs
- https://docs.railway.app
