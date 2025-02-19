from ninja import Schema
from typing import Optional
from datetime import date

class CargoIn(Schema):
    nome: str
    descricao: Optional[str] = None

class CargoOut(Schema):
    id: int
    nome: str
    descricao: Optional[str] = None

class FuncionarioIn(Schema):
    condominio_id: int
    usuario_id: int
    cargo_id: int
    tipo_contratacao: str  # Novo campo
    salario: float
    data_contratacao: date
    horas_extras: Optional[float] = 0
    vales: Optional[float] = 0
    remuneracao_adicional: Optional[float] = 0

class FuncionarioOut(Schema):
    id: int
    condominio_id: int
    usuario_id: int
    cargo: CargoOut
    tipo_contratacao: str  # Novo campo
    salario: float
    data_contratacao: date
    horas_extras: float
    vales: float
    remuneracao_adicional: float