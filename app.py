# ===== IMPORTS (TOP OF FILE) =====
import streamlit as st
import random
import time
import cv2


# ===== PAGE TITLE =====
st.set_page_config(page_title="Smart Emergency Healthcare", layout="wide")
st.title("Emotion-Aware Agentic AI Smart Emergency Healthcare System")
st.write("Real-time emergency monitoring dashboard")


# ===== ALERT STORAGE =====
if "alerts" not in st.session_state:
    st.session_state.alerts = []


# ===== EMOTION SIMULATION =====
def simulate_emotions():
    fear = random.randint(0, 100)
    stress = random.randint(0, 100)
    panic = random.randint(0, 100)
    return fear, stress, panic


# ===== HEALTH DATA SIMULATION =====
def simulate_health():
    heart_rate = random.randint(60, 150)
    temperature = round(random.uniform(36, 40), 1)
    motion = random.choice(["Normal", "Low", "Critical"])
    return heart_rate, temperature, motion


# ===== RISK CALCULATION =====
def calculate_risk(fear, stress, panic, heart_rate, temperature):
    score = fear + stress + panic

    if score > 200 or heart_rate > 130 or temperature > 39:
        return "CRITICAL"
    elif score > 120:
        return "MEDIUM"
    else:
        return "LOW"


# ===== AI DECISION =====
def ai_decision(risk):
    if risk == "LOW":
        return "Normal Monitoring"
    elif risk == "MEDIUM":
        return "Warning Issued"
    else:
        return "Emergency Triggered"


# ===== CAMERA EMOTION DETECTION =====
def detect_emotion_camera():

    cap = cv2.VideoCapture(0)

    st.write("Opening Camera... Click stop to exit")

    run = st.checkbox("Start Camera")
    FRAME_WINDOW = st.image([])

    fear = 0
    stress = 0
    panic = 0

    if run:
        ret, frame = cap.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            FRAME_WINDOW.image(frame)

            # SIMULATED EMOTION (real AI model later)
            fear = random.randint(0, 100)
            stress = random.randint(0, 100)
            panic = random.randint(0, 100)

    cap.release()

    return fear, stress, panic


# ===== SIDEBAR INPUT =====
st.sidebar.title("Input Source")

mode = st.sidebar.radio(
    "Select Emotion Input",
    ["Simulation", "Camera Detection"]
)


# ===== GENERATE DATA =====
if mode == "Simulation":
    fear, stress, panic = simulate_emotions()
else:
    fear, stress, panic = detect_emotion_camera()

heart_rate, temperature, motion = simulate_health()
risk = calculate_risk(fear, stress, panic, heart_rate, temperature)
decision = ai_decision(risk)


# ===== EMOTION DISPLAY =====
st.subheader("Emotion Detection")

col1, col2, col3 = st.columns(3)
col1.metric("Fear %", fear)
col2.metric("Stress %", stress)
col3.metric("Panic %", panic)


# ===== HEALTH MONITORING =====
st.subheader("Health Monitoring")

st.write("Heart Rate:", heart_rate, "bpm")
st.write("Body Temperature:", temperature, "°C")
st.write("Motion Status:", motion)


# ===== RISK LEVEL =====
st.subheader("Risk Level")

if risk == "LOW":
    st.success("LOW RISK")
elif risk == "MEDIUM":
    st.warning("MEDIUM RISK")
else:
    st.error("CRITICAL RISK")


# ===== AI DECISION OUTPUT =====
st.subheader("AI Decision")
st.write(decision)


# ===== EMERGENCY ALERT =====
if risk == "CRITICAL":
    st.error("🚨 EMERGENCY ALERT")
    st.write("Ambulance notified")
    st.write("Location shared with hospital")
    st.session_state.alerts.append("Emergency triggered")


# ===== ALERT HISTORY =====
st.subheader("Alert History")
st.write(st.session_state.alerts)


# ===== EMOTION GRAPH =====
st.subheader("Emotion Trend")

chart_data = {
    "Fear": fear,
    "Stress": stress,
    "Panic": panic
}

st.bar_chart(chart_data)


# ===== AUTO REFRESH =====
time.sleep(2)
st.rerun()