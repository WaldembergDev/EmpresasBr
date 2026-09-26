import streamlit as st
from utils.services_dados import DadosEmpresa


# carregando o dataframe
dados = DadosEmpresa()

st.title('Listagem de Empresas')

st.dataframe(dados.obter_dataframe())