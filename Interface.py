import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load('Assurance_model.pkl')

st.title('Estimation des charges d\'assurance:')

age = st.number_input("Âge", min_value=0, max_value=120, value=30)
sex = st.selectbox("Sexe", options=["male", "female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=27.9, format="%.3f")
children = st.number_input("Nombre d'enfants", min_value = 0, max_value=10, value=0)
smoker = st.selectbox("Fumeur", options=["yes", "no"])
region = st.selectbox("Region", options=["southwest", "southeast", "northwest", "northeast"])

input_df = pd.DataFrame({
    'age': [age],
    'sex': [sex],
    'bmi': [bmi],
    'children': [children],
    'smoker': [smoker],
    'region': [region]
})

if st.button("Estimer la charge"):
    pred = model.predict(input_df)

    st.success(f"Estimation des charges : {pred[0]:.3f}")