from sqlalchemy import create_engine
import pandas as pd
import numpy as np

host = 'localhost'
user = 'root'
passaword = 'root'
database = 'bd_loja'

engine = create_engine(f'mysql+pymysql://{user}:{passaword}@{host}/{database}')

#leitura dos dados da tabela de produtos
df_estoque = pd.read_sql('tb_produtos', engine)
#printando somente os 5 primeiros
#print(df_estoque.head())

#calcula o valor do estoque por linha
df_estoque['TotalEstoque'] = df_estoque['QuantidadeEstoque'] * df_estoque['Valor']
#print(df_estoque[['NomeProduto', 'TotalEstoque']])
#print(30*'=')

#print(f'Media total em estoque: R${df_estoque["TotalEstoque"].median()}')

#media_total = np.mean(df_estoque['Valor'])
#mediana_total = np.median(df_estoque['Valor'])
#print(media_total)
#print(mediana_total)

array_total = np.array(df_estoque['TotalEstoque'])
#print(array_total)

media = np.mean(array_total)
mediana = np.median(array_total)
distancia_media_mediana = abs((media - mediana) / mediana) *100
#print(media)
#print(mediana)
#print(f'Media do valor total: R$ {media:.2f}')
#print(f'Media do valor total: R$ {mediana:.2f}')
#print(f'A distancia entre a média e a mediana: {distancia_media_mediana:.2f} )

distancia = (media - mediana) / mediana
#print(distancia)

DISTANCIA = abs((media - mediana) / mediana) * 100
#print(DISTANCIA)

# Agrupando os produtos com o mesmo nome e somando as
# quantidade e valores
#df_estoque['TotalEstoque'] = df_estoque['QuantidadeEstoque'] * df_estoque['Valor']

df_agrupado = df_estoque.groupby('NomeProduto').agg({
    'QuantidadeEstoque': 'sum',
    'TotalEstoque': 'sum'
}).reset_index()
#print(df_agrupado)

# Ordenando os produtos pelo total de estoque
df_ordenando = df_agrupado.sort_values(by='TotalEstoque', ascending=False)

# Exibindo os produtos agrupados com o total de estoque
#print(df_ordenando[['NomeProduto', 'TotalEstoque']])

# Calculando o total geral do estoque
print(f'\nTotal geral em estoque: R$ {df_ordenando["TotalEstoque"].sum()}')