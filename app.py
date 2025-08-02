import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the trained model
with open('model_xgb.joblib', 'rb') as file:
    model = joblib.load(file)

# Define prediction function
def prediction(in_data):
    pred = model.predict([in_data])[0]
    if pred == 0:
        return "Sitting on bed"
    elif pred == 1:
        return "Sitting on chair"
    elif pred == 2:
        return "Lying on bed"
    else:
        return "Ambulating"

# Streamlit app interface
def main():
    st.title('Activity Prediction from Sensor Data')
    st.subheader('This application predicts the current activity based on sensor data provided.')
    st.image('image.webp')

    # Collect user inputs
    rfid = st.selectbox('RFID Configuration', ['Config 1 (4 sensors)', 'Config 2 (3 sensors)'])
    rfid_e = 3 if rfid == 'Config 2 (3 sensors)' else 4

    ant_ID = st.selectbox('Antenna ID', [1, 2, 3, 4])
    rssi = st.number_input('RSSI (Received Signal Strength Indicator)', step=1)

    accv = st.number_input("Vertical Acceleration", format="%.4f")
    accf = st.number_input("Frontal Acceleration", format="%.4f")
    accl = st.number_input("Lateral Acceleration", format="%.4f")

    in_data = [accf, accv, accl, ant_ID, rssi, rfid_e]

    if st.button('Predict'):
        response = prediction(in_data)
        st.success(f'Predicted Activity: {response}')

if __name__ == '__main__':
    main()
