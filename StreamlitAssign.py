import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px

# Load data
df = pd.read_csv("Country Data set.csv")

df['Population'] = df['Population'].str.replace(',', '').astype(float)


st.title("Streamlit Assignment")
st.markdown("By: Haya Moubayed")

# Logo
logo = Image.open("American University of Beirut-AUB LOGO.png")
st.image(logo)

# Sidebar widget for selecting the plot
choice = st.sidebar.radio("What do you want to see?", ["Unemployment Plot", "Forested Areas Plot"])


if choice == "Unemployment Plot":
    st.sidebar.header("Unemployment Plot Filters")
    
    # Round the maximum population value to the nearest integer
    max_population = int(round(df['Population'].max()))
    population_slider= st.sidebar.slider("Population Slider", min_value=0, max_value=max_population, step=1000, value=1000000)
    filtered_df = df[df['Population'] > population_slider]
    fig1 = px.scatter(data_frame=filtered_df, x='Population', y='Unemployment rate', log_x=True, hover_name='Country', title='Unemployment rate by population')
    st.plotly_chart(fig1)
elif choice == "Forested Areas Plot":
    st.sidebar.header("Forested Areas Plot Filters")
    max_area=int(round(df['Land Area(Km2)'].max()))
    area_slider= st.sidebar.slider("Area slider", min_value=0, max_value=max_area, step=1000, value=1000000)
    filtered_df2 = df[df['Land Area(Km2)'] > area_slider]
    fig2 = px.scatter(data_frame=filtered_df2, x='Land Area(Km2)', y='Forested Area (%)', range_x=[0, 500000], color_continuous_scale='Greens', color='Forested Area (%)', hover_name='Country', title='Forested area by Land Area')
    st.plotly_chart(fig2)


