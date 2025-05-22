from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Car(BaseModel):
    id: Optional[int] = None
    modelo: str
    marca: str
    ano: int
    disponivel: bool

class Client(BaseModel):
    id: Optional[int] = None
    nome: str
    cpf: str
    telefone: str

class Rent(BaseModel):
    id: Optional[int] = None
    id_cliente: int
    id_carro: int
    data_inicio: datetime
    data_fim: datetime
    
