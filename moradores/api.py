from ninja import Router
from django.shortcuts import get_object_or_404
from ninja.errors import HttpError
from .models import Morador, UnidadeHabitacional
from .schemas import MoradorIn, MoradorOut, UnidadeHabitacionalOut
from auth_custom.api import AuthBearer

router = Router(tags=["Moradores"])

# Criar um morador
@router.post(
    "/moradores/",
    response={201: MoradorOut, 400: dict},
    summary="Criar morador",
    description="Cria um novo morador com os dados fornecidos.",
    auth=AuthBearer(),
)
def criar_morador(request, payload: MoradorIn):
    try:
        usuario = get_object_or_404(User, id=payload.usuario_id)
        condominio = get_object_or_404(Condominio, id=payload.condominio_id)
        unidade = get_object_or_404(UnidadeHabitacional, id=payload.unidade_id) if payload.unidade_id else None

        morador = Morador.objects.create(
            usuario=usuario,
            condominio=condominio,
            unidade=unidade,
            status=payload.status,
            telefone=payload.telefone,
            documento=payload.documento,
        )
        return 201, morador
    except Exception as e:
        raise HttpError(400, {"detail": str(e)})

# Listar moradores de um condomínio
@router.get(
    "/moradores/{condominio_id}/",
    response=list[MoradorOut],
    summary="Listar moradores",
    description="Retorna uma lista de moradores de um condomínio específico.",
    auth=AuthBearer(),
)
def listar_moradores(request, condominio_id: int):
    condominio = get_object_or_404(Condominio, id=condominio_id)
    return condominio.moradores.all()

# Detalhes de um morador
@router.get(
    "/moradores/detalhes/{morador_id}/",
    response={200: MoradorOut, 404: dict},
    summary="Detalhes do morador",
    description="Retorna os detalhes de um morador específico.",
    auth=AuthBearer(),
)
def detalhes_morador(request, morador_id: int):
    morador = get_object_or_404(Morador, id=morador_id)
    return 200, morador

# Atualizar um morador
@router.put(
    "/moradores/{morador_id}/",
    response={200: MoradorOut, 400: dict, 404: dict},
    summary="Atualizar morador",
    description="Atualiza os dados de um morador existente.",
    auth=AuthBearer(),
)
def atualizar_morador(request, morador_id: int, payload: MoradorIn):
    morador = get_object_or_404(Morador, id=morador_id)
    try:
        for field, value in payload.dict().items():
            if value is not None:
                setattr(morador, field, value)
        morador.save()
        return 200, morador
    except Exception as e:
        raise HttpError(400, {"detail": str(e)})

# Excluir um morador
@router.delete(
    "/moradores/{morador_id}/",
    response={204: None, 404: dict},
    summary="Excluir morador",
    description="Exclui um morador existente.",
    auth=AuthBearer(),
)
def excluir_morador(request, morador_id: int):
    morador = get_object_or_404(Morador, id=morador_id)
    morador.delete()
    return 204, None