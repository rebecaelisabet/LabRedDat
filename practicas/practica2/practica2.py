import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
 
# Cargar algunos datos
datos = pd.read_csv('datos.csv')
 
st.title('Mi Aplicación de Visualización de Datos')
 
# Crear las pestañas
titulos_pestañas = ['Gráfico de Barras', 'Gráfico de Dispersión', 'Mapa de Calor']
pestañas = st.tabs(titulos_pestañas)
 
# Agregar contenido a cada pestaña
with pestañas[0]:
    st.header('Gráfico de Barras')
    st.bar_chart(datos)
 
with pestañas[1]:
    st.header('Gráfico de Dispersión')
    fig, ax = plt.subplots()
    ax.scatter(datos['x'], datos['y'])
    st.pyplot(fig)
 
with pestañas[2]:
    st.header('Mapa de Calor')
    st.heatmap(datos.corr())