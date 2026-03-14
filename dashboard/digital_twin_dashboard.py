
import streamlit as st
import pandas as pd

st.title("Digital Twin Energy Monitoring Dashboard")

data = pd.read_csv("ml_energy_dataset.csv")

st.subheader("Energy Consumption Data")
st.dataframe(data)

st.subheader("Energy Consumption Chart")
st.line_chart(data.set_index("hour")["energy_kwh"])

st.subheader("Temperature Impact")
st.line_chart(data.set_index("hour")["temperature"])

st.write("This dashboard simulates a Digital Twin monitoring system for industrial energy optimization.")
