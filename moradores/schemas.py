from ninja import Schema
from typing import Optional
from datetime import datetime

class UnidadeHabitacionalOut(Schema):
    id: int
    numero: str
    bloco: Optional[str] = None

class MoradorIn(Schema):
    usuario_id: int
    condominio_id: int
    unidade_id: Optional[int] = None
    status: str
    telefone: Optional[str] = None
    documento: str

class MoradorOut(Schema):
    id: int
    usuario_id: int
    condominio_id: int
    unidade: Optional[UnidadeHabitacionalOut] = None
    status: str
    telefone: Optional[str] = None
    documento: str
    data_cadastro: datetime