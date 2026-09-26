from utils.services import DadosEmpresa
import pandas as pd


def test_carregar_dataframe():
    dados = DadosEmpresa()
    df = dados.obter_dataframe()
    assert len(df) > 1

    colunas = list(df.columns)
    # testa se existem determinadas colunas
    assert 'MUNICÍPIO' in colunas or 'NOME FANTASIA' in colunas or 'CNAE PRINCIPAL' in colunas
    # testa quantidade de colunas
    assert len(colunas) == 18


def test_carregar_dados_retorna_dataframe():
    dados = DadosEmpresa()
    df = dados.obter_dataframe()
    assert isinstance(df, pd.DataFrame)


def test_total_empresas():
    dados = DadosEmpresa()
    assert dados.total_empresas() == 8


def test_municipio_mais_frequente():
    dados = DadosEmpresa()
    assert dados.municipio_mais_frequente().upper() == 'Rio de Janeiro'.upper()


def test_cnae_mais_frequente():
    dados = DadosEmpresa()
    assert dados.cnae_mais_frequente() == '4322302'


def test_empresas_por_municipio():
    dados = DadosEmpresa()
    df = dados.empresas_por_municipio()
    # primeira linha
    assert df.iat[0, 1] == 6
    # segunda linha
    assert df.iat[1, 1] == 1
    # terceira linha
    assert df.iat[2, 1] == 1


def test_cnaes_mais_comuns():
    dados = DadosEmpresa()
    serie = dados.cnaes_mais_comuns()
    assert serie.index[0] == 4322302