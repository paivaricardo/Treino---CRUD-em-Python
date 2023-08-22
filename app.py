"""
    Inserir Livro
    Listar Livros
    Atualizar Livro
    Deletar Livro
    Sair
"""

from service.livro_service import LivroService
from model.livro_model import Livro

def mostrar_menu_principal():
    print("")
    print("Bem-vindo ao sistema da biblioteca!")
    print("1 - Inserir Livro")
    print("2 - Listar Livros")
    print("3 - Atualizar Livro")
    print("4 - Deletar Livro")  
    print("5 - Sair")

def validar_opcao_usuario_menu_principal():
    input_valido = False

    while not input_valido:
        try:
            opcao_desejada = int(input("Digite a opção desejada (1 - 5):"))

            if opcao_desejada not in range(1, 6):
                raise ValueError
            
            input_valido = True

            return opcao_desejada
        except Exception as e:
            print(f"Houve um erro ao processar a opção: {e}")


def inserir_livro():
    print()
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano_publicacao = int(input("Digite o ano de publição do livro: "))

    livro_cadastro = Livro()
    livro_cadastro.titulo = titulo
    livro_cadastro.autor = autor
    livro_cadastro.ano_publicacao = ano_publicacao

    livro_service.inserir_livro_service(livro_cadastro)

    print("Livro cadastrado com sucesso!")

def listar_livros():
    livros = livro_service.listar_livros_service()

    if len(livros) == 0:
        print("Não há livros cadastrados na base de dados! Cadastre um novo!")
    else:
        for id, titulo, autor, ano in livros:
            print(f"Id: {id}, Título: {titulo}, Autor: {autor}, Ano: {ano}")


def atualizar_livro():
    id_livro = int(input("Digite o id do livro que deseja atualizar: "))

    livros = livros = livro_service.listar_livros_service()

    livro_encontrado = next((livro_tuple for livro_tuple in livros if livro_tuple[0] == id_livro), None)

    if livro_encontrado is not None:
        print("Livro econtrado!")
        id, titulo, autor, ano = livro_encontrado
        print(f"Id: {id}, Título: {titulo}, Autor: {autor}, Ano: {ano}")
        print()

        titulo_atualizar = input("Digite o novo título do livro: ")
        autor_atualizar = input("Digite o novo autor: ")
        ano_publicacao_atualizar = int(input("Digite o novo ano de publicação: "))
        
        livro_atualizar = Livro()
        livro_atualizar.id = id
        livro_atualizar.titulo = titulo_atualizar
        livro_atualizar.autor = autor_atualizar
        livro_atualizar.ano_publicacao = ano_publicacao_atualizar

        livro_service.atualizar_livro_service(livro_atualizar)

        print("Livro atualizado!")

    if livro_encontrado is None:
        print("Livro não localizado na base de dados.")


def deletar_livro():
    id_livro = int(input("Digite o id do livro que deseja deletar: "))
    livro_service.deletar_livro_service(id_livro)

    print("Livro excluído!")


if __name__ == "__main__":
    # Inicilizar a conexão com banco de dados:
    livro_service = LivroService()

    livro_service.inicializar_tabelas_banco_dados_service()

    app_loop = True
    
    while app_loop:
        mostrar_menu_principal()
        opcao = validar_opcao_usuario_menu_principal()

        match opcao:
            case 1:
                inserir_livro()
            case 2:
                listar_livros()
            case 3:
                atualizar_livro()
            case 4:
                deletar_livro()
            case 5:
                print("Programa encerrado.")
                app_loop = False