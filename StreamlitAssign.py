import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px

#C:\Users\hayam\Downloads\
logo=Image.open("American University of Beirut-AUB LOGO.png")
st.image(logo)
st.title("Streamlit Assignment")
st.markdown("By: Haya Moubayed")

#r"C:\Users\hayam\Documents\MSBA 325\1st Session\

df= pd.read_csv("Country Data set.csv")
choice=st.radio("What do you want to see?",["Unemployment Plot","Forested Areas Chart"])
if choice=="Unemployment Plot":
    fig1=px.scatter(data_frame=df,x='Population',y='Unemployment rate',log_x=True, hover_name='Country', range_x=[100000,1000000000], title='Unemployment rate by population')
    st.plotly_chart(fig1)
elif choice=="Forested Areas Chart":
    fig2=px.scatter(data_frame=df, x='Land Area(Km2)', y='Forested Area (%)',range_x=[0,500000],color_continuous_scale='Greens', color='Forested Area (%)', hover_name='Country', title='forested area by Land Area')
    st.plotly_chart(fig2)



