import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Generar dos DataFrames de series de tiempo aleatorios
data1 = {
    'Fecha': pd.date_range(start='1/1/2022', periods=100, freq='D'),
    'Valor': np.random.randn(100).cumsum()
}
df1 = pd.DataFrame(data1)

data2 = {
    'Fecha': pd.date_range(start='1/1/2022', periods=100, freq='D'),
    'Valor': np.random.randn(100).cumsum()
}
df2 = pd.DataFrame(data2)

# Función para filtrar datos según el rango de fechas seleccionado
def filtrar_datos(df, fecha_inicio, fecha_fin):
    df_filtrado = df[(df['Fecha'] >= fecha_inicio) & (df['Fecha'] <= fecha_fin)]
    return df_filtrado

# Crear la interfaz de Streamlit
st.title('Aplicación de Línea de Tiempo con Selector de Datos')

# Desplegable para seleccionar el DataFrame
opcion = st.selectbox('Selecciona la serie de tiempo', ['Serie 1', 'Serie 2'])

# Seleccionar el DataFrame según la opción elegida
df = df1 if opcion == 'Serie 1' else df2

# Crear las dos columnas
col1, col2 = st.columns(2)

# Columna 1: Gráfico de línea de tiempo
with col1:
    fig = px.line(df, x='Fecha', y='Valor', title='Línea de Tiempo')
    st.plotly_chart(fig)

# Columna 2: Selector de datos y botón de calcular
with col2:
    st.header('Selector de Datos')
    fecha_inicio = st.date_input('Fecha de Inicio', df['Fecha'].min())
    fecha_fin = st.date_input('Fecha de Fin', df['Fecha'].max())
    calcular_btn = st.button('Calcular')

    if calcular_btn:
        df_filtrado = filtrar_datos(df, fecha_inicio, fecha_fin)
        st.subheader('Datos Filtrados')
        st.write(df_filtrado)
        
        # Actualizar gráfico con datos filtrados
        fig_filtrado = px.line(df_filtrado, x='Fecha', y='Valor', title='Línea de Tiempo Filtrada')
        st.plotly_chart(fig_filtrado)
