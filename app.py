import streamlit as st
from pathlib import Path
from config.settings import BASE_DIR

# Especificação da página
st.set_page_config(page_title="Data manager", page_icon=":material/edit:", layout='wide')

# Páginas
dashboard_page = st.Page( BASE_DIR / "pages/dashboard.py", title="Dashboard")
home_page = st.Page(BASE_DIR / "pages/home.py", title="Início")

pg = st.navigation([home_page, dashboard_page])

pg.run()
