# Importando as bibliotecas necessárias para a exibicao de dados
import streamlit as st 
import pandas as pd

# Carregando a planilha
df = pd.read_csv('arquivos/criminalidade_sp_2.csv')

# Formatando conteúdo e exibindo usando o streamlit

# Exibindo um título para a visualizacao
st.title('criminalidade em São Paulo')

# Exibe um dado informativo, no caso, exibindo a quantidade de registros do dataframe
st.sidebar.info('Foram carregadas {} linhas'.format(df.shape[0]) )

# Exibe um checkbox que, se for marcado, exibe um resumo dos dados do dataframe
if st.sidebar.checkbox('Ver dados de entrada'):
    st.header('Dados de entrada')
    st.write(df)

# Formata os dados de data e hora
df.time = pd.to_datetime(df.time)

# Exibe um slider para selecao de filtragem por ano
ano_selecionado = st.sidebar.slider("Selecione um ano", 2010, 2018, 2015)

# Gera um novo dataframe de acordo com o ano selecionado pelo slider de filtragem
df_selected = df[df.time.dt.year == ano_selecionado]

# Insere um subtitulo no frame
st.subheader('Mapa da criminalidade')

# Mapa gerado utilizando dados de latitude e longitude, devendo ter cabecalhos com os mesmos nomes no dataframe
st.map(df_selected)

# Para executar o script e exibir os resultados, use o comando: streamlit run index.py
