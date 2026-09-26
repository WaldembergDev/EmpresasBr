from pathlib import Path
import pandas as pd
from config.settings import BASE_DIR


def criar_df_estabelecimento(caminho_arquivo: Path) -> pd.DataFrame:
    # carregando o dataframe estabelecimento
    # definindo as colunas que serão carregadas
    colunas_selecionadas = [0, 1, 2, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 27]
    # definindo o nome das colunas
    colunas_estabelecimentos = ['CNPJ BÁSICO',
                                'CNPJ ORDEM',
                                'CNPJ DV',
                                'NOME FANTASIA',
                                'SITUAÇÃO CADASTRAL',
                                'DATA INÍCIO ATIVIDADE',
                                'CNAE PRINCIPAL',
                                'CNAE SECUNDÁRIA',
                                'TIPO DE LOGRADOURO',
                                'LOGRADOURO',
                                'NÚMERO',
                                'COMPLEMENTO',
                                'BAIRRO',
                                'CEP',
                                'UF',
                                'COD_MUNICÍPIO',
                                'DDD 1',
                                'TELEFONE 1',
                                'CORREIO ELETRÔNICO']
    
    df_estabelecimento = pd.read_csv(
        caminho_arquivo,
        sep=';',
        encoding='latin-1',
        usecols=colunas_selecionadas,
        names=colunas_estabelecimentos,
        parse_dates=['DATA INÍCIO ATIVIDADE'],
        dtype={
            'CEP': 'string',
            'DDD 1': 'string',
            'TELEFONE 1': 'string',
            'CNPJ ORDEM': 'string',
            'CNPJ DV': 'string',
            'CNPJ BÁSICO': 'string',
            'SITUAÇÃO CADASTRAL': int},
        )
    
    # selecionando as empresas ativas
    df_empresas_ativos = df_estabelecimento[df_estabelecimento['SITUAÇÃO CADASTRAL'] == 2]
    # selecionando apenas as empresas do RJ
    df_empresas_ativos_rj = df_empresas_ativos[df_empresas_ativos['UF'] == 'RJ']
    # excluindo as colunas UF e SITUAÇÃO CADASTRAL
    df_empresas_ativos_rj.drop(columns=['SITUAÇÃO CADASTRAL', 'UF'], inplace=True)
    # filtrando para ter apenas empresas com telefone ou e-mail
    df_empresas_ativos_rj_filtrado = df_empresas_ativos_rj[
        (df_empresas_ativos_rj['TELEFONE 1'].notnull() | df_empresas_ativos_rj['CORREIO ELETRÔNICO'].notnull())
        ]

    # ajustando o formato da data
    df_empresas_ativos_rj_filtrado['DATA INÍCIO ATIVIDADE'] = (
        df_empresas_ativos_rj_filtrado['DATA INÍCIO ATIVIDADE'].dt.strftime('%d/%m/%Y')
        )
    
    return df_empresas_ativos_rj_filtrado
    

def criar_df_municipio(caminho_arquivo: Path) -> pd.DataFrame:
    # criando um dataframe contendo os códigos e seus respectivos nomes
    dataframe_municipios = pd.read_csv(
        caminho_arquivo, sep=';',
        encoding='latin-1',
        names=['COD_MUNICÍPIO', 'MUNICÍPIO'],
        )
    return dataframe_municipios


def criar_df_empresa(caminho_arquivo: Path) -> pd.DataFrame:
    # definindo o nome das colunas
    colunas_empresas =  ['CNPJ BÁSICO', 'RAZÃO SOCIAL','CAPITAL SOCIAL', 'PORTE']
    df_empresas = pd.read_csv(
        caminho_arquivo,
        sep=';',
        encoding='latin-1',
        usecols=[0, 1, 4, 5],
        names=colunas_empresas,
        dtype={'CNPJ BÁSICO': 'string', 'PORTE': 'Int64'},
        )
    # Definindo o padrão dos nomes dos MEIs
    padrao_regex = r'\d{2}\.\d{3}\.\d{3}|\d{11}'
    # Filtrando apenas as empresas que não são MEIs
    df_filtrado = df_empresas[~df_empresas['RAZÃO SOCIAL'].str.contains(padrao_regex, regex=True, na=False)]

    return df_filtrado


def obter_lista_dataframe(caminho: Path, nome_tipo: str) -> pd.DataFrame:
    # percorrendo pela pasta e salvando todos os dataframes em uma lista
    lista_dataframe = []
    for arquivo in caminho.iterdir():
        # obter o nome do arquivo dentro da pasta
        if arquivo.is_file():
            # aplicar a função
            match nome_tipo:
                case 'Estabelecimento':
                    dataframe = criar_df_estabelecimento(arquivo)
                case 'Empresa':
                    dataframe = criar_df_empresa(arquivo)
                case 'Municipio':
                    dataframe = criar_df_municipio(arquivo)
                case _:
                    print('Nome inválido')
                    continue
            lista_dataframe.append(dataframe)

    # Concatendo todos os dataframes encontrados
    dataframe_concatenado = pd.concat(lista_dataframe, ignore_index=True)
    return dataframe_concatenado


def criar_df_final(df_estabelecimentos: pd.DataFrame, df_empresas: pd.DataFrame, df_municipios: pd.DataFrame):
    df_merge = pd.merge(df_estabelecimentos, df_empresas, on='CNPJ BÁSICO', how='inner')
    df_merge_final = pd.merge(df_merge, df_municipios, on='COD_MUNICÍPIO')
    df_merge_final['CNPJ'] = df_merge_final['CNPJ BÁSICO'] + df_merge_final['CNPJ ORDEM'] + df_merge_final['CNPJ DV']
    df_merge_final.drop(columns=['CNPJ BÁSICO', 'CNPJ ORDEM', 'CNPJ DV', 'COD_MUNICÍPIO'], inplace=True)
    return df_merge_final


def script_df():
    try:
        caminho_empresas = Path(BASE_DIR / 'auxiliar/Empresa')
        df_empresas = obter_lista_dataframe(caminho_empresas, 'Empresa')


        caminho_municipios = Path(BASE_DIR / 'auxiliar/Municipio')
        df_municipios = obter_lista_dataframe(caminho_municipios, 'Municipio')


        caminho_estabelecimentos = Path(BASE_DIR / 'auxiliar/Estabelecimento')
        df_estabelecimentos = obter_lista_dataframe(caminho_estabelecimentos, 'Estabelecimento')


        # juntando os dataframes
        df_final = criar_df_final(df_estabelecimentos, df_empresas, df_municipios)


        df_final.to_parquet(Path(BASE_DIR / 'data/empresas_ativas_rj2.parquet'), index=False, compression='snappy')

        # ação realizada com sucesso
        return 1
    except Exception as e:
        # erro durante a ação
        return 0