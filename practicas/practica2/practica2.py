#File: p2.py
#Date: 02 / 04 / 2024

import streamlit as st
import numpy as np
import pandas as pd
from scipy import stats as sst
from scipy import optimize as sco
import math
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import pandas as pd
from scipy import optimize as sco
import math
import plotly.express as px

#Path
path = "practicas/practica1/"

#Fondo temático
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://i.pinimg.com/564x/39/c7/1e/39c71e43cd06601a698edc75859dd674.jpg");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)


input_style = """
<style>
input[type="text"] {
    background-color: transparent;
    color: #a19eae;  // This changes the text color inside the input box
}
div[data-baseweb="base-input"] {
    background-color: transparent !important;
}
[data-testid="stAppViewContainer"] {
    background-color: transparent !important;
}
</style>
"""
st.markdown(input_style, unsafe_allow_html=True)

#Título
st.title('Predicción de COVID19')

# Párrafos justificados
st.markdown("""
    <div style="text-align: justify">
        La distribución binomial es un modelo de probabilidad discreto que indica la probabilidad de obtener uno de dos resultados posibles al realizar una serie de pruebas independientes.
    </div>
""", unsafe_allow_html=True)

# Lista
st.markdown()

# Más parrafos justificados
st.markdown("""
    <div style="text-align: justify">
            
    </div>
""", unsafe_allow_html=True)
#Notación matemática usando latex
st.latex(r"")
# Más parrafos justificados
st.markdown("""
    <div style="text-align: justify">
        
    </div>
    <br>
    <div style="text-align: justify">
       
    </div>        
""", unsafe_allow_html=True)
#Más notación de latex
st.latex(r"")

# Crear las pestanias
titulos_pestanias = ['Resumen del Proyecto', 'Procedimiento Experimental', 'Visualización de Resultados', 'Referencias']
pestanias = st.tabs(titulos_pestanias)
 
# Agregar contenido a cada pestania
with pestanias[0]:
    st.header('Resumen del Proyecto')

# Párrafo en la interfaz usando st.write()
    st.write("El informe incluyó dos partes:")
 
with pestanias[1]:
    


 
with pestanias[2]:
    st.header('Histogramas')


    st.title('')


#Utilizamos pandas para leer nuestro archivo csv
    data = pd.read_csv(path+'datos.csv')
    print(f'data:\n{data}')

    data = data.loc[:m_1]


with pestanias[3]:
    st.header('Referencias')
    st.write('')

