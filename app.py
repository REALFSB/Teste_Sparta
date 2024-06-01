from flask import Flask, render_template, request
import sqlite3 as sql


def create_app():
    app = Flask(__name__)
    app.secret_key = "admin123"

    # Dados para o dropdown
    dropdown_items = ['ATIVO', 'CANCELADA', 'SUSPENSO(A) - DECISÃO ADM']

    def get_db_connection():
        """Cria e retorna uma conexão com o banco de dados."""
        con = sql.connect("./testeemprego.db")
        con.row_factory = sql.Row
        return con

    def query_database(query='', dropdown_query=''):
        """Consulta o banco de dados com base nos parâmetros fornecidos."""
        con = get_db_connection()
        cur = con.cursor()
        if query and dropdown_query:
            cur.execute("SELECT * FROM dados WHERE DENOM_SOCIAL LIKE ? AND SIT = ?",
                        ('%' + query + '%', dropdown_query))
        elif query:
            cur.execute("SELECT * FROM dados WHERE DENOM_SOCIAL LIKE ?",
                        ('%' + query + '%',))
        elif dropdown_query:
            cur.execute("SELECT * FROM dados WHERE SIT = ?",
                        (dropdown_query,))
        else:
            cur.execute("SELECT * FROM dados")
        data = cur.fetchall()
        con.close()
        return data

    @app.route("/", methods=['GET', 'POST'])
    @app.route("/index", methods=['GET', 'POST'])
    def index():
        query = ''
        dropdown_query = ''

        if request.method == 'POST':
            query = request.form.get('search', '')
            dropdown_query = request.form.get('dropdown', '')
            print("Search:", query)
            print("Dropdown:", dropdown_query)

        data = query_database(query, dropdown_query)

        return render_template("layout.html", datas=data, dropdown_items=dropdown_items, query=query,
                               dropdown_query=dropdown_query)

    return app
