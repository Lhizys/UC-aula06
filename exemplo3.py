from sqlalchemy import create_engine
import pandas as pd

host = 'localhost'
user = 'root'
passaword = 'root'
database = 'bd_vendas'

engine = create_engine(f'mysql+pymysql://{user}:{passaword}@{host}/{database}')

#carregar dados da tabela 'db_clientes' do Banco Exemplo3 MYQSL
query_clientes = "SELECT id_cliente, nome, email FROM tb_clientes"
df_clientes = pd.read_sql(query_clientes, engine)
print(df_clientes)

# Carregar dados tabela 'pedidos' do arquivo Excel
df_pedidos = pd.read_excel('tb_pedidos.xlsx')
#print(df_pedidos)

# Relacionar os dados usando merge
df_refacionado = pd.merge(df_pedidos, df_clientes, on='id_cliente', how='inner')

# Ordenar o DataFrame relacionando pela coluna 'id_cliente'
df_refacionado = df_refacionado.sort_values(by='nome')

# Exibir o resultado
print(df_refacionado)