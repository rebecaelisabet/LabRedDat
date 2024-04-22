from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import math 
import streamlit as st

st.title('Examen Parcial 1 - Parte Práctica')
st.caption('Rebeca Elisabet Rodríguez Barrera - 201908399')

st.header('Distribución Binomial')

# Valores para p y n

p_valor = st.slider('Escoge el valor para p', 0.0, 1.0, 1.0, step=0.01)
st.write("Tu valor de p es:",p_valor,)

n_valor = st.slider('Escoge el valor para n', 1, 100, 50,)
st.write("Tu valor de n es:",n_valor,)


#Definimos la funcion


def binomial(x,n,p,q):
    #todo lo que este aqui adentro es parte de lo que se ejecuta en la funcion
    
    comb = math.comb(n,x)
    p_x = p**x
    q_nx = q**(n-x)

    return comb*p_x*q_nx



eval_ = binomial(100,600,1/6,5/6)



print(eval_)

# Asignamos los valores del usuario a las variables

n = n_valor
p = p_valor
q = (1-p_valor)

#lista

lista = np.arange(n+1)
print(lista)

#Tabla

data_table = pd.DataFrame({'x':lista})
data_table['Nueva'] = data_table['x'] - 50

data_table['Pb'] = data_table.apply(lambda row: binomial(row['x'],n,p,q), axis=1)


print(data_table)


#Declarando una Figura

binomial_plot, axis = plt.subplots()

axis.bar(data_table['x'],data_table['Pb'])

axis.plot(data_table['x'],data_table['Pb'],color='C1')

binomial_plot.show()

#Gráfica

st.subheader('Gráfica distribución binomial')

st.pyplot(binomial_plot)