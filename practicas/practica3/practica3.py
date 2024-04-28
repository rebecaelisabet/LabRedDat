import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
 
st.title('Decaimiento de Cesio-137')

# Fondo temático
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://i.pinimg.com/564x/c1/97/7d/c1977de3ed571607a33c3c3e59691e6b.jpg");
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

st.subheader("¿Qué es la distribución de Poisson?")
st.markdown("""
La distribución de Poisson es una distribución de probabilidad discreta que describe la probabilidad de que ocurra un determinado número de eventos en un intervalo de tiempo o espacio, dado un valor promedio de ocurrencias. Es útil para modelar situaciones donde los eventos ocurren de manera independiente a una tasa constante en un intervalo de tiempo o espacio específico, como el número de llamadas telefónicas que recibe un centro de atención al cliente en una hora, el número de accidentes de tráfico en un tramo de carretera en un día o el número de partículas radiactivas emitidas por un material en un intervalo de tiempo.
            
La distribución de Poisson se caracteriza por un solo parámetro, denotado como lambda (λ), que representa la tasa promedio de ocurrencia de eventos en el intervalo considerado. La fórmula para la probabilidad de que ocurran exactamente k eventos en ese intervalo es:
""")

#Notación matemática usando latex
st.latex(r"P(x,n)=\frac{e^{-\mu}\mu^k}{k!}")
st.markdown("""
Donde:
            
- $P(X=k)$ es la probabilidad de que ocurran k eventos.

- e es la base del logaritmo natural
            
- $\mu$ es la tasa promedio de ocurrencia de eventos en el intervalo
            
- k  es el número de eventos que estamos interesados en calcular.
            
 La distribución de Poisson es especialmente útil cuando el número de eventos es grande y la probabilidad de que ocurra un evento en un intervalo de tiempo muy pequeño es muy pequeña. Además, la distribución de Poisson se relaciona con la distribución binomial cuando el número de ensayos es grande y la probabilidad de éxito es pequeña.           
""") 
#Distribucion Gaussiana
st.subheader("¿Qué es la distribución Gaussiana?")
st.markdown("""
La distribución Gaussiana, también conocida como distribución normal, es una de las distribuciones de probabilidad más importantes y ampliamente utilizadas en estadística y teoría de la probabilidad. Es especialmente útil debido a sus propiedades matemáticas y su capacidad para modelar una amplia variedad de fenómenos en la naturaleza y en diferentes campos de estudio.

La distribución Gaussiana se caracteriza por su forma de campana simétrica y su curva suave. La función de densidad de probabilidad de una distribución normal está dada por la fórmula:
""")

#Notación matemática usando latex
st.latex(r"f(x|\mu,\sigma )=\frac{1}{\sigma\sqrt{2\pi}}e^{\frac{-(x-\mu)^2}{2\sigma^2}}")
st.markdown("""
Donde:
            
- $x$ es la variable aleatoria.

- $\mu$ es la media de la distribución, que indica el valor central o la tendencia central de los datos
            
- $\sigma$ es la desviación estándar, que indica la dispersión o la variabilidad de los datos.
            
La distribución Gaussiana tiene las siguientes propiedades:

- Simetría: La distribución es simétrica en torno a su media.

- Media, Mediana y Moda: La media, la mediana y la moda de la distribución son iguales y están ubicadas en $\mu$

- Campana: La distribución tiene una forma de campana, con la mayoría de los valores concentrados cerca de la media y una dispersión decreciente a medida que nos alejamos de ella.

- Regla 68-95-99.7: Aproximadamente el 68% de los datos están dentro de una desviación estándar de la media, el 95% dentro de dos desviaciones estándar y el 99.7% dentro de tres desviaciones estándar.
""") 
#Chi-cuadrado

st.subheader("¿Qué Chi-cuadrado?")
st.markdown("""
La prueba de chi-cuadrado, también conocida como prueba de bondad de ajuste de chi-cuadrado, es una técnica estadística utilizada para determinar si existe una diferencia significativa entre las frecuencias observadas y las frecuencias esperadas en un conjunto de datos categóricos. Es una prueba no paramétrica, lo que significa que no requiere ninguna suposición sobre la distribución subyacente de los datos.
            
La prueba de chi-cuadrado se utiliza en una variedad de aplicaciones, como pruebas de independencia en tablas de contingencia, pruebas de bondad de ajuste para comparar una distribución observada con una teórica, y en análisis de regresión para evaluar la bondad de ajuste del modelo. Es una herramienta útil para analizar datos categóricos y determinar si hay una relación significativa entre las variables categóricas.
""")

#Contadorde Geiger
st.subheader("¿Qué es el contador de Geiger?")
st.markdown("""
El contador Geiger es un dispositivo utilizado para detectar la radiación ionizante, como los rayos alfa, beta y gamma. Consiste en un tubo lleno de gas (generalmente argón o helio) a baja presión, con un electrodo central y un electrodo externo que actúan como un condensador. Cuando una partícula cargada ioniza el gas dentro del tubo, se genera un pulso eléctrico detectable por el contador.

Cuando una partícula ionizante pasa a través del tubo, ioniza los átomos del gas, liberando electrones. Estos electrones, al acelerarse bajo la acción de un campo eléctrico, generan más ionizaciones en cascada, lo que produce una avalancha de electrones y iones positivos. Esto provoca un aumento rápido en la corriente eléctrica que puede ser detectado por el contador. El número de pulsos eléctricos registrados por el contador está relacionado con la intensidad de la radiación ionizante presente en el entorno.
            
Los contadores Geiger son ampliamente utilizados en aplicaciones de monitoreo de radiación, como en la industria nuclear, la medicina, la investigación científica y la protección radiológica. Son dispositivos portátiles, sensibles y relativamente económicos, lo que los hace ideales para la detección rápida y el monitoreo de la radiación en diferentes entornos.
""")




# Crear las pestañas
titulos_pestañas = ['Resumen del proyecto', 'Visualización de Datos', 'Análisis de Datos', 'Conclusiones', 'Referencias']
pestañas = st.tabs(titulos_pestañas)
 
# Agregar contenido a cada pestaña
with pestañas[0]:
    st.header('¿Qué se hizo en el Proyecto?')
    st.markdown("""
    Este reporte presenta un análisis detallado de las mediciones realizadas en clase, con el objetivo de implementar ajustes de las distribuciones de Poisson y Gaussiana. Además, se llevó a cabo la prueba de "chi-cuadrado" para cada ajuste, con el fin de determinar cuál de las distribuciones se adapta mejor al caso experimental.
    
   Procedimiento Experimental:
    - Se utilizaron mediciones realizadas en clase como datos experimentales.
                
    - Se implementaron ajustes de las distribuciones de Poisson y Gaussiana a los datos.
                
    - Se realizó la prueba de "chi-cuadrado" para cada ajuste.
                
    - Se compararon los resultados de las pruebas de "chi-cuadrado" para determinar la distribución que mejor se ajusta a los datos experimentales.

    """)
 
with pestañas[1]:
    st.header('Visualización de Datos')
    
 
with pestañas[2]:
    st.header('Análisis de Datos')
    

with pestañas[3]:
    st.header('Conclusiones')
    

with pestañas[4]:
    st.header('Referencias')
    