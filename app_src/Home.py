import streamlit as st
import numpy as np
import pandas as pd
import joblib 


model_package = joblib.load(r"model\rainfall_model_package.joblib")
model = model_package['model']

df = pd.read_csv(r"data\test_data.csv")
X = df.drop('RainTomorrow', axis=1)
y = df['RainTomorrow']


st.set_page_config(page_title="Rain Prediction", layout="wide")

st.title("🌧️ Rain Prediction App")
st.write("Welcome to the Rain Prediction App. Navigate to 'Predict' to start forecasting.")

