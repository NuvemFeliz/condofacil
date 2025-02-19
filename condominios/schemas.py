from ninja import Schema
from typing import Optional
from datetime import datetime

class CondominioIn(Schema):
    nome: str
    endereco: str
    provincia: Optional[str] = None
    estado: Optional[str] = None
    nif: Optional[str] = None
    pais: str = "Angola"
    tipo_condominio: str = "predio"
    numero_andares: Optional[int] = None
    numero_apartamentos: Optional[int] = None
    numero_vivendas: Optional[int] = None

class CondominioOut(Schema):
    id: int
    nome: str
    endereco: str
    provincia: Optional[str] = None
    estado: Optional[str] = None
    nif: Optional[str] = None
    pais: str
    tipo_condominio: str
    numero_andares: Optional[int] = None
    numero_apartamentos: Optional[int] = None
    numero_vivendas: Optional[int] = None
    data_cadastro: datetime
    logo: Optional[str] = None
    proprietario_id: int

class CondominioUpdate(Schema):
    nome: Optional[str] = None
    endereco: Optional[str] = None
    provincia: Optional[str] = None
    estado: Optional[str] = None
    nif: Optional[str] = None
    pais: Optional[str] = None
    tipo_condominio: Optional[str] = None
    numero_andares: Optional[int] = None
    numero_apartamentos: Optional[int] = None
    numero_vivendas: Optional[int] = None