from ninja import Schema
from datetime import date
from typing import Optional

# Schema para listar assinaturas
class AssinaturaSchema(Schema):
    id: int
    usuario_id: Optional[int] = None  # ID do usuário (opcional)
    tipo: str  # Tipo de assinatura (gratuito/pago)
    status: str  # Status da assinatura (ativa/cancelada/vencida)
    data_inicio: date  # Data de início da assinatura
    data_vencimento: date  # Data de vencimento da assinatura
    valor: float  # Valor da assinatura
    created_at: str  # Data de criação (serializada como string)
    updated_at: str  # Data de atualização (serializada como string)

# Schema para criar/atualizar assinaturas
class AssinaturaCreateSchema(Schema):
    usuario_id: Optional[int] = None  # ID do usuário (opcional)
    tipo: str  # Tipo de assinatura (gratuito/pago)
    status: str  # Status da assinatura (ativa/cancelada/vencida)
    data_inicio: date  # Data de início da assinatura
    data_vencimento: date  # Data de vencimento da assinatura
    valor: float  # Valor da assinatura

# Schema para resposta de sucesso/erro
class MessageSchema(Schema):
    message: str  # Mensagem de sucesso ou erro