import streamlit as st
import numpy as np
import string
import pickle
import sklearn
from sklearn.ensemble import RandomForestClassifier
st.set_option('deprecation.showfileUploaderEncoding',False) 
model = pickle.load(open('model.pkl','rb'))


def main():
    st.sidebar.header("Diabetes Risk Prediction for Females.")
    st.sidebar.text("This a Web app that tells you Wheather you have Diabetes or not.")
    st.sidebar.header("Just fill in the information below")
    st.sidebar.text("The RandomForestClassifier was used.")



Pregnancies = st.slider("Input Your Number of Pregnancies", 0, 16)
Glucose = st.slider("Input your Gluclose",74,200)
BloodPressure = st.slider("Input your Blood Pressure",30,130)
SkinThickness = st.slider("Input your Skin thickness",0, 100)
Insulin = st.slider("Input your Insulin",0,200)
BMI = st.slider("Input your BMI",14.0,60.0)
DiabetesPedigreeFunction = st.slider("Input your Diabetes Pedigree Function",0.0,6.0)
Age = st.slider("Input your Age",0, 100)

inputs = [[Pregnancies, Glucose,BloodPressure,SkinThickness,Insulin, BMI, DiabetesPedigreeFunction, Age]]

if st.button('Predict'):
    result = model.predict(inputs)
    updated_res = result.flatten().astype(int)
    if updated_res == 0:
        st.write("Sorry, You Might Have Diabetes. Take Care Of Yourselves")
    else:
        st.write("You are Safe now. But take care of your Health.")
if __name__ =='__main__':
    main()
