"""
Streamlit Dashboard for AI Hydration Intelligence Platform.

Professional, responsive dashboard with user profiles, analytics,
AI coaching, and progress tracking.
"""

import requests
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from datetime import datetime, timedelta

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Hydration Coach",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
    }
    
    body {
        background-color: #0f172a;
        color: #e2e8f0;
    }
    
    .main {
        padding: 2rem 1rem;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #334155;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: bold;
        color: #06b6d4;
        margin: 0.5rem 0;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .score-excellent {
        color: #10b981;
    }
    
    .score-good {
        color: #3b82f6;
    }
    
    .score-fair {
        color: #f59e0b;
    }
    
    .score-poor {
        color: #ef4444;
    }
    
    .section-header {
        font-size: 1.8rem;
        font-weight: bold;
        color: #e2e8f0;
        margin: 2rem 0 1rem 0;
        border-bottom: 2px solid #06b6d4;
        padding-bottom: 0.5rem;
    }
    
    .insight-box {
        background: #1e293b;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #06b6d4;
        margin: 1rem 0;
    }
    
    .insight-text {
        color: #cbd5e1;
        font-size: 0.95rem;
        line-height: 1.5;
    }
    
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);
        color: white;
        border: none;
        padding: 0.75rem;
        border-radius: 8px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #0891b2 0%, #06b6d4 100%);
        box-shadow: 0 4px 12px rgba(6, 182, 212, 0.4);
    }
    
    .success-box {
        background: #064e3b;
        border: 1px solid #10b981;
        color: #86efac;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .warning-box {
        background: #78350f;
        border: 1px solid #f59e0b;
        color: #fcd34d;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data(ttl=300)
def get_profile_data(user_id):
    """Fetch user profile from API."""
    try:
        response = requests.get(f"{API_URL}/profile/{user_id}")
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

@st.cache_data(ttl=60)
def get_analytics_data(user_id):
    """Fetch analytics from API."""
    try:
        response = requests.get(f"{API_URL}/analytics/{user_id}")
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

@st.cache_data(ttl=60)
def get_history_data(user_id, days=7):
    """Fetch intake history from API."""
    try:
        response = requests.get(f"{API_URL}/history/{user_id}", params={"days": days})
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

def get_score_color(score):
    """Determine color based on hydration score."""
    if score >= 80:
        return "score-excellent"
    elif score >= 60:
        return "score-good"
    elif score >= 40:
        return "score-fair"
    else:
        return "score-poor"

st.title("💧 AI Hydration Coach")
st.markdown("Track your hydration with AI-powered insights powered by Llama 3.2")

with st.sidebar:
    st.header("⚙️ Control Panel")
    
    st.subheader("User Management")
    user_id = st.text_input(
        "User ID",
        value="user1",
        help="Your unique identifier"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Load Profile"):
            st.session_state["load_profile"] = True
    
    with col2:
        if st.button("New User"):
            st.session_state["show_create_user"] = True
    
    st.divider()
    
    st.subheader("📊 Log Water Intake")
    
    intake_ml = st.number_input(
        "Amount (mL)",
        min_value=0,
        max_value=10000,
        value=250,
        step=50
    )
    
    if st.button("Log & Analyze", use_container_width=True):
        st.session_state["log_intake"] = True
        st.session_state["intake_value"] = intake_ml

if st.session_state.get("show_create_user"):
    st.warning("Creating a new user profile...")
    
    with st.form("create_user_form"):
        new_user_id = st.text_input("User ID", value="user1")
        age = st.number_input("Age (years)", min_value=1, max_value=150, value=25)
        weight = st.number_input("Weight (kg)", min_value=20.0, max_value=300.0, value=75.0)
        
        activity_level = st.selectbox(
            "Activity Level",
            ["sedentary", "light", "moderate", "heavy"]
        )
        
        daily_goal = st.number_input(
            "Daily Goal (mL)",
            min_value=1000,
            max_value=10000,
            value=2500,
            step=250
        )
        
        if st.form_submit_button("Create Profile"):
            try:
                payload = {
                    "user_id": new_user_id,
                    "age": age,
                    "weight_kg": weight,
                    "activity_level": activity_level,
                    "daily_goal_ml": daily_goal
                }
                
                response = requests.post(f"{API_URL}/profile", json=payload)
                
                if response.status_code == 200:
                    st.success("✅ Profile created successfully!")
                    st.session_state["show_create_user"] = False
                    st.rerun()
                else:
                    st.error("❌ Failed to create profile")
            except Exception as e:
                st.error(f"Error: {e}")

if st.session_state.get("log_intake"):
    try:
        payload = {
            "user_id": user_id,
            "intake_ml": st.session_state.get("intake_value", 250)
        }
        
        with st.spinner("🔄 Analyzing your hydration..."):
            response = requests.post(f"{API_URL}/log-intake", json=payload)
        
        if response.status_code == 200:
            result = response.json()
            st.session_state["latest_analysis"] = result["analysis"]
            st.session_state["last_logged"] = datetime.now()
            st.success(f"✅ Logged {result['intake_ml']}mL successfully!")
            st.rerun()
        else:
            error_detail = response.text if response.text else "Unknown error"
            st.error(f"❌ Failed to log intake: {error_detail}")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

profile = get_profile_data(user_id) if user_id else None

if profile:
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Profile</div>
            <div style="font-size: 1.5rem; margin: 0.5rem 0;">
                {profile['age']} yrs • {profile['weight_kg']}kg
            </div>
            <div style="color: #94a3b8; font-size: 0.85rem;">
                {profile['activity_level'].title()} Activity
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Daily Goal</div>
            <div class="metric-value">{profile['daily_goal_ml']:,}</div>
            <div style="color: #94a3b8; font-size: 0.85rem;">milliliters</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Member Since</div>
            <div style="font-size: 1.2rem; margin: 0.5rem 0; color: #06b6d4;">
                {profile['created_at'][:10]}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    analytics = get_analytics_data(user_id)
    
    if analytics:
        score_class = get_score_color(analytics['hydration_score'])
        
        # Calculate today's intake from profile goal and completion percentage
        daily_goal = profile['daily_goal_ml']
        today_intake = int(daily_goal * analytics['goal_completion_percent'] / 100)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Hydration Score</div>
                <div class="metric-value {score_class}">
                    {analytics['hydration_score']:.0f}
                </div>
                <div style="color: #94a3b8; font-size: 0.8rem;">out of 100</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Today's Progress</div>
                <div class="metric-value">{analytics['goal_completion_percent']:.0f}%</div>
                <div style="color: #94a3b8; font-size: 0.8rem;">of daily goal</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Current Streak</div>
                <div class="metric-value">{analytics['current_streak']}</div>
                <div style="color: #94a3b8; font-size: 0.8rem;">days</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Best Streak</div>
                <div class="metric-value">{analytics['longest_streak']}</div>
                <div style="color: #94a3b8; font-size: 0.8rem;">days</div>
            </div>
            """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Weekly Average</div>
                <div class="metric-value">{analytics['weekly_average']:.0f}</div>
                <div style="color: #94a3b8; font-size: 0.8rem;">mL/day</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Monthly Average</div>
                <div class="metric-value">{analytics['monthly_average']:.0f}</div>
                <div style="color: #94a3b8; font-size: 0.8rem;">mL/day</div>
            </div>
            """, unsafe_allow_html=True)
        
        progress_percent = min(100, analytics['goal_completion_percent'])
        st.markdown(f"""
        <div style="margin: 2rem 0;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                <span style="color: #cbd5e1;">Today's Progress</span>
                <span style="color: #06b6d4; font-weight: bold;">
                    {today_intake:.0f} / {daily_goal} mL
                </span>
            </div>
            <div style="
                background: #1e293b;
                border-radius: 8px;
                height: 12px;
                overflow: hidden;
                border: 1px solid #334155;
            ">
                <div style="
                    background: linear-gradient(90deg, #06b6d4, #0891b2);
                    height: 100%;
                    width: {progress_percent}%;
                    transition: width 0.3s ease;
                "></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<div class='section-header'>📈 Hydration Trends</div>", unsafe_allow_html=True)
    
    history = get_history_data(user_id, days=30)
    
    if history and history["history"]:
        df = pd.DataFrame(history["history"])
        
        if not df.empty and "date" in df.columns:
            daily_totals = df.groupby("date")["intake_ml"].sum().reset_index()
            daily_totals = daily_totals.sort_values("date")
            
            fig = px.line(
                daily_totals,
                x="date",
                y="intake_ml",
                title="Daily Water Intake Trend",
                labels={"date": "Date", "intake_ml": "Intake (mL)"},
                template="plotly_dark"
            )
            
            if profile:
                fig.add_hline(
                    y=profile['daily_goal_ml'],
                    line_dash="dash",
                    line_color="green",
                    annotation_text="Daily Goal",
                    annotation_position="right"
                )
            
            fig.update_layout(
                hovermode="x unified",
                plot_bgcolor="#1e293b",
                paper_bgcolor="#0f172a",
                font=dict(color="#cbd5e1")
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown("<div class='section-header'>📊 History</div>", unsafe_allow_html=True)
            
            display_df = daily_totals.copy()
            display_df.columns = ["Date", "Total Intake (mL)"]
            display_df = display_df.sort_values("Date", ascending=False)
            
            st.dataframe(
                display_df,
                use_container_width=True,
                hide_index=True
            )
    else:
        st.info("📭 No intake history yet. Start logging to see trends!")
    
    st.markdown("<div class='section-header'>🤖 AI Coach Analysis</div>", unsafe_allow_html=True)
    
    if "latest_analysis" in st.session_state:
        st.markdown(f"""
        <div class="insight-box">
            <div class="insight-text">
                {st.session_state["latest_analysis"]}
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("💡 Log some water intake to receive AI-powered analysis and personalized recommendations!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📋 Get Weekly Report", use_container_width=True):
            try:
                with st.spinner("📊 Generating report..."):
                    response = requests.get(f"{API_URL}/weekly-report/{user_id}")
                
                if response.status_code == 200:
                    report = response.json()
                    
                    st.markdown("<div class='section-header'>📊 Weekly Report</div>", unsafe_allow_html=True)
                    
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric("Total Intake", f"{report['total_intake']:,} mL")
                    
                    with col2:
                        st.metric("Daily Average", f"{report['average_daily']:.0f} mL")
                    
                    with col3:
                        st.metric("Goal Achievement", f"{report['goal_achievement']:.0f}%")
                    
                    st.markdown(f"""
                    <div class="insight-box">
                        <div style="font-weight: bold; color: #06b6d4; margin-bottom: 0.5rem;">
                            📌 Assessment
                        </div>
                        <div class="insight-text">{report['overall_assessment']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(f"""
                    <div class="insight-box">
                        <div style="font-weight: bold; color: #06b6d4; margin-bottom: 0.5rem;">
                            💡 Key Insights
                        </div>
                        <div class="insight-text">
                            {'<br>'.join(['• ' + insight for insight in report['key_insights']])}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(f"""
                    <div class="insight-box">
                        <div style="font-weight: bold; color: #06b6d4; margin-bottom: 0.5rem;">
                            📈 Trend Analysis
                        </div>
                        <div class="insight-text">{report['trends']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(f"""
                    <div class="insight-box">
                        <div style="font-weight: bold; color: #06b6d4; margin-bottom: 0.5rem;">
                            ✅ Recommendations
                        </div>
                        <div class="insight-text">
                            {'<br>'.join(['• ' + rec for rec in report['recommendations']])}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error("Failed to generate report")
            except Exception as e:
                st.error(f"Error: {e}")
    
    with col2:
        if st.button("⚙️ Update Profile", use_container_width=True):
            st.session_state["show_update"] = True
    
    if st.session_state.get("show_update"):
        with st.form("update_profile_form"):
            new_age = st.number_input("Age (years)", value=profile['age'])
            new_weight = st.number_input("Weight (kg)", value=profile['weight_kg'])
            new_activity = st.selectbox(
                "Activity Level",
                ["sedentary", "light", "moderate", "heavy"],
                index=["sedentary", "light", "moderate", "heavy"].index(profile['activity_level'])
            )
            new_goal = st.number_input("Daily Goal (mL)", value=profile['daily_goal_ml'])
            
            if st.form_submit_button("Save Changes"):
                try:
                    profile_payload = {
                        "user_id": user_id,
                        "age": new_age,
                        "weight_kg": new_weight,
                        "activity_level": new_activity,
                        "daily_goal_ml": new_goal
                    }
                    
                    response = requests.put(f"{API_URL}/profile/{user_id}", json=profile_payload)
                    
                    if response.status_code == 200:
                        st.success("✅ Profile updated!")
                        st.session_state["show_update"] = False
                        st.rerun()
                    else:
                        st.error("Failed to update profile")
                except Exception as e:
                    st.error(f"Error: {e}")

else:
    if user_id:
        st.warning(f"👤 User '{user_id}' not found. Create a new profile or try another ID.")

st.divider()

st.caption("""
💧 **AI Hydration Intelligence Platform** • Powered by FastAPI, SQLite, LangChain, Ollama, and Llama 3.2

🔧 Built with professional architecture for scalability, maintenance, and future growth.
""")
