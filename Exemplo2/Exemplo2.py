import pandas as pd
import numpy as np

# Obter dados
try:
    print('Obtendo dados...')
    ENDEREÇO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    df_ocorrencias = pd.read_csv(ENDEREÇO_DADOS, sep=';', encoding='iso-8859-1')
    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]
    df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['roubo_veiculo']).reset_index()
     #print(df_roubo_veiculo.head())
     #print('\ndados obtidos com sucesso!')
except Exception as e:
   # print(f'Erro ao obter dados: {e}')
    exit()


# Gerando informações ..
try:
    print('\nCalculando informações sobre padrão de roubo de veículos...')
    # Array Numpy
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])
    media_roubo_veiculo = np.mean(array_roubo_veiculo)
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)
    distancia_media_mediana = abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo) *100
    print('\nMedidas de tedencia central:')
    print(f'Media de roubo é: {media_roubo_veiculo}')
    print(f'Mediana de roubo é: {mediana_roubo_veiculo}')
    print(distancia_media_mediana)

except Exception as e:
    print(f'Erro ao obter informações sobre padrão de roubo de veículo: {e}')
    exit()