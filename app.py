import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Calculador de Pronósticos", layout="wide")

# Carga el archivo index.html (debe estar en la misma carpeta que este app.py)
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Lo muestra dentro de la app de Streamlit
components.html(html_code, height=2000, scrolling=True)
