from arquivo import processar_arquivo
from sql import processar_csv_para_sqlite
from app import create_app

# Uso da função
caminho_arquivo = 'cad_cia_aberta.csv'
colunas_necessarias = ['CNPJ_CIA', 'DENOM_SOCIAL', 'SIT']
caminho_saida = 'arquivo.csv'

processar_arquivo(caminho_arquivo, colunas_necessarias, caminho_saida)
processar_csv_para_sqlite('testeemprego.db', 'arquivo.csv')

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
