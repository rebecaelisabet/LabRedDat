import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

def validate_inputs(n, p):
    if n > 100:
        st.write("Error: n should be less than or equal to 100.")
        return None, None
    if p < 0 or p > 1:
        st.write("Error: p should be between 0 and 1.")
        return None, None
    return n, p

st.title("Distribución Binomial")

n = st.number_input("Ingrese un valor para n:", min_value=1, max_value=100, value=10)
p = st.number_input("Ingrese un valor para p:", min_value=0.0, max_value=1.0, value=0.5)

n, p = validate_inputs(n, p)

if n is not None and p is not None:
    # Generate binomial distribution
    x = np.arange(0, n+1)
    y = binom.pmf(x, n, p)

    # Plot binomial distribution
    plt.plot(x, y, '-o')
    plt.xlabel('Numero de eventos')
    plt.ylabel('Probabilidad')
    plt.title(f'Distribución Binomial para n={n} y p={p:.2f}')
    plt.grid()
    st.pyplot()

