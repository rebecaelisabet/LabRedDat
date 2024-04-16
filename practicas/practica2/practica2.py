import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Fondo temático
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://i.pinimg.com/564x/8b/2c/4e/8b2c4e50f131160938153449e8b8dad2.jpg");
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
 
# Cargar algunos datos
#datos = pd.read_csv('datos.csv')

# Agrega el enlace de la fuente cursiva de Google Fonts a tu aplicación
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Homemade Apple&display=swap" rel="stylesheet">
    """,
    unsafe_allow_html=True
)

# Aplica la fuente cursiva a un título y texto en tu aplicación
st.markdown("""
    <h1 style='font-family: "Homemade Apple", cursive; text-align: center;'>Predicción de Covid 2019</h1>
    """,
    unsafe_allow_html=True
)


# Parrafos justificados
st.markdown("""
    <div style="text-align: justify">
        ¿Qué es el COVID?    
    </div>
    <br>
    <div style="text-align: justify">
        Los coronavirus son una extensa familia de virus que pueden provocar una variedad de enfermedades, desde el resfriado común hasta afecciones más graves, como el síndrome respiratorio de Oriente Medio (MERS-CoV) y el síndrome respiratorio agudo severo (SRAS-CoV).    
    </div>
    <br>
    <div style="text-align: justify">
        Un nuevo coronavirus es una cepa que no se había visto previamente en humanos, como el 2019nCoV o COVID-19, identificado por primera vez durante el brote en Wuhan, China, en diciembre de 2019.    
    </div>
    <br>
    <div style="text-align: justify">
        La transmisión de los coronavirus puede ocurrir de animales a personas (transmisión zoonótica). Se sabe que el SRAS-CoV se transmitió de la civeta al ser humano y que el MERS-CoV se originó en dromedarios. Aunque existen otros coronavirus que circulan entre animales, no han infectado a los humanos.        
    </div>    
    <br>
    <div style="text-align: justify">
        Los síntomas comunes incluyen fiebre y problemas respiratorios como tos y dificultad para respirar. En casos graves, pueden causar neumonía, síndrome respiratorio agudo severo, insuficiencia renal e incluso la muerte.            
    </div> 
   <br>
    <div style="text-align: justify">
        Las medidas de prevención habituales incluyen una buena higiene de manos y respiratoria, como cubrirse la boca al toser o estornudar, y asegurarse de cocinar completamente la carne y los huevos. También se debe evitar el contacto cercano con personas que presenten síntomas respiratorios como tos o estornudos.            
    </div>         
""", unsafe_allow_html=True)
#Espacio en blanco
st.write("")  # o st.text("")


# Texto
st.markdown("""
¿Qué es la distribución binomial?
            
La distribución binomial es un modelo matemático que describe la probabilidad de obtener un número específico de éxitos en una serie de ensayos independientes, donde cada ensayo tiene solo dos posibles resultados: éxito o fracaso. Cada ensayo se considera independiente, lo que significa que el resultado de uno no afecta al resultado de otro.

Las características principales de la distribución binomial son:

1. **Número fijo de ensayos**: Se realiza un número fijo de ensayos, denotado como \( n \).

2. **Resultados mutuamente excluyentes**: Cada ensayo tiene solo dos resultados posibles, que son mutuamente excluyentes, como éxito o fracaso.

3. **Probabilidad de éxito constante**: La probabilidad de éxito en cada ensayo, denotada como \( p \), permanece constante en todos los ensayos.

4. **Independencia**: Los ensayos son independientes entre sí.

La fórmula para calcular la probabilidad de obtener exactamente \( k \) éxitos en \( n \) ensayos bajo una distribución binomial es:
""")

#Notación matemática usando latex
st.latex(r"P(x,n)=\binom{n}{x}p^k(1-p)^{n-k}")

# Texto
st.markdown("""
Donde:

- \( P(X = k) \) es la probabilidad de obtener exactamente \( k \) éxitos.
- $\( \binom{n}{k} \)$ es el coeficiente binomial, que representa el número de formas de elegir \( k \) éxitos de \( n \) ensayos.
- \( p \) es la probabilidad de éxito en un solo ensayo.
- \( (1-p) \) es la probabilidad de fracaso en un solo ensayo.
- \( n \) es el número total de ensayos.
- \( k \) es el número de éxitos que se están considerando.

Aplicaciones de la distribución binomial:

1. **Pruebas de éxito o fracaso**: Se utiliza para modelar situaciones donde solo hay dos resultados posibles en cada ensayo, como lanzar una moneda, tirar un dado, etc.

2. **Procesos de Bernoulli**: Modela eventos que tienen solo dos resultados posibles y se repiten un número fijo de veces.

3. **Control de calidad**: Se utiliza para determinar la probabilidad de que un cierto número de productos de una línea de producción cumplan con ciertas especificaciones.

4. **Estadísticas y encuestas**: Se puede utilizar para modelar la probabilidad de obtener cierto número de respuestas afirmativas en una encuesta de opción múltiple.

5. **Biología y medicina**: Se aplica en estudios clínicos para evaluar la eficacia de un tratamiento o medicamento, así como en la genética para estudiar la herencia de ciertos rasgos.

""")

# Espacio en blanco
st.write("")  # o st.text("")

# Texto principal con notación LaTeX
st.write("""
La distribución de Poisson es un modelo matemático que describe la probabilidad de que ocurra un número específico de eventos en un intervalo de tiempo o espacio, dado un ritmo promedio de ocurrencia y bajo la suposición de que los eventos ocurren de forma independiente y a una tasa constante.

Las características principales de la distribución de Poisson son:

1. **Eventos discretos e independientes**: Los eventos que se están contando son discretos (como llegadas, llamadas telefónicas, accidentes, etc.) y son independientes entre sí, lo que significa que la ocurrencia de uno no afecta la ocurrencia de otro.

2. **Tasa promedio de ocurrencia constante**: La tasa promedio de ocurrencia de eventos, denotada como \( \lambda \) (lambda), es constante durante el intervalo de tiempo o espacio considerado.

La fórmula para calcular la probabilidad de que ocurran exactamente \( k \) eventos en un intervalo bajo una distribución de Poisson es:
""")

#Notación matemática usando latex
st.latex(r"P(X = k) = \frac{e^{-\lambda} \cdot \lambda^k}{k!} ")

# Texto
st.write("""
Donde:

- \( P(X = k) \) es la probabilidad de que ocurran \( k \) eventos.
- \( e \) es la base del logaritmo natural (aproximadamente 2.71828).
- \( \lambda \) es la tasa promedio de ocurrencia de eventos en el intervalo.
- \( k \) es el número de eventos que se están considerando.
- \( k! \) es el factorial de \( k \).

Aplicaciones de la distribución de Poisson:

1. **Modelado de llegadas**: Se utiliza para modelar el número de llegadas de clientes a un banco, llamadas a un centro de atención telefónica, llegadas de vehículos a un peaje, etc.

2. **Procesos de conteo**: Se aplica en situaciones donde se cuenta el número de eventos en un intervalo de tiempo o espacio, como el número de accidentes de tráfico en una carretera en un día.

3. **Procesos de producción**: Se utiliza en la planificación de la producción para estimar la cantidad de productos defectuosos que se producirán en un cierto período de tiempo.

4. **Estimación de probabilidades raras**: La distribución de Poisson se utiliza para modelar eventos raros pero importantes, como fallas de equipos críticos, incidentes de seguridad, etc.

5. **Biología y medicina**: Se aplica en biología para modelar la tasa de mutaciones genéticas y en medicina para analizar la frecuencia de eventos médicos raros, como casos de enfermedades raras.
""")


# Crear las pestañas
titulos_pestañas = ['Resumen de la Práctica', 'Procedimiento Experimental', 'Mapa de Calor']
pestañas = st.tabs(titulos_pestañas)
 
# Agregar contenido a cada pestaña
with pestañas[0]:
    st.header('Resume de la práctica')
    # Texto principal del resumen
    st.write("""
    En el reporte, se aborda el desafío de predecir la evolución de los contagios por COVID-19 en Guatemala utilizando datos de los registros del Ministerio de Salud. Como epidemiólogos, nos enfrentamos a la tarea de realizar una predicción basada en datos disponibles hasta el 15 de marzo de 2021.

    Para lograr esta predicción, se optó por ajustar los datos a una distribución binomial. La selección de los datos y el enfoque metodológico se realizaron cuidadosamente, considerando varios aspectos, como la fiabilidad de los datos, la representatividad de las muestras y la idoneidad del modelo estadístico.

    Se establecieron dos fechas clave para el análisis: el 1 de junio de 2020 y el 15 de marzo de 2021. Estas fechas delimitan el período de estudio y permiten utilizar datos recopilados hasta ese momento para realizar la predicción.

    En la sección de discusión del reporte, se detallan las decisiones tomadas durante el proceso de análisis y modelado. Se justifica la elección de los datos utilizados, así como los métodos empleados para el ajuste a la distribución binomial. Además, se presentan las limitaciones y posibles sesgos del modelo, así como recomendaciones para futuras investigaciones.

    El objetivo final del reporte es proporcionar una visión clara y fundamentada sobre la predicción de la evolución de los contagios por COVID-19 en Guatemala, con el fin de contribuir al diseño de estrategias de prevención y control de la enfermedad.
    """)
    

    #st.bar_chart(datos)
 
with pestañas[1]:
    st.header('Procedimiento Experimental para el Análisis de Datos de COVID-19')

# Introducción
    st.write("""
    El objetivo de esta práctica fué analizar los datos de COVID-19 del Ministerio de Salud para comprender mejor la evolución de la enfermedad en Guatemala y realizar predicciones sobre su propagación futura.

    Para llevar a cabo este análisis, se siguieron los siguientes pasos:
    """)

# Paso 1: Obtención de datos
    st.write("Paso 1: Obtención de Datos")
    st.write("""
    Se accedió a los registros de casos de COVID-19 proporcionados por el Ministerio de Salud. Estos datos estaban disponibles en un archivo CSV o mediante una API. Se utilizó Python para cargar y procesar los datos.
    """)

# Paso 2: Exploración de datos
    st.write("Paso 2: Exploración de Datos")
    st.write("""
    Se realizó una exploración inicial de los datos para comprender su estructura y contenido. Se analizaron las variables disponibles, como la fecha de reporte, el número de casos confirmados, las tasas de mortalidad, etc.
    """)

# Paso 3: Preprocesamiento de datos
    st.write("Paso 3: Preprocesamiento de Datos")
    st.write("""
    Se llevó a cabo el preprocesamiento de los datos para limpiarlos y prepararlos para el análisis. Esto incluyó la eliminación de valores nulos, la corrección de errores, la normalización de datos, etc.
    """)

# Paso 4: Análisis estadístico
    st.write("Paso 4: Análisis Estadístico")
    st.write("""
    Se realizó un análisis estadístico de los datos para identificar tendencias, patrones y relaciones significativas. Se calcularon estadísticas descriptivas, se visualizaron los datos mediante gráficos y se aplicaron pruebas estadísticas según fue necesario.
    """)

# Paso 5: Modelado y predicción
    st.write("Paso 5: Modelado y Predicción")
    st.write("""
    Se utilizaron técnicas de modelado estadístico, como ajustes a distribuciones binomiales o de Poisson, para realizar predicciones sobre la evolución futura de la enfermedad. Se evaluó la calidad del modelo y se realizaron ajustes según fue necesario.
    """)

# Paso 6: Conclusiones y recomendaciones
    st.write("Paso 6: Conclusiones y Recomendaciones")
    st.write("""
    Se resumieron los hallazgos del análisis y se formularon conclusiones basadas en los resultados obtenidos.
    """)


 
with pestañas[2]:
    st.header('Mapa de Calor')
    #st.heatmap(datos.corr())