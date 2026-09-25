import streamlit as st
import pandas as pd
from pathlib import Path

# local do arquivo
BASE_DIR = Path(__file__).parent.parent

@st.cache_data(ttl=3600)
def _carregar_dados() -> pd.DataFrame:
    df = pd.read_parquet(BASE_DIR / 'data' / 'Empresas_ativas_rj.parquet')
    return df


class DadosEmpresa():
    def __init__(self):
        self.df = _carregar_dados()


    def obter_dataframe(self) -> pd.DataFrame:
        return self.df


    def total_empresas(self) -> int:
        return len(self.df)


    def municipio_mais_frequente(self) -> str:
        municipio = self.df['MUNICÍPIO'].mode()[0]
        return municipio


    def cnae_mais_frequente(self) -> str:
        cnae = self.df['CNAE PRINCIPAL'].mode()[0]
        return cnae


    def empresas_por_municipio(self) -> pd.DataFrame:
        dados_agrupados = (
            self.df.groupby('MUNICÍPIO')
            .size()
            .reset_index(name='QUANTIDADE')
            .sort_values(by='QUANTIDADE', ascending=False)
            .head(5)
            )
        return dados_agrupados


    def cnaes_mais_comuns(self) -> pd.Series:
        dados_agrupados = (
            self.df.groupby('CNAE PRINCIPAL')
            .size()
            .sort_values(ascending=True)
            .head(5)
            )
        return dados_agrupados