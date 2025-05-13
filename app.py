import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar datos
df = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Análisis de vehículos en venta en EE.UU.')

# Botón para histograma
if st.button('Mostrar histograma de odómetro'):
    st.write('Histograma de la columna odometer:')
    fig = px.histogram(df, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión
if st.button('Mostrar gráfico de dispersión (precio vs año del modelo)'):
    st.write('Gráfico de dispersión: Precio vs Año del modelo')
    fig2 = px.scatter(df, x='model_year', y='price')
    st.plotly_chart(fig2, use_container_width=True)