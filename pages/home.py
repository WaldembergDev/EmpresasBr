import streamlit as st
from utils.services_extracao import script_df


st.title('Empresas do Brasil')

st.subheader('Sobre', divider=True)
st.text(
"""Este projeto nasceu devido a dificuldade em obter a relação das empresas do Brasil.

Os dados públicos disponibilizados pela Receita Federal são extensos, desatualizados no
formato original e exigem tratamento manual antes de serem úteis. Este sistema automatiza
esse processo: carrega os arquivos oficiais, filtra apenas as empresas ativas e organiza
as informações de forma clara e acessível.
"""
)

st.subheader('Como obter os dados?', divider=True)
st.markdown(
    """
    - Acesse [dados gov](https://arquivos.receitafederal.gov.br/index.php/s/YggdBLfdninEJX9)
    - Selecione e baixe a versão dos dados mais recente
    - Extraia o arquivo
    - Acesse a pasta extraída
    - Mova os arquivos seguindo a estrutura abaixo:
        - Terminados em .EMPRECSV devem ser movidos para a pasta deste projeto auxiliar/Empresa
        - Terminados em .ESTABELE devem ser movidos para a pasta deste projeto auxiliar/Estabelecimento
        - Terminados em .MUNICCSVC devem ser movidos para a pasta deste projeto auxiliar/Municipio
    - Como último passo, clique no botão abaixo. Faça isso apenas quando realmente houver atualização
    pois este é um processo extremamente pesado para a máquina"""
)

if st.button('Gerar dados'):
    with st.spinner('Gerando os dados, por favor, aguarde...'):
        sucesso = script_df()
        if sucesso:
            st.success('Dados gerados com sucesso')
        else:
            st.error('Erro ao gerar os dados')