"""
SETUP_GUIDE.md - Complete Setup Instructions

Step-by-step guide to run the AI Hydration Intelligence Platform
"""

# 🚀 Complete Setup Guide

## Prerequisites

Before starting, ensure you have:
- **Python 3.9 or higher** installed
- **Ollama** installed and running locally
- **Llama 3.2 model** downloaded in Ollama

## Step 1: Verify Ollama Setup

### Install Ollama
Visit: https://ollama.ai

### Download Llama 3.2
```bash
ollama pull llama3.2
```

### Verify Installation
```bash
ollama list
```
You should see:
```
NAME            ID              SIZE    MODIFIED
llama3.2:latest ...             ...     ...
```

### Start Ollama Server
```bash
ollama serve
```
This will run on `http://127.0.0.1:11434` by default

## Step 2: Clone/Setup Project

```bash
# Navigate to project directory
cd "path/to/water intake tracker"

# Verify structure
ls -la
```

## Step 3: Create Virtual Environment (Optional but Recommended)

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

## Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- FastAPI - Web framework
- Uvicorn - ASGI server
- Pydantic - Data validation
- LangChain - LLM framework
- Streamlit - Dashboard framework
- Ollama integration
- And more...

## Step 5: Initialize Database

```bash
python src/database.py
```

You should see:
```
Database tables initialized successfully
```

This creates:
- `user_profile` table
- `hydration_goal` table
- `water_intake` table
- Necessary indexes

## Step 6: Configure Environment (Optional)

### Create `.env` file
```bash
cp .env.example .env
```

### Edit `.env` if needed
```
DATABASE_NAME=water_tracker.db
OLLAMA_MODEL=llama3.2
OLLAMA_TEMPERATURE=0.3
API_HOST=127.0.0.1
API_PORT=8000
LOG_LEVEL=INFO
```

## Step 7: Start Services

### Terminal 1: Start Ollama
```bash
ollama serve
```
⏳ Keep this running. You'll see:
```
Listening on 127.0.0.1:11434
```

### Terminal 2: Start FastAPI Server
```bash
python -m uvicorn src.api:app --host 127.0.0.1 --port 8000 --reload
```
✅ You should see:
```
Uvicorn running on http://127.0.0.1:8000
```

### Terminal 3: Start Streamlit Dashboard
```bash
streamlit run dashboard.py
```
✅ You should see:
```
You can now view your Streamlit app in your browser.
Local URL: http://localhost:8501
```

## Step 8: Access the Application

### Dashboard
Open your browser to: **http://localhost:8501**

You'll see the Streamlit dashboard with:
- User management controls
- Water intake logging
- Analytics dashboard
- Weekly reports
- AI coach section

### API Documentation
Visit: **http://127.0.0.1:8000/docs**

Interactive API documentation with:
- All endpoints
- Request/response models
- Try it out functionality

## First Use

### Create a User Profile

1. Click **"New User"** button in sidebar
2. Fill in details:
   - User ID: `user1` (or your name)
   - Age: Your age
   - Weight: Your weight in kg
   - Activity Level: Select your activity level
   - Daily Goal: Recommended or custom (mL)
3. Click **"Create Profile"**

### Log Water Intake

1. Select User ID (should auto-populate)
2. Enter amount in mL (e.g., 250, 500)
3. Click **"Log & Analyze"**
4. View:
   - Immediate AI analysis
   - Intake logged confirmation
   - Dashboard updates

### View Analytics

- **Hydration Score**: 0-100 based on goals and streaks
- **Progress**: Today's percentage of daily goal
- **Streaks**: Current and all-time best
- **Averages**: Weekly and monthly intake
- **Trends**: Line chart of daily intake

### Generate Weekly Report

1. Click **"Get Weekly Report"** button
2. View:
   - Weekly summary
   - Key insights from AI
   - Trend analysis
   - Personalized recommendations

## Verification Checklist

- [ ] Ollama running (`ollama serve`)
- [ ] Ollama model downloaded (`ollama list`)
- [ ] FastAPI running (`http://127.0.0.1:8000`)
- [ ] Streamlit running (`http://localhost:8501`)
- [ ] Dashboard loads without errors
- [ ] Can create user profile
- [ ] Can log water intake
- [ ] Can view analytics
- [ ] AI analysis appears after logging

## Troubleshooting

### API Won't Start
**Error**: `Connection refused at 127.0.0.1:11434`

**Solution**:
```bash
# Ensure Ollama is running in another terminal
ollama serve
```

### Database Error
**Error**: `database.db is locked`

**Solution**:
```bash
# Close all Python processes
# Delete database
rm water_tracker.db
# Reinitialize
python src/database.py
```

### Ollama Model Not Found
**Error**: `error creating model`

**Solution**:
```bash
# Pull the model again
ollama pull llama3.2
```

### Port Already in Use

For port 8000:
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux
lsof -i :8000
kill -9 <PID>
```

For port 8501:
```bash
streamlit run dashboard.py --server.port 8502
```

### Slow Responses
- Ollama model loading is normal first time (~30s)
- Subsequent requests are faster
- Check system RAM availability

## Development Tips

### Hot Reload
FastAPI automatically reloads on code changes with `--reload` flag

### Streamlit Caching
Use `@st.cache_data` for API calls to improve performance

### Database Queries
All database operations use context managers for proper connection handling

### Logging
Check application logs for debugging:
```bash
# In API terminal
# Logs appear in console
```

## Next Steps

1. **Create Multiple Users**: Test with different profiles
2. **Log Multiple Days**: Generate trends and analytics
3. **Generate Reports**: Test weekly report generation
4. **Customize**: Update daily goals, profiles
5. **Explore API**: Use `/docs` endpoint for API testing

## Performance Notes

### First Time Setup
- Model loading: 30-60 seconds
- Database initialization: < 1 second

### Typical Operations
- Logging intake: 2-5 seconds (includes AI analysis)
- Loading analytics: < 1 second
- Weekly report: 5-10 seconds (includes AI analysis)

### System Requirements
- RAM: 4GB minimum (8GB recommended)
- Storage: 500MB minimum (for model + data)
- Network: Not required (all local)

## File Structure After Setup

```
water-intake-tracker/
├── venv/                    # Virtual environment (if created)
├── src/
│   ├── __init__.py
│   ├── database.py
│   ├── agent.py
│   ├── api.py
│   ├── analytics.py
│   ├── config.py
│   ├── utils.py
│   └── logger.py
├── dashboard.py
├── dashboard_new.py         # New improved version
├── requirements.txt
├── water_tracker.db         # Created after init
├── app.log                  # Application logs
├── .env                     # Created from .env.example
├── .env.example
├── README.md
└── SETUP_GUIDE.md          # This file
```

## Support & Resources

### Official Docs
- FastAPI: https://fastapi.tiangolo.com
- Streamlit: https://docs.streamlit.io
- LangChain: https://python.langchain.com
- Ollama: https://github.com/ollama/ollama

### Common Issues
See Troubleshooting section above

---

**Ready to track your hydration! 💧**

Start the services and visit http://localhost:8501
