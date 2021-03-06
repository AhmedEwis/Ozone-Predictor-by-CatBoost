# -*- coding: utf-8 -*-
"""
Created on Nov 2021
Author: Ahmed Ewis
Supervised By: Dr. Fahad Al Fadli
               Dr. Nawaf Al Hajri
"""


import numpy as np
import pickle
import streamlit as st 

st.write("""Author: Ahmed Ewis""")
st.write("""Supervised By: Dr. Fahad Al Fadli and Dr. Nawaf Al Hajri""")
st.write("""Kuwait University""")

file_name = "xgb_reg_sklearn_local.pkl"
model_cat = pickle.load(open(file_name, "rb"))

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_ozone(year,month,quarter,dayofyear,dayofmonth,weekofyear,dayofweek,datehour,WD_Hour,WS_Hour,Temp_Hour,SR_Hour,RH_Hour,NO2):
    
    test = np.array([[year,\
    month,\
    quarter,\
    dayofyear,\
    dayofmonth,\
    weekofyear,\
    dayofweek,\
    datehour,\
    WD_Hour,\
    WS_Hour,\
    Temp_Hour,\
    SR_Hour,\
    RH_Hour,\
    NO2]])
    
    prediction=model_cat.predict(test)[0] 

    return prediction



def main():
    st.title("Welcome All to the Ozone Predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">O3 Predictor ML App in the North of Kuwait </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Year = st.text_input("Year","Type Here")
    Month = st.text_input("Month","Type Here")
    Quarter = st.text_input("Quarter","Type Here")
    Dayofyear = st.text_input("Dayofyear","Type Here")
    Dayofmonth = st.text_input("Dayofmonth","Type Here")
    Weekofyear = st.text_input("Weekofyear","Type Here")
    Dayofweek = st.text_input("Dayofweek","Type Here")
    Datehour = st.text_input("Datehour","Type Here")
    WD_Hour = st.text_input("WD-Hour","Type Here")
    WS_Hour = st.text_input("WS-Hour","Type Here")
    Temp_Hour = st.text_input("Temp-Hour","Type Here")
    SR_Hour = st.text_input("SR-Hour","Type Here")
    RH_Hour = st.text_input("RH-Hour","Type Here")
    NO2 = st.text_input("NO2","Type Here")
    #SO2 = st.text_input("SO2","Type Here")
    
    result=""
    if st.button("Predict"):
        result=predict_ozone(Year,Month,Quarter,Dayofyear,Dayofmonth,Weekofyear,Dayofweek,Datehour,WD_Hour,WS_Hour,Temp_Hour,SR_Hour,RH_Hour,NO2)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        #st.text("Author: Ahmed Ewis")
        #st.text("Supervised By: Dr. Fahad Al Fadli and Dr. Nawaf Al Hajri")
        st.text("Model Name: XGBoost Regressor")
        st.text("Built and Deployed with: Streamlit")

if __name__=='__main__':
    main()
