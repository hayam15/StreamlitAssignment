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

st.write(df)


