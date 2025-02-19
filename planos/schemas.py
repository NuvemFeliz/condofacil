from ninja import Schema
from typing import Optional
from datetime import date

class PlanoIn(Schema):
    nome: str
    descricao: Optional[str] = None
    preco_mensal: float
    limite_moradores: int
    limite_funcionarios: int
    limite_espacos_comuns: int
    suporte_prioritario: bool
    relatorios_avancados: bool

class PlanoOut(Schema):
    id: int
    nome: str
    descricao: Optional[str] = None
    preco_mensal: float
    limite_moradores: int
    limite_funcionarios: int
    limite_espacos_comuns: int
    suporte_prioritario: bool
    relatorios_avancados: bool

class AssinaturaIn(Schema):
    condominio_id: int
    plano_id: int
    data_inicio: date

class AssinaturaOut(Schema):
    id: int
    condominio_id: int
    plano: PlanoOut
    data_inicio: date
    data_renovacao: Optional[date] = None
    ativo: bool