import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('notebooks/vehicles_us.csv') # leer los datos

st.header('Proyecto - Sprint 7 - Aplicacion web de datos')
hist_button = st.button('Construir histograma') # crear un botón
scatter_button = st.button('Construir diagrama de dispersion') # crear un botón

if hist_button: # al hacer clic en el botón
    
    # escribir un mensaje
    st.write('Histograma correspondiente al precio del conjunto de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="price")

    # mostrar el grafico
    st.plotly_chart(fig, use_container_width=True)


if scatter_button: # al hacer clic en el botón
    
    # escribir un mensaje
    st.write('Diagrama de dispersion de precio respecto a dias listados')

    # crear un histograma
    fig = px.scatter(car_data, x="price", y='days_listed')

    # mostrar el grafico
    st.plotly_chart(fig, use_container_width=True)
