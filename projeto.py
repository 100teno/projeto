# Passo a passo da solução

# Lógica de programação

# Passo 0 - Entender o que preciso resolver

# Passo 1 - Percorrer todos os arquivos da pasta base de dados (Pasta Vendas)
#biblioteca os serve para trabalhar em conjunto com o sistema operacional
import os
import pandas as pd

lista_arquivo = os.listdir("C:\\Users\\Bielc\\Desktop\\ESTUDOS\\projetos\\Vendas")
print(lista_arquivo)

tabela_total = pd.DataFrame()

# Passo 2 - Importar as bases de dados de vendas

for arquivo in lista_arquivo:
    #importo se for um arquivo de vendas
    if "Vendas" in arquivo:

    # importar o arquivo
        tabela = pd.read_csv(f"C:\\Users\\Bielc\\Desktop\\ESTUDOS\\projetos\\Vendas\\{arquivo}")
        tabela_total = tabela_total._append(tabela)
# Passo 3 - Tratar / Compilar as bases de dados

# Passo 4 - Calcular o produto mais vendido (em quantidade)
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)


# Passo 5 - Calcular o produto que mais faturou (em faturamento)
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']

tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)



# Passo 6 - Calcular a loja/cidade que mais vendeu (em faturamento) - criar um gráfico/dashboard

tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']]
print(tabela_lojas)

import plotly.express as px

grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento',)
grafico.show()


