from fastapi import FastAPI, HTTPException, status
from models import Veiculo
from typing import List


app = FastAPI()

veiculos = []

@app.get("/veiculos/", response_model=List[Veiculo])
def get_veiculos():
    return veiculos


@app.post("/veiculos/", response_model=Veiculo)
def post_veiculos(veiculo: Veiculo):
    for veiculo_check in veiculos:
        if veiculo_check.placa == veiculo.placa:
            raise HTTPException(status.HTTP_409_CONFLICT, "Já existe um veículo com esta placa!")
    veiculos.append(veiculo)
    return veiculo


@app.put("/veiculos/{placa}", response_model=Veiculo)
def put_veiculos(placa: int, veiculo_novo: Veiculo):
    for index, veiculo_check in enumerate(veiculos):
        if veiculo_check.placa == placa:
            veiculos[index] = veiculo_novo
            return veiculo_novo
    raise HTTPException(status.HTTP_404_NOT_FOUND, "Veículo não encontrado!")


@app.delete("/veiculos/{placa}", response_model=Veiculo)
def delete_veiculos(placa: int):
    for index, veiculo_check in enumerate(veiculos):
        if veiculo_check.placa == placa:
            veiculos.pop(index)
            return veiculo_check
    raise HTTPException(status.HTTP_404_NOT_FOUND, "Já existe um veículo com esta placa!")
    