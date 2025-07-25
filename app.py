# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Configuración inicial de la app
st.set_page_config(page_title="Análisis de Vehículos Usados", layout="wide")
st.title('Análisis de Vehículos Usados en EE. UU.')

# Cargar datos
df = pd.read_csv('vehicles_clean.csv')

# ======================
# Sección introductoria
# ======================
st.markdown("""
Bienvenido al panel interactivo de análisis de vehículos usados en Estados Unidos.
Explora tendencias clave del mercado: precios, kilometraje, condiciones, transmisiones, marcas y más.
Usa los filtros laterales para personalizar tu análisis.
""")

# ======================
# Filtros en sidebar
# ======================
st.sidebar.header('🔍 Filtros')

# Filtro por tipo de vehículo
selected_type = st.sidebar.selectbox('Tipo de vehículo', ['Todos'] + sorted(df['type'].dropna().unique().tolist()))
if selected_type != 'Todos':
    df = df[df['type'] == selected_type]

# Filtro por tipo de combustible
selected_fuel = st.sidebar.multiselect(
    'Tipo de combustible',
    options=sorted(df['fuel'].dropna().unique().tolist()),
    default=sorted(df['fuel'].dropna().unique().tolist())
)
if selected_fuel:
    df = df[df['fuel'].isin(selected_fuel)]

# ======================
# Sección: Distribución de precios
# ======================
st.header('Distribución de Precios')
st.markdown("Visualiza cómo se distribuyen los precios de los vehículos en el mercado.")
fig_price = px.histogram(df, x='price', nbins=50, title='Distribución de Precios')
st.plotly_chart(fig_price, use_container_width=True)

# ======================
# Sección: Precio vs Kilometraje
# ======================
st.header('Relación Precio vs Kilometraje')
st.markdown("Explora la relación entre el precio y el kilometraje de los vehículos.")
fig_odometer = px.scatter(
    df,
    x='odometer',
    y='price',
    color='condition',
    title='Precio vs Kilometraje',
    hover_data=['model_year', 'model']
)
st.plotly_chart(fig_odometer, use_container_width=True)

# ======================
# Sección: Condición del Vehículo
# ======================
st.header('Distribución por Condición del Vehículo')
condition_counts = df['condition'].value_counts().reset_index()
condition_counts.columns = ['Condición', 'Cantidad']
fig_condition = px.bar(condition_counts, x='Condición', y='Cantidad', title='Condición del Vehículo')
st.plotly_chart(fig_condition, use_container_width=True)

# ======================
# Sección: Precio promedio por marca
# ======================
st.header('Top 20 Marcas con Mayor Precio Promedio')
df['brand'] = df['model'].str.split().str[0].str.lower()
avg_price_by_brand = df.groupby('brand')['price'].mean().sort_values(ascending=False).head(20).reset_index()
fig_brand_price = px.bar(
    avg_price_by_brand,
    x='brand',
    y='price',
    title='Top 20 Marcas con Mayor Precio Promedio',
    labels={'brand': 'Marca', 'price': 'Precio Promedio'},
    text_auto='.2s'
)
st.plotly_chart(fig_brand_price, use_container_width=True)

# ======================
# Sección: Distribución por año de modelo
# ======================
st.header('Distribución por Año del Modelo')
fig_year = px.histogram(df, x='model_year', nbins=30, title='Cantidad de Vehículos por Año de Modelo')
st.plotly_chart(fig_year, use_container_width=True)

# ======================
# Sección: Distribución por transmisión
# ======================
st.header('Distribución por Transmisión')
transmission_counts = df['transmission'].value_counts().reset_index()
transmission_counts.columns = ['Transmisión', 'Cantidad']
fig_transmission = px.bar(transmission_counts, x='Transmisión', y='Cantidad', title='Transmisión del Vehículo')
st.plotly_chart(fig_transmission, use_container_width=True)

# ======================
# Sección: Tiempo de Publicación del Anuncio
# ======================
st.header('Tiempo de Publicación del Anuncio')
fig_days_listed = px.histogram(df, x='days_listed', nbins=50, title='Días Listado en el Portal')
st.plotly_chart(fig_days_listed, use_container_width=True)

# ======================
# NUEVA Sección: Distribución por Tipo de Vehículo y Combustible
# ======================
st.header('Distribución por Tipo de Vehículo y Combustible')

col1, col2 = st.columns(2)

with col1:
    type_counts = df['type'].value_counts().reset_index()
    type_counts.columns = ['Tipo', 'Cantidad']
    fig_type = px.bar(type_counts, x='Tipo', y='Cantidad', title='Distribución por Tipo de Vehículo')
    st.plotly_chart(fig_type, use_container_width=True)

with col2:
    fuel_counts = df['fuel'].value_counts().reset_index()
    fuel_counts.columns = ['Combustible', 'Cantidad']
    fig_fuel = px.bar(fuel_counts, x='Combustible', y='Cantidad', title='Distribución por Tipo de Combustible')
    st.plotly_chart(fig_fuel, use_container_width=True)

# ======================
# seccion final: conclusiones
# ======================
st.header('Conclusiones Finales')

st.markdown("""
El presente análisis tuvo como objetivo explorar el mercado de vehículos usados en Estados Unidos a partir de un conjunto de datos con más de 50.000 registros, permitiendo identificar patrones y tendencias relevantes para compradores, vendedores o analistas del sector automotor.

A través de gráficos interactivos y filtros personalizables, se evidenciaron **aspectos clave que influyen en el precio de los vehículos**. La distribución general de precios mostró una fuerte concentración de vehículos en rangos bajos, sugiriendo un mercado amplio para autos asequibles. La relación entre **precio y kilometraje** confirmó una tendencia esperada: a mayor kilometraje, menor valor, aunque con excepciones según la condición del vehículo.

Se analizó la **distribución por condición**, revelando que la mayoría de los autos se encuentran en condiciones aceptables o buenas, lo que puede reflejar cierto estándar de calidad en las publicaciones. Adicionalmente, se identificaron las **20 marcas con mayor precio promedio**, destacando nombres reconocidos por su valor de reventa, lo cual puede orientar decisiones de inversión o reventa.

Otras variables relevantes como el **año del modelo**, **tipo de transmisión**, **tiempo de publicación** y **tipo de combustible**, permitieron ampliar la perspectiva sobre las características más comunes y su impacto en el mercado. El análisis también abordó la distribución conjunta entre **tipo de vehículo y combustible**, útil para perfilar la oferta según tendencias tecnológicas o preferencias regionales.

Finalmente, aunque se consideró un mapa de calor para observar la correlación entre variables numéricas, se concluyó que su aporte no era crítico para este nivel de análisis, priorizando la claridad y aplicabilidad de los resultados visuales presentados.

Este panel representa una herramienta útil y accesible para examinar los factores determinantes del precio y características de los vehículos usados, y puede ser fácilmente ampliado con nuevos datos o enfoques más específicos según el interés del usuario.
""")

# ======================
# Pie de página
# ======================
st.markdown("---")
st.markdown("© 2025 - Proyecto educativo | TripleTen | Desarrollado por Diego Tascon")




