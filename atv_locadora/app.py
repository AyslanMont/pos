from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from models import Car, Rent, Client
from typing import List, Dict


app = FastAPI()

carros: List[Car] = list()
clientes: List[Client] = list()
reservas: List[Rent] = list()


@app.get("/carros/", response_model=List[Car])
def get_carros():
    return carros


@app.post("/carros/", response_model=Car, status_code=status.HTTP_201_CREATED)
def post_carro(carro: Car):
    id_carro = len(carros) + 1
    if not carro in carros:
        carro.id = id_carro
        carros.append(carro)
        return carro
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)


@app.put("/carros/{id_carro}", response_model=Car)
def put_carro(id_carro: int, carro_atualizado: Car):
    for index, carro in enumerate(carros):
        if id_carro == carro.id:
            carro_atualizado.id = index
            carros[index] = carro_atualizado
            return carro_atualizado
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.delete("/carros/{id_carro}", response_model=Car)
def del_carro(id_carro: int):
    for index, carro in enumerate(carros):
        if id_carro == carro.id:
            carro_del = carros.pop(index)
            return carro_del
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.get("/carros/disponiveis", response_model=List[Car])
def get_carros_disponiveis():
    lista_aux: List[Car] = list()
    for carro in carros:
        if carro.disponivel == True:
            lista_aux.append(carro)
    return lista_aux


@app.get("/clientes/", response_model=List[Client])
def get_clientes():
    return clientes


@app.post("/clientes/", response_model=Client, status_code=status.HTTP_201_CREATED)
def post_cliente(cliente: Client):
    id_cliente = len(clientes) + 1
    if not cliente in clientes:
        cliente.id = id_cliente
        carros.append(cliente)
        return cliente
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)


@app.get("/clientes/{id_cliente}", response_model=Client)
def get_cliente(id_cliente: int):
    if clientes[id_cliente]:
        cliente = clientes[id_cliente]
        return cliente
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.get("/reservas/", response_model=List[Rent])
def get_reservas():
    return reservas


@app.post("/reservas/", response_model=Rent, status_code=status.HTTP_201_CREATED)
def post_reservas(reserva: Rent):
    id_reserva = len(reservas) + 1
    if not reserva in reservas and carros[reserva.id_carro]:
        reserva.id = id_reserva
        reservas.append(reserva)
        carro = carros[reserva.id_carro]
        carro.disponivel = False
        return reserva
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)


@app.delete("/reservas/{id_reserva}", response_model=Rent)
def del_carro(id_reserva: int):
    for index, reserva in enumerate(reservas):
        if id_reserva == reserva.id:
            reserva_del = reservas.pop(index)
            return reserva_del
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)