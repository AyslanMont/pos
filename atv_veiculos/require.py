
import requests

if __name__ == "__main__":

    url = "http://127.0.0.1:8000"

    while True:

        opcao = int(input("""
        1 - Listar todos os veiculos
        2 - Pesquisa veiculos por título
        3 - Cadastrar um veiculos
        4 - Deletar um veiculos
        5 - Editar um veiculos
        6 - Sair
        """))

        match opcao:
            case 1:
                response = requests.get(f"{url}/veiculos")
                print(response.text)
            case 2:
                placa = input("Digite a placa do veículo: ")
                response = requests.get(f"{url}/veiculos/{placa}")
                print(response.text)
            case 3:
                nome = input("Digite o nome do veículo: ")
                marca = input("Digite a marca do veículo: ")
                modelo = input("Digite o modelo do veículo: ")
                placa = int(input("Digite a placa do veículo: "))

                veiculo = {
                    "nome": nome,
                    "marca": marca,
                    "modelo": modelo,
                    "placa": placa
                }

                response = requests.post(f"{url}/veiculos/", json=veiculo)
                print(f"{response.text} --------- status:{response.status_code}")
            case 4:
                placa = input("Digite a placa do veículo: ")
                response = requests.delete(f"{url}/veiculos/{placa}")
                print(f"{response.text} --------- status:{response.status_code}")
            case 5:
                placa = input("Digite a placa do veículo a ser alterado: ")
                nome = input("Digite o novo nome do veículo: ")
                marca = input("Digite a nova marca do veículo: ")
                modelo = input("Digite o novo modelo do veículo: ")
                placa_nova = int(input("Digite a nova placa do veículo: "))

                veiculo = {
                    "nome": nome,
                    "marca": marca,
                    "modelo": modelo,
                    "placa": placa_nova
                }

                response = requests.put(f"{url}/veiculos/{placa}", json=veiculo)
                print(f"{response.text} --------- status:{response.status_code}")
            case 6:
                break
