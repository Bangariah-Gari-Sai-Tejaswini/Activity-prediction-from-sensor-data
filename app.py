
import streamlit as t
import numpy as np
import pandas as pd
import joblib

with open('model_xgb.joblib','rb') as file:
    model = joblib.load(file)

def prediction(in_data):
    pred = model.predict([in_data])[0]
    if pred==0:
        return "Sitting on bed"
    elif pred==1:
        return "Sitting on chair"
    elif pred ==2:
        return "Lying on bed"
    else:
        return "Ambulating"

def main():
    st.title('Activity prediction from sensor data')
    st.subheader('''This application tool will predict the on going activity of the basis of sensor data provided.Fill the resepective fields''')
    st.image('image.webp')
    
    rfid = st.dropbox("Enter the rfid configuration settings',['Config 1 (4 sensors)','Config 2 (3 sensors)'])
    rfid_e = (lambda x: 3 if x=='Config 2 (3 sensors)' else 4)(rfid)
              
    ant_ID = st.dropbox('Select the Antenna ID',[1,2,3,4])
    rssi = st.selectbox('Enter the received signal strength indicator {RSSI}')
                      
    accv = st.text_input("Enter the vertical acceleration data")
    accf = st.text_input("Enter the frontal acceleration data")                
    accl = st.text_input("Enter the lateral acceleration data")  
                      
    in_data = [accf,accv,accl,ant_ID,rssi,rfid_e]
                      
    if st.button('Predict'):
                      response = prediction(in_data)
                      st.success(response)
                      
if __name__ == '__main__':
                      main()
              
