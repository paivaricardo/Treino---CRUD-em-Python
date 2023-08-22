from dao.livro_dao import LivroDao

class LivroService:
    def __init__(self):
        self.dao = LivroDao()

    def inicializar_tabelas_banco_dados_service(self):
        self.dao.inicializar_tabelas_banco_dados()

    def inserir_livro_service(self, livro) -> None:
        self.dao.inserir_livro(livro)

    def listar_livros_service(self) -> list:
        return self.dao.listar_livros()

    def atualizar_livro_service(self, livro) -> None:
        self.dao.atualizar_livro(livro)

    def deletar_livro_service(self, id: int) -> None:
        self.dao.deletar_livro(id)