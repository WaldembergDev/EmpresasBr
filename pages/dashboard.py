import streamlit as st
import pandas as pd
from utils.services import DadosEmpresa

dados = DadosEmpresa()

st.title('Dashboard de Empresas do Brasil', text_alignment='center')

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label='Total de empresas ativas no RJ', value=dados.total_empresas(), border=True)

with col2:
    st.metric(label='Munícipio com maior número de empresas', value=dados.municipio_mais_frequente(), border=True)

with col3:
    st.metric(label="CNAE mais comum", value=dados.cnae_mais_frequente(), border=True)


col_grafico1, col_grafico2 = st.columns(2)

with col_grafico1:
    st.bar_chart(
        dados.empresas_por_municipio(),
        x='MUNICÍPIO',
        y='QUANTIDADE',
        sort=False,
        x_label='',
        horizontal=True,
        height='stretch'
        )

with col_grafico2:
    st.bar_chart(
        dados.cnaes_mais_comuns(),
        sort=False
    )