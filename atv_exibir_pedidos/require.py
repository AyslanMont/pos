import requests

while True:
    user_id =  int(input("Digite o  ID do pedido (0 para sair): "))

    if user_id != 0:
        response = requests.get(f"http://localhost:8000/pedidos/{user_id}")
        print(response.text)
    else:
        break