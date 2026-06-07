import requests
import pandas as pd
import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Water Tracker",
    page_icon="💧",
    layout="wide"
)

# -----------------------------
# Custom Styling
# -----------------------------
st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.metric-card {
    background-color: #1e293b;
    padding: 1rem;
    border-radius: 12px;
    text-align: center;
}

.big-number {
    font-size: 2rem;
    font-weight: bold;
}

.analysis-box {
    padding: 1rem;
    border-radius: 12px;
    border: 1px solid #334155;
    background-color: #0f172a;
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3rem;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

API_URL = "http://127.0.0.1:8000"

# -----------------------------
# Header
# -----------------------------
st.title("AI Water Tracker")
st.caption(
    "Track hydration habits and receive AI-powered insights generated locally with Llama 3.2."
)

st.divider()

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.header("Daily Intake")

    user_id = st.text_input(
        "User ID",
        value="aditya"
    )

    intake_ml = st.number_input(
        "Water Intake (mL)",
        min_value=0,
        max_value=10000,
        value=500,
        step=100
    )

    submit = st.button("Analyze & Save")

# -----------------------------
# Main Layout
# -----------------------------
left, right = st.columns([1, 1])

# -----------------------------
# Save Intake
# -----------------------------
if submit:

    payload = {
        "user_id": user_id,
        "intake_ml": intake_ml
    }

    try:

        with st.spinner("Generating AI hydration analysis..."):

            response = requests.post(
                f"{API_URL}/log-intake",
                json=payload
            )

        if response.status_code == 200:

            result = response.json()

            st.session_state["latest_analysis"] = result["analysis"]

            st.success("Water intake logged successfully.")

        else:
            st.error("Backend returned an error.")

    except Exception as e:
        st.error(f"Unable to connect to API: {e}")

# -----------------------------
# Load History
# -----------------------------
history_data = []

try:

    history_response = requests.get(
        f"{API_URL}/history/{user_id}"
    )

    if history_response.status_code == 200:

        history_data = history_response.json()["history"]

except:
    pass

# -----------------------------
# Metrics
# -----------------------------
with left:

    st.subheader("Hydration Metrics")

    if history_data:

        df = pd.DataFrame(
            history_data,
            columns=["Water Intake (mL)", "Date"]
        )

        total_intake = df["Water Intake (mL)"].sum()
        average_intake = int(df["Water Intake (mL)"].mean())

        c1, c2 = st.columns(2)

        with c1:
            st.metric(
                "Total Logged",
                f"{total_intake:,} mL"
            )

        with c2:
            st.metric(
                "Average Intake",
                f"{average_intake:,} mL"
            )

        st.subheader("History")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.subheader("Hydration Trend")

        chart_df = df.copy()
        chart_df = chart_df.groupby("Date").sum()

        st.line_chart(chart_df)

    else:
        st.info("No hydration records found.")

# -----------------------------
# AI Analysis
# -----------------------------
with right:

    st.subheader("AI Hydration Coach")

    if "latest_analysis" in st.session_state:

        st.markdown(
            f"""
            <div class="analysis-box">
            {st.session_state["latest_analysis"]}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.info(
            "Submit a water intake record to receive AI feedback."
        )

# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption(
    "Powered by FastAPI, SQLite, LangChain, Ollama, and Llama 3.2"
)