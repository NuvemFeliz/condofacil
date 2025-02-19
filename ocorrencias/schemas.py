from ninja import Schema
from typing import Optional
from datetime import datetime

class TipoOcorrenciaIn(Schema):
    nome: str
    descricao: Optional[str] = None

class TipoOcorrenciaOut(Schema):
    id: int
    nome: str
    descricao: Optional[str] = None

class OcorrenciaIn(Schema):
    condominio_id: int
    tipo_id: int
    descricao: str

class OcorrenciaOut(Schema):
    id: int
    condominio_id: int
    tipo: TipoOcorrenciaOut
    descricao: str
    data: datetime
    usuario_id: int
    resolvido: bool

class ComunicadoIn(Schema):
    condominio_id: int
    titulo: str
    mensagem: str

class ComunicadoOut(Schema):
    id: int
    condominio_id: int
    titulo: str
    mensagem: str
    data: datetime
    usuario_id: int