from sqlalchemy import create_engine
import pandas as pd

host = 'localhost'
user = 'root'
passaword = 'root'
database = 'bd_loja'

engine = create_engine(f'mysql+pymysql://{user}:{passaword}@{host}/{database}')

#leitura dos dados da tabela de produtos
df_estoque = pd.read_sql('tb_produtos', engine)
#printando somente os 5 primeiros
print(df_estoque.head())
print(30*'=')

#calcula o valor do estoque por linha
df_estoque['TotalEstoque'] = df_estoque['QuantidadeEstoque'] * df_estoque['Valor']
print(df_estoque[['NomeProduto', 'TotalEstoque']])
print(30*'=')

#calcular o valor total do estoque
print(f'Total geral em estoque: R${df_estoque["TotalEstoque"].sum()}')