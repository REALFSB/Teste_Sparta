import sqlite3
import csv


def processar_csv_para_sqlite(db_file, csv_file):
    """
    Processa um arquivo CSV e insere os dados em uma tabela SQLite.

    Parâmetros:
    - db_file (str): Caminho para o arquivo do banco de dados SQLite.
    - csv_file (str): Caminho para o arquivo CSV a ser processado.
    """

    def criar_conexao(db_file):
        """Cria uma conexão com o banco de dados SQLite especificado."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Conexão com o banco de dados {db_file} estabelecida.")
        except sqlite3.Error as e:
            print(f"Erro ao conectar-se ao banco de dados: {e}")
        return conn

    def criar_tabela(conn):
        """Cria a tabela 'dados' no banco de dados SQLite."""
        sql_create_table = """
        CREATE TABLE IF NOT EXISTS dados (
            CNPJ_CIA TEXT,
            DENOM_SOCIAL TEXT,
            SIT TEXT
        );
        """
        try:
            cursor = conn.cursor()
            cursor.execute(sql_create_table)
            print("Tabela 'dados' criada ou já existe.")
        except sqlite3.Error as e:
            print(f"Erro ao criar a tabela: {e}")

    def inserir_dados(conn, csv_file):
        """Insere os dados do arquivo CSV na tabela 'dados'."""
        try:
            with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
                csv_reader = csv.DictReader(csvfile)
                for row in csv_reader:
                    cnpj = row['CNPJ_CIA']
                    denom = row['DENOM_SOCIAL']
                    sit = row['SIT']
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO dados (CNPJ_CIA, DENOM_SOCIAL, SIT) VALUES (?, ?, ?)",
                                   (cnpj, denom, sit))
            conn.commit()
            print(f"Dados do arquivo {csv_file} inseridos na tabela 'dados'.")
        except FileNotFoundError as e:
            print(f"Arquivo não encontrado: {e}")
        except csv.Error as e:
            print(f"Erro ao ler o arquivo CSV: {e}")
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados na tabela: {e}")

    # Criar uma conexão com o banco de dados
    conn = criar_conexao(db_file)

    if conn is not None:
        # Criar a tabela
        criar_tabela(conn)

        # Inserir os dados do CSV na tabela
        inserir_dados(conn, csv_file)

        # Fechar a conexão
        conn.close()
        print("Conexão com o banco de dados fechada.")
    else:
        print("Falha ao criar a conexão com o banco de dados.")
