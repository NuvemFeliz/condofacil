from ninja import Schema
from typing import Optional
from datetime import datetime

class EspacoComumOut(Schema):
    id: int
    nome: str
    descricao: Optional[str] = None
    capacidade: int
    valor_reserva: float

class ReservaIn(Schema):
    espaco_id: int
    morador_id: int
    data_reserva: datetime
    valor_pago: Optional[float] = 0
    comprovativo_pagamento: Optional[str] = None  # URL ou base64 para o comprovante

class ReservaOut(Schema):
    id: int
    espaco: EspacoComumOut
    morador_id: int
    data_reserva: datetime
    data_criacao: datetime
    valor_pago: float
    comprovativo_pagamento: Optional[str] = None
    status: str