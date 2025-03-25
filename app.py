import streamlit as st
import pandas as pd
import joblib

# Load models & scalers
# log_model = joblib.load('logistic_model.pkl')
rf_model = joblib.load('rf_classifier.pkl')
scaler_clf = joblib.load('scaler_clf.pkl')

# Initialize session state for approval status
if "approval_status" not in st.session_state:
    st.session_state.approval_status = None

st.title('Medical Insurance Approval and Claim Estimator!')

# Step 1: Insurance Approval Check
st.header('Step 1: Check if your insurance claim is approved')

# User Inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)
charges = st.number_input("Medical Charges", min_value=0, value=5000)
smoker = st.selectbox("Smoker?", ["No", "Yes"])
diabetes = st.selectbox("Diabetes Condition", ["No", "Controlled", "Uncontrolled"])
cholesterol = st.selectbox("Cholesterol Level", ["Normal", "High"])
hypertension = st.selectbox("Hypertension Condition", ["No", "Controlled", "Uncontrolled"])
exercise = st.selectbox("Do you exercise regularly?", ["No", "Yes"])
policy_type = st.selectbox("Policy Type", ["Basic", "Standard", "Premium"])

# Define policy max payout
max_payout_dict = {"Basic": 30000, "Standard": 50000, "Premium": 75000}
max_payout = max_payout_dict[policy_type]

# Encode categorical values
smoker_encoded = 1 if smoker == "Yes" else 0
diabetes_encoded = 2 if diabetes == "Uncontrolled" else (1 if diabetes == "Controlled" else 0)
cholesterol_encoded = 1 if cholesterol == "High" else 0
hypertension_encoded = 2 if hypertension == "Uncontrolled" else (1 if hypertension == "Controlled" else 0)
exercise_encoded = 1 if exercise == "Yes" else 0

# Create DataFrame
user_data = pd.DataFrame([[age, charges, smoker_encoded, diabetes_encoded, cholesterol_encoded, 
                           hypertension_encoded, exercise_encoded, max_payout]],
                         columns=['age', 'charges', 'smoker_encoded', 'diabetes_encoded', 
                                  'cholesterol_encoded', 'hypertension_encoded', 'exercise_encoded', 'max_payout'])

# Scale the input for classification
user_data_scaled = scaler_clf.transform(user_data) 

# Approval Prediction Button
if st.button("Check Approval"):
    st.session_state.approval_status = rf_model.predict(user_data_scaled)[0]

# Step 2: Estimate Claim Amount (Only if approved)
if st.session_state.approval_status == 1:
    st.success("✅ Your claim has been approved!")
    st.header("Step 2: Estimate Your Claim Amount")
    st.write(f"💰 Your policy's max payout is ₹{max_payout}")

    # Function to calculate received amount
    def calculate_received_amount(row):
        claim_amount = min(row['charges'], row['max_payout'])  # Cap at max payout
        deduction = 0
        if row['smoker_encoded'] == 1:
            deduction += 0.10  # 10% reduction for smokers
        if row['diabetes_encoded'] == 2:
            deduction += 0.10  # 10% reduction for controlled diabetes
        if row['diabetes_encoded'] == 1:
            deduction += 0.05  # 5% reduction for controlled diabetes
        if row['hypertension_encoded'] == 1:
            deduction += 0.10  # 10% reduction for controlled hypertension
        if row['hypertension_encoded'] == 2:
            deduction += 0.05  # 10% reduction for controlled hypertension
        if row['cholesterol_encoded'] == 1:
            deduction += 0.10  # 10% reduction for high cholesterol  
        if row['exercise_encoded'] == 1:
            deduction -= 0.05  # 5% increase if exercising

        received_amount = claim_amount * (1 - deduction)
        return max(received_amount, 0)  # Ensure non-negative value

    # Button for claim estimation
    if st.button("Estimate Claim Amount"):
        received_amount = calculate_received_amount(user_data.iloc[0])
        st.success(f"💰 Estimated Claim Amount: ₹{received_amount:.2f}")

elif st.session_state.approval_status == 0:
    st.error("❌ Your claim was not approved.")
