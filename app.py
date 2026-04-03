import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("jhabua_weather_data.csv")

def recommend_crop(temp, rainfall):
    if rainfall > 120 and 25 <= temp <= 32:
        return "Soybean"
    elif rainfall < 100:
        return "Wheat"
    else:
        return "Maize"

st.title("🌤️ Weather Forecasting & Crop Dashboard")

city = st.selectbox("Select Location", df["city"])

row = df[df["city"] == city].iloc[0]

st.metric("Temperature", row["temperature"])
st.metric("Humidity", row["humidity"])
st.metric("Rainfall", row["rainfall"])

crop = recommend_crop(row["temperature"], row["rainfall"])
st.write(f"🌾 Recommended Crop: {crop}")

# Forecast (demo)
days = [f"Day {i+1}" for i in range(15)]
temp = np.random.normal(row["temperature"], 1.5, 15)
rain = np.random.normal(row["rainfall"], 10, 15)

forecast = pd.DataFrame({
    "Day": days,
    "Temperature": temp,
    "Rainfall": rain
})

st.line_chart(forecast.set_index("Day"))
