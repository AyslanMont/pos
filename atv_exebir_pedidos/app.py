from fastapi import FastAPI
import pandas as pd

# Read the CSV file 
pedidos_data = pd.read_csv("pedidos.csv", encoding="utf-16", sep=';')

app = FastAPI()

@app.get("/pedidos/{id}")
def get_pedidos(id: int):
    dados = pedidos_data[pedidos_data["IdPedido"] == id]
    return  dados.to_dict(orient="records")[0]