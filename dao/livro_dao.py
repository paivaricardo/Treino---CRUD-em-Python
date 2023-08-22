from database.database_connection import DatabaseConnection
from model.livro_model import Livro

"""
O programa deve mostrar um menu com as seguintes opções:
Inserir Livro
Listar Livros
Atualizar Livro
Deletar Livro

Sair

"""

class LivroDao:
    def inicializar_tabelas_banco_dados(self):
        connection = DatabaseConnection.connect_database()

        with connection:
            cursor = connection.cursor()

            sql = """
                CREATE TABLE IF NOT EXISTS biblioteca (
                    id INTEGER PRIMARY KEY AUTO_INCREMENT,
                    titulo VARCHAR(255) NOT NULL,
                    autor VARCHAR(255) NOT NULL,
                    ano_publicacao INTEGER NOT NULL
                );
            """

            cursor.execute(sql)

            print("Inicializada a tabela do banco de dados!")

            connection.commit()

    def inserir_livro(self, livro) -> None:
        connection = DatabaseConnection.connect_database()
        
        with connection:
            cursor = connection.cursor()

            sql = """
                INSERT INTO biblioteca (titulo, autor, ano_publicacao)
                VALUES (%s, %s, %s);
            """

            params = (livro.titulo, livro.autor, livro.ano_publicacao)

            cursor.execute(sql, params)

            connection.commit()

    def listar_livros(self) -> list:
        connection = DatabaseConnection.connect_database()
        
        with connection:
            cursor = connection.cursor()

            sql = """
                SELECT * FROM biblioteca;
            """

            cursor.execute(sql)

            results = cursor.fetchall()

            return results

    def atualizar_livro(self, livro):
        connection = DatabaseConnection.connect_database()
        
        with connection:
            cursor = connection.cursor()

            sql = """
                UPDATE biblioteca SET titulo = %s, autor = %s, ano_publicacao = %s WHERE id = %s;
            """

            params = (livro.titulo, livro.autor, livro.ano_publicacao, livro.id)

            cursor.execute(sql, params)

            connection.commit()

    def deletar_livro(self, id: int):
        connection = DatabaseConnection.connect_database()
        
        with connection:
            cursor = connection.cursor()

            sql = """
                DELETE FROM biblioteca WHERE id = %s
            """

            cursor.execute(sql, (id,))

            connection.commit()