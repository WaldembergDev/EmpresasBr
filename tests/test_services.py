from utils.services import DadosEmpresa
import pandas as pd

def test_carregar_dataframe():
    dados = DadosEmpresa()
    df = dados.obter_dataframe()
    assert len(df) > 1

    colunas = list(df.columns)
    assert 'MUNICÍPIO' in colunas or 'NOME FANTASIA' in colunas or 'CNAE PRINCIPAL' in colunas

def test_carregar_dados_retorna_dataframe():
    dados = DadosEmpresa()
    df = dados.obter_dataframe()
    assert isinstance(df, pd.DataFrame)
    