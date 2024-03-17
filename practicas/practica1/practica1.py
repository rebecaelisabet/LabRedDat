import streamlit as st

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
st.title('Explorando la Distribución Binomial en Lanzamientos de Monedas')

# Párrafos justificados
st.markdown("""
    <div style="text-align: justify">
        La distribución binomial es un modelo de probabilidad discreto que indica la probabilidad de obtener uno de dos resultados posibles al realizar una serie de pruebas independientes.
    </div>
    <br>
    <div style="text-align: justify">
        Cada resultado posible tiene una probabilidad que va de 0 a 1, y en estas pruebas, solo pueden ocurrir dos resultados, como en el lanzamiento de una moneda (cara o cruz) o en la ruleta francesa (rojo o negro).
    </div>
    <br>
    <div style="text-align: justify">
        Cada prueba es independiente de las demás, lo que significa que el resultado de una no afecta la probabilidad de las siguientes. La probabilidad de cada resultado sigue siendo constante en cada prueba.
    </div>    
    <br>
     <div style="text-align: justify">
        En la distribución binomial tenemos tres variables:
    </div> 
""", unsafe_allow_html=True)

# Lista
st.markdown("""
- n: Es el número de veces que repetimos el experimento
- p: es uno de los dos resultados al que llamaremos éxito.
- q: es el otro resultado posible al que llamaremos fracaso.
""")

# Más parrafos justificados
st.markdown("""
    <div style="text-align: justify">
        Como p y q son los dos únicos resultados posibles, entre los dos su porcentaje debe sumar uno por lo que p=1-q. De esto obtenemos la siguiente fórmula.
    </div>
""", unsafe_allow_html=True)
#Notación matemática usando latex
st.latex(r"P(x,n)=\binom{n}{x}p^x(1-p)^{n-x}")
# Crear las pestañas



titulos_pestañas = ['Resumen del Proyecto', 'Procedimiento Experimental', 'Visualización de Resultados', 'Referencias']
pestañas = st.tabs(titulos_pestañas)
 
# Agregar contenido a cada pestaña
with pestañas[0]:
    st.header('Resumen del Proyecto')

# Párrafo en la interfaz usando st.write()
    st.write("El informe incluyó dos partes:")
    st.write("")
    st.write("1. **Análisis de datos individuales:**")
    st.write("   Se generó un histograma que exhibió la distribución del conteo de caras de los primeros $m$ lanzamientos de 10 monedas, donde el lector tuvo la capacidad de variar $m$ en el rango de $0 \leq m \leq 100$. Además, se realizó un ajuste de una función binomial a estos datos y se graficó sobre el histograma. Se proporcionaron los valores resultantes del ajuste, así como el conteo medio de caras y su desviación estándar, medidos experimentalmente y obtenidos del ajuste.")
    st.write("")
    st.write("2. **Análisis de datos colectivos:**")
    st.write("   Se produjo un segundo histograma que representó la distribución del conteo de caras para los 500 datos recopilados por toda la clase. Asimismo, se llevó a cabo un ajuste de una función binomial a estos datos y se mostró sobre el histograma. Se incluyeron los valores derivados del ajuste, así como el conteo medio de caras y su desviación estándar.")
    st.write("")
    st.write("Cada sección del informe proporcionó una comprensión tanto de la distribución individual de los datos como de la distribución colectiva, permitiendo una evaluación completa de la variabilidad de los resultados y su concordancia con el modelo teórico de la distribución binomial.")

 
with pestañas[1]:
    
# Procedimiento Experimental
    st.write("## Procedimiento Experimental")

# 1. Preparación de materiales
    st.write("**1. Preparación de materiales:**")
    st.write("- Se reunieron 10 monedas idénticas.")
    st.write("- Se registraron los datos en una hoja de cálculo.")

# 2. Configuración del experimento
    st.write("**2. Configuración del experimento:**")
    st.write("- Se estableció un área de trabajo limpia y plana para realizar los lanzamientos de las monedas.")
    st.write("- Se decidió sobre el número máximo de lanzamientos que se realizarían para cada moneda, denotado como $m$.")
    st.write("- Se configuró el entorno de programación preferido con las bibliotecas necesarias, como `numpy`, `matplotlib` y `pandas`.")

# 3. Realización de los lanzamientos
    st.write("**3. Realización de los lanzamientos:**")
    st.write("- Se lanzarón las 10 monedas $m$ veces.")
    st.write("- Se registró el número de caras obtenidas en cada lanzamiento.")

# 4. Análisis de datos individuales
    st.write("**4. Análisis de datos individuales:**")
    st.write("- Para cada valor de $m$ en el rango de $0 \leq m \leq 100$:")
    st.write("  - Se calculó la distribución del conteo de caras de los primeros $m$ lanzamientos de las 10 monedas.")
    st.write("  - Se realizó un ajuste de una función binomial a los datos obtenidos.")
    st.write("  - Se graficó la distribución junto con la función binomial ajustada.")
    st.write("  - Se extrajeron los valores resultantes del ajuste, así como el conteo medio de caras y su desviación estándar.")

# 5. Análisis de datos colectivos
    st.write("**5. Análisis de datos colectivos:**")
    st.write("- Se reunieron los datos de todos los participantes de la clase (500 datos en total).")
    st.write("- Se calculó la distribución del conteo de caras para los 500 datos recopilados.")
    st.write("- Se realizó un ajuste de una función binomial a estos datos.")
    st.write("- Se graficó la distribución junto con la función binomial ajustada.")
    st.write("- Se extrajeron los valores resultantes del ajuste, así como el conteo medio de caras y su desviación estándar.")

 
with pestañas[2]:
    st.header('Histogramas')
    st.write('')
 
with pestañas[3]:
    st.header('Referencias')
    st.write('Software DELSOL. (2019, junio 20). Distribución binomial. Sdelsol.com. https://www.sdelsol.com/glosario/distribucion-binomial/')