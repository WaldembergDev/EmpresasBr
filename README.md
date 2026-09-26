# Empresas Ativas RJ

Aplicação em **Streamlit** para processar os arquivos públicos disponibilizados pela Receita Federal e extrair as empresas ativas do estado do Rio de Janeiro.

Os dados públicos da Receita Federal são extensos, chegam em formato bruto e exigem tratamento manual antes de serem úteis. Este projeto automatiza esse processo: carrega os arquivos oficiais, filtra apenas as empresas ativas e organiza as informações de forma clara e acessível, com visualizações interativas.

## Funcionalidades

- Carregamento e processamento dos arquivos públicos da Receita Federal
- Tratamento e limpeza de dados com Pandas
- Junção (merge) dos diferentes arquivos (Empresa, Estabelecimento e Município)
- Dashboard interativo com gráficos por município
- Listagem navegável das empresas processadas

## Tecnologias utilizadas

- [Python](https://www.python.org/) 3.12+
- [Streamlit](https://streamlit.io/) — interface web
- [Pandas](https://pandas.pydata.org/) — tratamento e análise de dados
- [PyArrow](https://arrow.apache.org/docs/python/) — leitura/escrita eficiente de dados
- [Matplotlib](https://matplotlib.org/) — gráficos
- [OpenPyXL](https://openpyxl.readthedocs.io/) — exportação/leitura de planilhas
- [uv](https://docs.astral.sh/uv/) — gerenciamento de dependências e ambiente
- [Pytest](https://docs.pytest.org/) — testes automatizados

## Estrutura do projeto

```
EmpresasBr/
├── app.py                    # Ponto de entrada da aplicação Streamlit
├── config/                   # Configurações do projeto (ex: BASE_DIR)
├── pages/                    # Páginas do app (Início, Dashboard, Listagem)
├── utils/                    # Funções de extração e processamento dos dados
├── tests/                    # Testes automatizados (pytest)
├── auxiliar/                 # Pasta onde os arquivos brutos da Receita Federal são colocados
├── .streamlit/                # Configurações do Streamlit
├── .github/workflows/         # Pipelines de CI (GitHub Actions)
└── pyproject.toml            # Dependências e configuração do projeto
```

## Como executar o projeto

### Pré-requisitos

- Python 3.12 ou superior
- [uv](https://docs.astral.sh/uv/getting-started/installation/) instalado

### Passo a passo

1. Clone o repositório:
   ```bash
   git clone https://github.com/WaldembergDev/EmpresasBr.git
   cd EmpresasBr
   ```

2. Instale as dependências com o uv:
   ```bash
   uv sync
   ```

3. Rode a aplicação:
   ```bash
   uv run streamlit run app.py
   ```

4. Acesse no navegador o endereço indicado no terminal (geralmente `http://localhost:8501`).

## Como obter e carregar os dados

A aplicação não inclui os dados — eles precisam ser baixados manualmente do portal da Receita Federal:

1. Acesse o [portal de dados abertos da Receita Federal](https://arquivos.receitafederal.gov.br/index.php/s/YggdBLfdninEJX9)
2. Baixe a versão mais recente dos dados
3. Extraia o arquivo baixado
4. Mova os arquivos extraídos para a pasta `auxiliar/` do projeto, seguindo a estrutura:
   - Arquivos terminados em `.EMPRECSV` → `auxiliar/Empresa`
   - Arquivos terminados em `.ESTABELE` → `auxiliar/Estabelecimento`
   - Arquivos terminados em `.MUNICCSVC` → `auxiliar/Municipio`
5. Na página **Início** do app, clique em **"Gerar dados"**

> ⚠️ **Atenção:** a geração dos dados é um processo pesado para a máquina. Execute esse passo apenas quando realmente houver uma atualização dos arquivos da Receita Federal.

## Rodando os testes

```bash
uv run pytest
```

## Autor

Desenvolvido por [Waldemberg Pereira](https://github.com/WaldembergDev).