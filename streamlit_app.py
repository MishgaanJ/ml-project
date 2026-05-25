import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("models/best_model.pkl")

st.set_page_config(page_title="CTG Fetal Health Predictor")

st.title("🫀 CTG Fetal Health Prediction App")
st.write("Enter patient CTG parameters to predict fetal state (NSP).")

# Input fields (important features only — not all 21 to keep UI clean)

LB = st.number_input("Baseline FHR (LB)", value=120)
AC = st.number_input("Accelerations (AC)", value=0.0)
FM = st.number_input("Fetal Movements (FM)", value=0.0)
UC = st.number_input("Uterine Contractions (UC)", value=0.0)
DL = st.number_input("Light Decelerations (DL)", value=0.0)
DS = st.number_input("Severe Decelerations (DS)", value=0.0)
ASTV = st.number_input("% of Abnormal Short Term Variability (ASTV)", value=0.0)
MSTV = st.number_input("Mean Short Term Variability (MSTV)", value=0.0)
ALTV = st.number_input("% of Abnormal Long Term Variability (ALTV)", value=0.0)
MLTV = st.number_input("Mean Long Term Variability (MLTV)", value=0.0)

if st.button("Predict Fetal Health"):
    features = np.array([[LB, AC, FM, UC, DL, DS, ASTV, MSTV, ALTV, MLTV]])
    
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.success("Normal Fetal State 🟢")
    elif prediction == 2:
        st.warning("Suspect Fetal State 🟡")
    else:
        st.error("Pathologic Fetal State 🔴")