from fastapi import FastAPI, HTTPException, status
import pandas as pd

# Read the CSV file 
pedidos_data = pd.read_csv("pedidos.csv", encoding="utf-16", sep=';')

app = FastAPI()

@app.get("/pedidos/{id}")
def get_pedidos(id: int):
    dados = pedidos_data[pedidos_data["IdPedido"] == id]
    if dados.empty:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID não encontrado!")
    else:
         return  dados.to_dict(orient="records")[0]