import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Calculador de Pronósticos", layout="wide", initial_sidebar_state="collapsed")

# Quita el margen blanco que Streamlit pone por defecto alrededor de la app
# (encabezado, relleno del contenedor y espacios entre elementos) para que
# la herramienta ocupe toda la pantalla.
st.markdown(
    """
    <style>
      header[data-testid="stHeader"],
      [data-testid="stToolbar"],
      [data-testid="stDecoration"],
      [data-testid="stSidebar"],
      [data-testid="collapsedControl"],
      #MainMenu,
      footer { display: none !important; }

      html, body, .stApp, [data-testid="stAppViewContainer"], section.main, .main {
        margin: 0 !important;
        padding: 0 !important;
        background: #FFFFFF !important;
      }
      .block-container,
      [data-testid="stMainBlockContainer"] {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
      }
      [data-testid="stVerticalBlock"] { gap: 0 !important; }
      [data-testid="stElementContainer"] { margin: 0 !important; }
      iframe { display: block; border: 0 !important; width: 100% !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Carga el archivo index.html (debe estar en la misma carpeta que este app.py)
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Lo muestra dentro de la app de Streamlit
components.html(html_code, height=2000, scrolling=True)
