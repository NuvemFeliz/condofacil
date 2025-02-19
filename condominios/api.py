from ninja import Router, UploadedFile, File
from django.shortcuts import get_object_or_404
from ninja.errors import HttpError
from .models import Condominio
from .schemas import CondominioIn, CondominioOut, CondominioUpdate
from auth_custom.api import AuthBearer
from ninja import Router
from typing import List


router = Router(tags=["Condomínios"])
# Criar um novo condomínio
@router.post(
    "/condominios/",
    response={201: CondominioOut, 400: dict},
    summary="Criar condomínio",
    description="Cria um novo condomínio com os dados fornecidos.",
    auth=AuthBearer(),
)
def criar_condominio(request, payload: CondominioIn, logo: UploadedFile = File(None)):
    try:
        proprietario = request.user
        condominio = Condominio.objects.create(**payload.dict(), proprietario=proprietario)
        if logo:
            condominio.logo.save(logo.name, logo)
        return 201, condominio
    except Exception as e:
        raise HttpError(400, {"detail": str(e)})

# Listar todos os condomínios
@router.get(
    "/condominios/",
    response=list[CondominioOut],
    summary="Listar condomínios",
    description="Retorna uma lista de todos os condomínios cadastrados.",
    auth=AuthBearer(),
)
def listar_condominios(request):
    return Condominio.objects.filter(proprietario=request.user)

# Obter detalhes de um condomínio
@router.get(
    "/condominios/{condominio_id}/",
    response={200: CondominioOut, 404: dict},
    summary="Detalhes do condomínio",
    description="Retorna os detalhes de um condomínio específico.",
    auth=AuthBearer(),
)
def detalhes_condominio(request, condominio_id: int):
    condominio = get_object_or_404(Condominio, id=condominio_id, proprietario=request.user)
    return 200, condominio

# Atualizar um condomínio
@router.put(
    "/condominios/{condominio_id}/",
    response={200: CondominioOut, 400: dict, 404: dict},
    summary="Atualizar condomínio",
    description="Atualiza os dados de um condomínio existente.",
    auth=AuthBearer(),
)
def atualizar_condominio(request, condominio_id: int, payload: CondominioUpdate, logo: UploadedFile = File(None)):
    condominio = get_object_or_404(Condominio, id=condominio_id, proprietario=request.user)
    try:
        for field, value in payload.dict().items():
            if value is not None:
                setattr(condominio, field, value)
        if logo:
            condominio.logo.save(logo.name, logo)
        condominio.save()
        return 200, condominio
    except Exception as e:
        raise HttpError(400, {"detail": str(e)})

# Excluir um condomínio
@router.delete(
    "/condominios/{condominio_id}/",
    response={204: None, 404: dict},
    summary="Excluir condomínio",
    description="Exclui um condomínio existente.",
    auth=AuthBearer(),
)
def excluir_condominio(request, condominio_id: int):
    condominio = get_object_or_404(Condominio, id=condominio_id, proprietario=request.user)
    condominio.delete()
    return 204, None