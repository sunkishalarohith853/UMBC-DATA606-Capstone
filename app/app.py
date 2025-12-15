import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("crime_probability_model.pkl")

st.set_page_config(page_title="Chicago Crime Probability Predictor", layout="centered")

st.title("🔮 Chicago Crime Probability Prediction App")
st.write("Enter the conditions below to estimate the probability of a crime occurring.")

# ----------------------- USER INPUTS -----------------------

primary_type = st.selectbox(
    "Crime Category",
    [
        "THEFT", "BATTERY", "CRIMINAL DAMAGE", "ASSAULT", "DECEPTIVE PRACTICE",
        "OTHER OFFENSE", "NARCOTICS", "MOTOR VEHICLE THEFT", "ROBBERY",
        "BURGLARY", "CRIMINAL TRESPASS", "WEAPONS VIOLATION", "PUBLIC PEACE VIOLATION",
        "OFFENSE INVOLVING CHILDREN", "ARSON", "PROSTITUTION", "INTERFERENCE WITH PUBLIC OFFICER",
        "LIQUOR LAW VIOLATION", "GAMBLING", "KIDNAPPING", "INTIMIDATION"
    ]
)

location_description = st.selectbox(
    "Location Description",
    [
        "STREET", "RESIDENCE", "APARTMENT", "SIDEWALK", "ALLEY", "COMMERCIAL",
        "PARKING LOT", "RESTAURANT", "GAS STATION", "SCHOOL", "VEHICLE",
        "HOTEL", "HOSPITAL", "AIRPORT", "BANK", "CHA BUILDING"
    ]
)

hour = st.slider("Hour of Day", 0, 23, 12)

day_of_week = st.selectbox(
    "Day of Week",
    ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
)

month = st.selectbox("Month", list(range(1, 13)))

year = st.selectbox("Year", [2019, 2020, 2021, 2022, 2023])

# ----------------------- MODEL INPUT DF -----------------------

input_data = pd.DataFrame({
    "primary_type": [primary_type],
    "location_description": [location_description],
    "hour": [hour],
    "day_of_week": [day_of_week],
    "month": [month],
    "year": [year],
})

# ----------------------- PREDICTION -----------------------

if st.button("Predict Crime Probability"):
    proba = model.predict_proba(input_data)[0][1]  # Crime=1 probability
    st.subheader("📌 Prediction Result")
    st.write(f"*Estimated Crime Probability: {proba * 100:.2f}%*")

    if proba >= 0.7:
        st.error("🔴 Very High Likelihood of Crime")
    elif proba >= 0.4:
        st.warning("🟠 Medium Likelihood of Crime")
    else:
        st.success("🟢 Low Likelihood of Crime")