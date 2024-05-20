import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Cargar los datos desde un archivo CSV con delimitador ;
data = pd.read_csv('/home/rebeca/Documentos/5sem/LabRedDat/python/practicas/Examenfinal2/frecuencia.csv', delimiter=';')

# Mostrar las primeras filas para verificar la carga correcta
print(data.head())

# Mostrar los nombres de las columnas
print("Columnas del DataFrame:")
print(data.columns)

# Verificar si hay valores nulos
print(data.isnull().sum())

# Limpiar datos nulos si es necesario
data = data.dropna()

# Análisis descriptivo
print(data.describe())

# Visualización de la distribución de la frecuencia cardíaca antes, durante y después del ejercicio
def plot_histogram(data, column, title, xlabel, filename):
    sns.histplot(data[column], kde=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('Densidad')
    plt.savefig(filename)
    plt.close()

plot_histogram(data, 'Frecuencia_Cardíaca_Antes', 'Distribución de la Frecuencia Cardíaca Antes del Ejercicio', 'Frecuencia Cardíaca Antes', 'histograma_antes.png')
plot_histogram(data, 'Frecuencia_Cardíaca_Durante', 'Distribución de la Frecuencia Cardíaca Durante el Ejercicio', 'Frecuencia Cardíaca Durante', 'histograma_durante.png')
plot_histogram(data, 'Frecuencia_Cardíaca_Después', 'Distribución de la Frecuencia Cardíaca Después del Ejercicio', 'Frecuencia Cardíaca Después', 'histograma_despues.png')

# Calcular estadísticas descriptivas y ajustar la distribución normal
def calculate_stats_and_plot(data, column, title, filename):
    mean = np.mean(data[column])
    std_dev = np.std(data[column])
    print(f"Media de {column}: {mean}, Desviación Estándar de {column}: {std_dev}")
    
    # Visualización con distribución normal
    sns.histplot(data[column], kde=True, stat="density", bins=20)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mean, std_dev)
    plt.plot(x, p, 'k', linewidth=2)
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel('Densidad')
    plt.savefig(filename)
    plt.close()
    
    # Prueba de normalidad
    stat, p_value = stats.shapiro(data[column])
    print(f"Prueba de normalidad para {column}: Estadístico={stat}, p-valor={p_value}")
    if p_value > 0.05:
        print(f"Los datos de {column} siguen una distribución normal.")
    else:
        print(f"Los datos de {column} no siguen una distribución normal.")
    
    return mean, std_dev

mean_antes, std_dev_antes = calculate_stats_and_plot(data, 'Frecuencia_Cardíaca_Antes', 'Distribución Normal para Frecuencia Cardíaca Antes del Ejercicio', 'normal_antes.png')
mean_durante, std_dev_durante = calculate_stats_and_plot(data, 'Frecuencia_Cardíaca_Durante', 'Distribución Normal para Frecuencia Cardíaca Durante el Ejercicio', 'normal_durante.png')
mean_despues, std_dev_despues = calculate_stats_and_plot(data, 'Frecuencia_Cardíaca_Después', 'Distribución Normal para Frecuencia Cardíaca Después del Ejercicio', 'normal_despues.png')

# Cálculo de intervalos de confianza
conf_int_antes = stats.norm.interval(0.95, loc=mean_antes, scale=std_dev_antes)
conf_int_durante = stats.norm.interval(0.95, loc=mean_durante, scale=std_dev_durante)
conf_int_despues = stats.norm.interval(0.95, loc=mean_despues, scale=std_dev_despues)

print(f"Intervalo de confianza del 95% para frecuencia cardíaca antes del ejercicio: {conf_int_antes}")
print(f"Intervalo de confianza del 95% para frecuencia cardíaca durante el ejercicio: {conf_int_durante}")
print(f"Intervalo de confianza del 95% para frecuencia cardíaca después del ejercicio: {conf_int_despues}")
