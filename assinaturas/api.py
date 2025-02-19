from ninja import NinjaAPI, Router
from .models import Assinatura
from .schemas import AssinaturaSchema, AssinaturaCreateSchema, MessageSchema
from django.shortcuts import get_object_or_404
from typing import List

# Cria um router para as assinaturas
router = Router()

# Rotas da API
@router.get("/", response=List[AssinaturaSchema])
def listar_assinaturas(request):
    """Lista todas as assinaturas."""
    return Assinatura.objects.all()

@router.get("/{assinatura_id}", response=AssinaturaSchema)
def obter_assinatura(request, assinatura_id: int):
    """Obtém uma assinatura pelo ID."""
    return get_object_or_404(Assinatura, id=assinatura_id)

@router.post("/", response=AssinaturaSchema)
def criar_assinatura(request, payload: AssinaturaCreateSchema):
    """Cria uma nova assinatura."""
    assinatura = Assinatura.objects.create(**payload.dict())
    return assinatura

@router.put("/{assinatura_id}", response=AssinaturaSchema)
def atualizar_assinatura(request, assinatura_id: int, payload: AssinaturaCreateSchema):
    """Atualiza uma assinatura existente."""
    assinatura = get_object_or_404(Assinatura, id=assinatura_id)
    for attr, value in payload.dict().items():
        setattr(assinatura, attr, value)
    assinatura.save()
    return assinatura

@router.delete("/{assinatura_id}", response=MessageSchema)
def deletar_assinatura(request, assinatura_id: int):
    """Exclui uma assinatura."""
    assinatura = get_object_or_404(Assinatura, id=assinatura_id)
    assinatura.delete()
    return {"message": "Assinatura excluída com sucesso."}