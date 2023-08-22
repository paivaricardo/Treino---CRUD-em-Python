from mysql import connector

connection_params = {
    "db": "biblioteca",
    "host": "localhost",
    "user": "root",
    "password": "root",
    "port": 3306
}

class DatabaseConnection:
    @classmethod
    def connect_database(cls):
        try:
            connection = connector.connect(**connection_params)
            if connection:
                print("Conectado à base de dados MySQL")

                return connection
        except Exception as e:
            print("Houve um erro ao tentar conectar com a base de dados MySQL.")
            return None
