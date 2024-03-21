import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image

model=pickle.load(open("nba_sp.pkl","rb"))
st.title("Basketball Salary Predictor")
st.sidebar.header('Player Data')
img=Image.open("pexels-markus-spiske-1752757.jpg")
st.image(img)

def user_report():
    rating=st.sidebar.number_input('Player rating',0,100)
    geo=st.sidebar.selectbox("Country",("USA","Canada","Australia","Others"))
    if (geo=="USA"):
        country=0
    elif(geo=="Canada"):
        country=1
    elif(geo=="Australia"):
        country=2
    else:
        country=3
    draft_year=st.sidebar.slider("Draft year",2000,2050)
    draft_round=st.sidebar.slider("Draft round",1,20)
    draft_peak=st.sidebar.slider("Draft peak",1,50)
    Age=st.sidebar.number_input("Age",1,100)


    user_report_data = {
        "rating": rating,
        "country": country,
        "draft_year": draft_year,
        "draft_round": draft_round,
        "draft_peak": draft_peak,
        "Age": Age
    }
    report_data=pd.DataFrame(user_report_data,index=[0])
    return report_data
user_data=user_report()

st.subheader("Player Data Summary")
st.write(user_data)

salary=model.predict(user_data)
st.subheader("Player Salary")
st.subheader("$"+str(np.round(salary[0])))


