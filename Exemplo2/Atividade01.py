import pandas as pd
import numpy as np

try:
    print('Obtendo dados...')
    ENDEREÇO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    df_ocorrencias = pd.read_csv(ENDEREÇO_DADOS, sep=';', encoding='iso-8859-1')
    df_estelionatos = df_ocorrencias[['mes_ano', 'estelionato']]
    df_estelionatos = df_estelionatos.groupby(['mes_ano']).sum(['estelionato']).reset_index()
    #print(df_estelionatos.head())
    #print('\ndados obtidos com sucesso!')

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()



# Resultado
try:
    print('\nInformando sobre o crime estelionato.')
    array_estelionato = np.array(df_estelionatos['estelionato'])
    media_estelionato = np.mean(df_estelionatos['estelionato'])
    mediana_estelionato = np.median(df_estelionatos['estelionato'])
    distancia_media_mediana = abs((media_estelionato - mediana_estelionato) / mediana_estelionato) *100
    
    print('\nInformação para a central:')
    print(f'Media de roubo é: {media_estelionato}')
    print(f'Mediana de roubo é: {mediana_estelionato}')
    print(f'A diferença entre eles são: {distancia_media_mediana}')
                            
except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()


print('Analisando os parâmetros cheguei ao veredito que ha extremos da distribuição tende a não ser uma medida de tedencia central confiável!')