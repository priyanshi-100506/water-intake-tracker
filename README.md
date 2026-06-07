"""
README: AI Hydration Intelligence Platform

A production-grade hydration tracking application with AI-powered insights,
built with FastAPI, Streamlit, SQLite, LangChain, and Ollama (Llama 3.2).
"""

# AI Hydration Intelligence Platform 💧

Advanced hydration tracking with personalized AI coaching powered by Llama 3.2

## 🎯 Features

### User Management
- ✅ User profiles with age, weight, and activity level
- ✅ Customizable daily hydration goals
- ✅ Profile updates and management

### Hydration Tracking
- ✅ Log water intake with timestamps
- ✅ View intake history (daily, weekly, monthly)
- ✅ Daily total calculations
- ✅ Intake records with automatic timestamps

### AI-Powered Analytics
- ✅ Hydration score (0-100)
- ✅ Goal completion percentage
- ✅ Current streak tracking
- ✅ Longest streak (all-time)
- ✅ Weekly and monthly averages
- ✅ Trend analysis
- ✅ AI-powered recommendations

### Weekly Reports
- ✅ Comprehensive weekly analysis
- ✅ Key insights and trends
- ✅ Personalized recommendations
- ✅ Goal achievement metrics

### Dashboard
- ✅ Modern, responsive Streamlit UI
- ✅ Real-time analytics display
- ✅ Interactive charts and trends
- ✅ Profile management interface
- ✅ Weekly report generation

## 🏗️ Architecture

```
water-intake-tracker/
├── src/
│   ├── __init__.py
│   ├── database.py         # Database operations with CRUD
│   ├── agent.py            # AI agent with LangChain
│   ├── api.py              # FastAPI endpoints
│   ├── analytics.py        # Analytics engine
│   ├── config.py           # Configuration settings
│   ├── utils.py            # Utility functions
│   └── logger.py           # Logging setup
├── dashboard.py            # Streamlit dashboard
├── requirements.txt        # Python dependencies
├── water_tracker.db        # SQLite database
└── README.md              # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Ollama with Llama 3.2 model installed locally
- SQLite3

### Installation

1. **Clone/Setup Project**
```bash
cd water-intake-tracker
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Initialize Database**
```bash
python src/database.py
```

4. **Start Ollama Server** (in another terminal)
```bash
ollama serve
```

5. **Run API Server** (in another terminal)
```bash
python -m uvicorn src.api:app --host 127.0.0.1 --port 8000 --reload
```

6. **Run Dashboard** (in another terminal)
```bash
streamlit run dashboard.py
```

Visit: `http://localhost:8501`

## 📚 API Endpoints

### User Management
- `POST /profile` - Create user profile
- `GET /profile/{user_id}` - Get user profile
- `PUT /profile/{user_id}` - Update profile
- `DELETE /user/{user_id}` - Delete user

### Hydration Goals
- `POST /goal` - Set daily hydration goal
- `GET /goal/{user_id}` - Get current goal

### Intake Logging
- `POST /log-intake` - Log water intake
- `GET /history/{user_id}` - Get intake history

### Analytics
- `GET /analytics/{user_id}` - Get analytics metrics
- `GET /weekly-report/{user_id}` - Get weekly report

### Health
- `GET /` - Health check
- `GET /docs` - API documentation

## 🤖 AI Features

### Real-time Analysis
When logging water intake, receive:
- Immediate hydration assessment
- Personalized recommendations
- Hydration tips

### Weekly Reports
AI-generated reports include:
- Overall performance assessment
- Key insights and trends
- Personalized recommendations
- Motivation and celebration messages

### Personalized Recommendations
Based on user profile:
- Age and weight
- Activity level
- Hydration history
- Goal achievement
- Current streak

## 📊 Database Schema

### user_profile
```sql
user_id (TEXT PRIMARY KEY)
age (INTEGER)
weight_kg (REAL)
activity_level (TEXT)
created_at (TIMESTAMP)
updated_at (TIMESTAMP)
```

### hydration_goal
```sql
user_id (TEXT PRIMARY KEY)
daily_goal_ml (INTEGER)
created_at (TIMESTAMP)
updated_at (TIMESTAMP)
```

### water_intake
```sql
id (INTEGER PRIMARY KEY)
user_id (TEXT)
intake_ml (INTEGER)
date (TEXT)
timestamp (TIMESTAMP)
```

## 🎨 Dashboard Features

### Metrics Cards
- Hydration Score (0-100)
- Daily Progress (%)
- Current Streak
- Best Streak
- Weekly Average
- Monthly Average

### Progress Bar
Visual representation of daily goal progress

### Charts
- Line chart of intake trends
- Daily totals table

### AI Coach Section
- Immediate analysis feedback
- Weekly report generation
- Trend analysis

### Profile Management
- Create new profiles
- Update profile information
- View profile details

## ⚙️ Configuration

### Environment Variables
```bash
DATABASE_NAME=water_tracker.db
OLLAMA_MODEL=llama3.2
OLLAMA_TEMPERATURE=0.3
API_HOST=127.0.0.1
API_PORT=8000
LOG_LEVEL=INFO
```

### Activity Levels
- `sedentary` - Little or no exercise
- `light` - Exercise 1-3 days/week
- `moderate` - Exercise 3-5 days/week
- `heavy` - Exercise 6-7 days/week

## 🔍 Analytics Metrics

### Hydration Score
Calculated from:
- Daily goal achievement (40%)
- Weekly consistency (40%)
- Streak bonus (20%)

Score Range: 0-100

### Goal Completion
Percentage of daily goal achieved today

### Streaks
- Current: Consecutive days meeting goal
- Longest: All-time best streak

### Averages
- Weekly: Average daily intake last 7 days
- Monthly: Average daily intake current month

## 🛠️ Development

### Project Structure
- **Database**: `src/database.py` - CRUD operations
- **Agent**: `src/agent.py` - AI analysis and recommendations
- **API**: `src/api.py` - REST endpoints
- **Analytics**: `src/analytics.py` - Metrics calculation
- **Dashboard**: `dashboard.py` - Streamlit UI
- **Config**: `src/config.py` - Settings
- **Utils**: `src/utils.py` - Helper functions

### Type Hints
All functions include proper type hints for better IDE support and error detection

### Error Handling
- Comprehensive try/except blocks
- Proper HTTP status codes
- User-friendly error messages

### Logging
Structured logging throughout the application for debugging and monitoring

## 📈 Future Enhancements

### Planned Features
- [ ] PostgreSQL support (current: SQLite)
- [ ] User authentication
- [ ] Social features (friend leaderboards)
- [ ] Mobile app integration
- [ ] Advanced trend analysis
- [ ] Export reports (PDF, CSV)
- [ ] Multi-language support
- [ ] Dark/light theme toggle

### Scalability
- Database layer abstraction allows easy migration to PostgreSQL
- API designed for microservices architecture
- Separate business logic from API routes
- AI logic isolated for easy model swapping

## 🐛 Troubleshooting

### Ollama Connection Issues
- Ensure Ollama is running: `ollama serve`
- Verify model is pulled: `ollama pull llama3.2`
- Check API is using correct host/port

### Database Errors
- Verify database file exists and is readable
- Check disk space for new records
- Reset database: delete `water_tracker.db` and reinit

### Streamlit Issues
- Clear cache: `streamlit cache clear`
- Restart server: `Ctrl+C` then rerun
- Check port 8501 availability

## 📝 License

This project is provided as-is for portfolio and educational purposes.

## 🙋 Support

For issues or questions:
1. Check troubleshooting section
2. Review API documentation
3. Check application logs

---

**Built with ❤️ for hydration health**

Powered by FastAPI, SQLite, LangChain, Ollama, and Llama 3.2
