git add README.md# Análisis de Vehículos Usados en EE. UU.

Este proyecto corresponde al Sprint 7 del programa de Data Analyst en TripleTen. El objetivo principal fue desarrollar una aplicación interactiva utilizando Streamlit para analizar un conjunto de datos de vehículos usados en Estados Unidos. La app permite visualizar de forma clara y sencilla diversos patrones que pueden influir en el precio de un vehículo.

## Objetivo del Proyecto

Crear una aplicación visual que facilite el análisis exploratorio de datos (EDA), permitiendo identificar características relevantes que influyen en el precio de los vehículos, como el kilometraje, año del modelo, tipo de transmisión, condición, entre otros. 

## Archivos del Proyecto

```
.
├── app.py                 # Aplicación principal en Streamlit
├── vehicles_us.csv        # Dataset original entregado por TripleTen
├── vehicles_clean.csv     # Dataset limpiado y procesado (utilizado por la app)
├── requirements.txt       # Librerías necesarias para correr la app
├── README.md              # Este archivo
└── notebooks
    └── EDA.ipynb          # Análisis exploratorio y limpieza de datos
```

> **Nota importante**: El archivo `vehicles_clean.csv` contiene los datos preprocesados y es esencial para que la aplicación funcione correctamente. Fue generado a partir del dataset original (`vehicles_us.csv`) mediante limpieza y transformación, llevadas a cabo en el notebook `EDA.ipynb`.

## Estructura de la App

La aplicación incluye las siguientes visualizaciones clave:

- Distribución de precios de los vehículos.
- Relación entre precio y kilometraje.
- Distribución por condición del vehículo.
- Top 20 marcas con mayor precio promedio.
- Cantidad de distribuidores por año del modelo.
- Distribución por tipo de transmisión.
- Tiempo de publicación del anuncio.

## Tecnologías Utilizadas

- Python 3.13.5
- Streamlit
- Pandas
- Plotly Express
- Seaborn
- Matplotlib

## Aplicación Desplegada

Puedes acceder a la aplicación en línea desde el siguiente enlace:

👉 [https://sprint-7-psv8.onrender.com](https://sprint-7-psv8.onrender.com)


## Cómo Ejecutar la App

1. Asegúrate de tener Python instalado y crea un entorno virtual si lo deseas.
2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta la aplicación:

   ```bash
   streamlit run app.py
   ```

## Notas Finales

El análisis se diseñó para proporcionar una visión general y no busca profundizar en modelos predictivos ni segmentaciones avanzadas. El propósito es ofrecer una herramienta interactiva que sirva como base para futuras exploraciones más detalladas.

