import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model
with open("fraud_detection_rf.pkl", "rb") as file:
    model = pickle.load(file)

# Load feature names
with open("model_features.pkl", "rb") as f:
    feature_names = pickle.load(f)

st.title("🏥 Healthcare Provider Fraud Detection")
st.write("Predict potential fraud risk based on provider billing patterns.")

st.sidebar.header("Enter Provider Details")

# User inputs
inpatient_claims = st.sidebar.number_input("Inpatient Claims", min_value=0)
outpatient_claims = st.sidebar.number_input("Outpatient Claims", min_value=0)

inpatient_reimb = st.sidebar.number_input("Inpatient Reimbursement", min_value=0.0)
outpatient_reimb = st.sidebar.number_input("Outpatient Reimbursement", min_value=0.0)

inpatient_deductible = st.sidebar.number_input("Inpatient Deductible Paid", min_value=0.0)
outpatient_deductible = st.sidebar.number_input("Outpatient Deductible Paid", min_value=0.0)

# 🔑 Derived features (MUST match training)
total_claims = inpatient_claims + outpatient_claims
total_reimbursement = inpatient_reimb + outpatient_reimb
total_deductible = inpatient_deductible + outpatient_deductible

# Create DataFrame in EXACT training order
input_data = pd.DataFrame([[
    inpatient_claims,
    inpatient_reimb,
    inpatient_deductible,
    outpatient_claims,
    outpatient_reimb,
    outpatient_deductible,
    total_claims,
    total_reimbursement,
    total_deductible
]], columns=feature_names)


# Prediction
if st.button("Predict Fraud Risk"):
    prob = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    st.write(f"**Fraud Probability:** {prob:.2f}")

    if prob >= 0.4:
        st.error("⚠️ High Risk Provider – Audit Recommended")
    else:
        st.success("✅ Low Risk Provider")
