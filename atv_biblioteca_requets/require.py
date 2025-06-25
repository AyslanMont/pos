import requests

if __name__ == "__main__":

    url = "http://127.0.0.1:8000"

    while True:

        opcao = int(input("""
        1 - Listar todos os livros
        2 - Pesquisa livro por título
        3 - Cadastrar um livro
        4 - Deletar um livro
        5 - Editar um livro
        6 - Sair
        """))

        match opcao:
            case 1:
                response = requests.get(f"{url}/livros")
                print(response.text)
            case 2:
                titulo = input("Digite o título do livro: ")
                response = requests.get(f"{url}/livros/{titulo}")
                print(response.text)
            case 3:
                titulo = input("Digite o título do livro: ")
                ano = int(input("Digite o ano do livro: "))
                edicao = int(input("Digite a edição do livro: "))

                livro = {
                    "titulo": titulo,
                    "ano": ano,
                    "edicao": edicao
                }

                response = requests.post(f"{url}/livros/", json=livro)
                print(f"{response.text} --------- status:{response.status_code}")
            case 4:
                titulo = input("Digite o título do livro: ")
                response = requests.delete(f"{url}/livros/{titulo}")
                print(f"{response.text} --------- status:{response.status_code}")
            case 5:
                titulo = input("Digite o título do livro a ser alterado: ")
                titulo_novo = input("Digite o novo título do livro: ")
                ano = int(input("Digite o novo ano do livro: "))
                edicao = int(input("Digite a nova edição do livro: "))

                livro = {
                    "titulo": titulo_novo,
                    "ano": ano,
                    "edicao": edicao
                }

                response = requests.put(f"{url}/livros/{titulo}", json=livro)
                print(f"{response.text} --------- status:{response.status_code}")

            case 6:
                break