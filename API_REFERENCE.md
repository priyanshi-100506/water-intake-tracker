"""
API_REFERENCE.md - Complete API Documentation

Full reference for all endpoints with examples
"""

# 📚 API Reference

## Base URL
```
http://127.0.0.1:8000
```

## Authentication
No authentication required (local development)

---

## Health & Documentation

### Health Check
```
GET /
```

**Response** (200):
```json
{
  "status": "healthy",
  "service": "AI Hydration Intelligence Platform",
  "version": "1.0.0"
}
```

### API Documentation
```
GET /docs
```
Interactive Swagger UI with all endpoints

### API Reference
```
GET /api/docs
```
Alternative documentation endpoint

---

## User Management

### Create User Profile
```
POST /profile
```

**Request Body**:
```json
{
  "user_id": "user1",
  "age": 28,
  "weight_kg": 75.0,
  "activity_level": "moderate",
  "daily_goal_ml": 2500
}
```

**Response** (200):
```json
{
  "user_id": "user1",
  "age": 28,
  "weight_kg": 75.0,
  "activity_level": "moderate",
  "daily_goal_ml": 2500,
  "created_at": "2024-01-15T10:30:00"
}
```

**Errors**:
- 409: User already exists
- 400: Invalid data

---

### Get User Profile
```
GET /profile/{user_id}
```

**Parameters**:
- `user_id` (string, path): Unique user identifier

**Response** (200):
```json
{
  "user_id": "user1",
  "age": 28,
  "weight_kg": 75.0,
  "activity_level": "moderate",
  "daily_goal_ml": 2500,
  "created_at": "2024-01-15T10:30:00"
}
```

**Errors**:
- 404: User not found

---

### Update User Profile
```
PUT /profile/{user_id}
```

**Parameters**:
- `user_id` (string, path): Unique user identifier

**Request Body**:
```json
{
  "user_id": "user1",
  "age": 29,
  "weight_kg": 76.0,
  "activity_level": "heavy",
  "daily_goal_ml": 3000
}
```

**Response** (200):
```json
{
  "user_id": "user1",
  "age": 29,
  "weight_kg": 76.0,
  "activity_level": "heavy",
  "daily_goal_ml": 3000,
  "created_at": "2024-01-15T10:30:00"
}
```

**Errors**:
- 404: User not found
- 400: Invalid data

---

### Delete User
```
DELETE /user/{user_id}
```

**Parameters**:
- `user_id` (string, path): Unique user identifier

**Response** (200):
```json
{
  "message": "User user1 deleted successfully"
}
```

**Errors**:
- 404: User not found

---

## Hydration Goals

### Set/Update Hydration Goal
```
POST /goal
```

**Request Body**:
```json
{
  "user_id": "user1",
  "daily_goal_ml": 3000
}
```

**Response** (200):
```json
{
  "message": "Goal updated successfully",
  "user_id": "user1",
  "daily_goal_ml": 3000
}
```

**Errors**:
- 404: User not found
- 400: Invalid goal value

---

## Water Intake

### Log Water Intake
```
POST /log-intake
```

**Request Body**:
```json
{
  "user_id": "user1",
  "intake_ml": 500
}
```

**Response** (200):
```json
{
  "message": "Water intake logged successfully",
  "intake_ml": 500,
  "analysis": "Great hydration session! You're maintaining healthy drinking habits. Keep it up!"
}
```

**Errors**:
- 404: User not found
- 400: Invalid intake value (must be 0-10000)

---

### Get Intake History
```
GET /history/{user_id}
```

**Parameters**:
- `user_id` (string, path): Unique user identifier
- `days` (integer, query, optional): Number of past days to retrieve (default: all)

**Example**:
```
GET /history/user1?days=7
```

**Response** (200):
```json
{
  "user_id": "user1",
  "total_records": 3,
  "history": [
    {
      "id": 1,
      "intake_ml": 500,
      "date": "2024-01-15",
      "timestamp": "2024-01-15T10:30:00"
    },
    {
      "id": 2,
      "intake_ml": 300,
      "date": "2024-01-15",
      "timestamp": "2024-01-15T14:30:00"
    },
    {
      "id": 3,
      "intake_ml": 250,
      "date": "2024-01-15",
      "timestamp": "2024-01-15T18:00:00"
    }
  ]
}
```

**Errors**:
- 404: User not found

---

## Analytics

### Get Analytics
```
GET /analytics/{user_id}
```

**Parameters**:
- `user_id` (string, path): Unique user identifier

**Response** (200):
```json
{
  "user_id": "user1",
  "hydration_score": 78.5,
  "goal_completion_percent": 92.0,
  "current_streak": 5,
  "longest_streak": 12,
  "weekly_average": 2400.0,
  "monthly_average": 2350.0
}
```

**Metrics Explained**:
- `hydration_score`: Overall score (0-100)
- `goal_completion_percent`: Today's progress toward goal
- `current_streak`: Days meeting goal consecutively
- `longest_streak`: All-time best streak
- `weekly_average`: Average daily intake (last 7 days)
- `monthly_average`: Average daily intake (current month)

**Errors**:
- 404: User not found

---

### Get Weekly Report
```
GET /weekly-report/{user_id}
```

**Parameters**:
- `user_id` (string, path): Unique user identifier

**Response** (200):
```json
{
  "user_id": "user1",
  "total_intake": 16800,
  "average_daily": 2400.0,
  "goal_achievement": 96.0,
  "days_met_goal": 6,
  "overall_assessment": "Excellent work! You've been consistently meeting your hydration goals.",
  "key_insights": [
    "You maintained an average of 2400 mL daily",
    "You met your goal 6 out of 7 days",
    "Your hydration habits are excellent"
  ],
  "trends": "Your intake is stable with slight improvement",
  "recommendations": [
    "Keep maintaining this excellent hydration routine",
    "Remember to hydrate even on busy days",
    "Stay consistent with your daily habit"
  ]
}
```

**Errors**:
- 404: User not found

---

## Activity Levels

Valid values for `activity_level`:
- `sedentary` - Little or no exercise
- `light` - Exercise 1-3 days per week  
- `moderate` - Exercise 3-5 days per week
- `heavy` - Exercise 6-7 days per week

---

## Error Responses

All error responses follow this format:

```json
{
  "detail": "Error message describing what went wrong"
}
```

### Common HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK - Request succeeded |
| 400 | Bad Request - Invalid input data |
| 404 | Not Found - Resource doesn't exist |
| 409 | Conflict - Resource already exists |
| 500 | Server Error - Internal error |

---

## Data Models

### UserProfile
```json
{
  "user_id": "string",
  "age": "integer (1-150)",
  "weight_kg": "float (20-300)",
  "activity_level": "string (sedentary|light|moderate|heavy)",
  "daily_goal_ml": "integer (1000-10000)",
  "created_at": "ISO 8601 timestamp"
}
```

### WaterIntakeRecord
```json
{
  "id": "integer",
  "user_id": "string",
  "intake_ml": "integer (0-10000)",
  "date": "YYYY-MM-DD",
  "timestamp": "ISO 8601 timestamp"
}
```

### Analytics
```json
{
  "user_id": "string",
  "hydration_score": "float (0-100)",
  "goal_completion_percent": "float (0-200+)",
  "current_streak": "integer",
  "longest_streak": "integer",
  "weekly_average": "float",
  "monthly_average": "float"
}
```

---

## Usage Examples

### Python with Requests
```python
import requests

BASE_URL = "http://127.0.0.1:8000"

# Create user
response = requests.post(
    f"{BASE_URL}/profile",
    json={
        "user_id": "john_doe",
        "age": 30,
        "weight_kg": 80,
        "activity_level": "moderate",
        "daily_goal_ml": 2500
    }
)
print(response.json())

# Log intake
response = requests.post(
    f"{BASE_URL}/log-intake",
    json={"user_id": "john_doe", "intake_ml": 500}
)
print(response.json())

# Get analytics
response = requests.get(f"{BASE_URL}/analytics/john_doe")
print(response.json())
```

### cURL
```bash
# Create user
curl -X POST "http://127.0.0.1:8000/profile" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "john_doe",
    "age": 30,
    "weight_kg": 80,
    "activity_level": "moderate",
    "daily_goal_ml": 2500
  }'

# Log intake
curl -X POST "http://127.0.0.1:8000/log-intake" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "john_doe",
    "intake_ml": 500
  }'

# Get analytics
curl -X GET "http://127.0.0.1:8000/analytics/john_doe"
```

### JavaScript/Fetch
```javascript
const BASE_URL = "http://127.0.0.1:8000";

// Create user
fetch(`${BASE_URL}/profile`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    user_id: "john_doe",
    age: 30,
    weight_kg: 80,
    activity_level: "moderate",
    daily_goal_ml: 2500
  })
})
.then(r => r.json())
.then(data => console.log(data));

// Log intake
fetch(`${BASE_URL}/log-intake`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    user_id: "john_doe",
    intake_ml: 500
  })
})
.then(r => r.json())
.then(data => console.log(data));
```

---

## Rate Limiting
No rate limiting in development mode

## Validation Rules

| Field | Rules |
|-------|-------|
| user_id | 1-50 characters, alphanumeric |
| age | 1-150 years |
| weight_kg | 20-300 kg |
| activity_level | One of: sedentary, light, moderate, heavy |
| daily_goal_ml | 1000-10000 mL |
| intake_ml | 0-10000 mL |

---

## Pagination
Not applicable (future enhancement)

---

## Versioning
Current API version: **1.0.0**

---

**Last Updated**: 2024-01-15

For questions or issues, refer to README.md or SETUP_GUIDE.md
