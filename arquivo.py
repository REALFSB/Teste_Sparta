import os
import pandas as pd


def processar_arquivo(caminho_arquivo, colunas_necessarias, caminho_saida):
    """
    Processa um arquivo CSV, mantendo apenas as colunas necessárias e salvando o resultado em um novo arquivo.

    Parâmetros:
    - caminho_arquivo (str): Caminho do arquivo CSV de entrada.
    - colunas_necessarias (list): Lista das colunas que devem ser mantidas.
    - caminho_saida (str): Caminho do arquivo CSV de saída.
    """
    if os.path.exists(caminho_arquivo):
        try:
            # Carrega o arquivo CSV
            arquivo = pd.read_csv(caminho_arquivo, encoding='cp1252', delimiter=';')

            # Configura a exibição de todas as colunas (opcional)
            pd.set_option('display.max_columns', None)

            # Seleciona apenas as colunas necessárias
            arquivo = arquivo[colunas_necessarias]

            # Salva o DataFrame resultante em um novo arquivo CSV
            arquivo.to_csv(caminho_saida, index=False)
            print(f"Arquivo processado e salvo como '{caminho_saida}'.")

        except pd.errors.ParserError as e:
            print(f"Erro ao analisar o arquivo CSV: {e}")
        except FileNotFoundError as e:
            print(f"Arquivo não encontrado: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
    else:
        print('Caminho/arquivo inexistente!')
