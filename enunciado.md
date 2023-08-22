Exercício: Gerenciador de Biblioteca
Objetivo: Desenvolver um pequeno sistema de gerenciamento para uma biblioteca usando Python e MySQL. O sistema deve permitir ao usuário inserir, atualizar, excluir e listar livros.

Modelo de Dados: Utilize a seguinte estrutura para um livro:

id: Identificador único (chave primária)
titulo: Título do livro
autor: Nome do autor
ano_publicacao: Ano de publicação

Parte 1: Configuração do Banco de Dados
Crie o Banco de Dados: Utilize seu cliente MySQL preferido para criar um novo banco de dados chamado biblioteca.
Crie a Tabela: Dentro do banco de dados, crie uma tabela chamada livros que inclua as colunas mencionadas no modelo de dados.
Parte 2: Desenvolvimento do Programa
Utilize o módulo mysql-connector-python para conectar-se ao MySQL.

Menu Principal:

O programa deve mostrar um menu com as seguintes opções:
Inserir Livro
Listar Livros
Atualizar Livro
Deletar Livro
Sair

Funções CRUD:

Inserir: Solicite ao usuário os detalhes do livro e insira no banco de dados.
Listar: Mostre uma lista de todos os livros no banco de dados.
Atualizar: Solicite ao usuário o ID do livro que deseja atualizar e, em seguida, peça os novos detalhes.
Deletar: Solicite ao usuário o ID do livro que deseja deletar e remova-o do banco de dados.

Considerações Adicionais:
Utilize tratamento de exceções para lidar com possíveis erros, como entrada inválida ou problemas de conexão com o banco de dados.
Certifique-se de fechar a conexão com o banco de dados quando não estiver em uso.
Mantenha o código bem organizado e utilize funções para separar a lógica.

Critérios de Avaliação:
Funcionalidade: O programa atende às especificações CRUD?
Qualidade do Código: O código é bem estruturado e fácil de entender?
Manipulação de Banco de Dados: As operações com o banco de dados estão corretas e eficientes?
Boa sorte no exercício e no seu exame do SERPRO! Se tiver alguma dúvida ou precisar de mais orientações, estou aqui para ajudar.