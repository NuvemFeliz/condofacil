from ninja import Schema
from typing import Optional
from datetime import datetime

class TipoTransacaoIn(Schema):
    nome: str
    descricao: Optional[str] = None

class TipoTransacaoOut(Schema):
    id: int
    nome: str
    descricao: Optional[str] = None

class TransacaoIn(Schema):
    condominio_id: int
    tipo_id: int
    valor: float
    descricao: Optional[str] = None
    comprovante: Optional[str] = None  # URL ou base64 para o comprovante

class TransacaoOut(Schema):
    id: int
    condominio_id: int
    tipo: TipoTransacaoOut
    valor: float
    data: datetime
    comprovativo: Optional[str] = None
    descricao: Optional[str] = None
    usuario_id: int

class DespesaIn(Schema):
    condominio_id: int
    descricao: str
    valor: float
    categoria: str

class DespesaOut(Schema):
    id: int
    condominio_id: int
    descricao: str
    valor: float
    data: datetime
    categoria: str