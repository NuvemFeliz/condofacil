from ninja import Router
from django.shortcuts import get_object_or_404
from ninja.errors import HttpError
from .models import Plano, Assinatura
from .schemas import PlanoIn, PlanoOut, AssinaturaIn, AssinaturaOut
from auth_custom.api import AuthBearer

router = Router(tags=["Planos"])

# Criar um plano
@router.post(
    "/planos/",
    response={201: PlanoOut, 400: dict},
    summary="Criar plano",
    description="Cria um novo plano de assinatura.",
    auth=AuthBearer(),
)
def criar_plano(request, payload: PlanoIn):
    try:
        plano = Plano.objects.create(**payload.dict())
        return 201, plano
    except Exception as e:
        raise HttpError(400, {"detail": str(e)})

# Listar planos
@router.get(
    "/planos/",
    response=list[PlanoOut],
    summary="Listar planos",
    description="Retorna uma lista de todos os planos disponíveis.",
    auth=AuthBearer(),
)
def listar_planos(request):
    return Plano.objects.all()

# Criar uma assinatura
@router.post(
    "/assinaturas/",
    response={201: AssinaturaOut, 400: dict},
    summary="Criar assinatura",
    description="Cria uma nova assinatura para um condomínio.",
    auth=AuthBearer(),
)
def criar_assinatura(request, payload: AssinaturaIn):
    try:
        condominio = get_object_or_404(Condominio, id=payload.condominio_id)
        plano = get_object_or_404(Plano, id=payload.plano_id)
        assinatura = Assinatura.objects.create(
            condominio=condominio,
            plano=plano,
            data_inicio=payload.data_inicio,
        )
        return 201, assinatura
    except Exception as e:
        raise HttpError(400, {"detail": str(e)})

# Listar assinaturas de um condomínio
@router.get(
    "/assinaturas/{condominio_id}/",
    response=list[AssinaturaOut],
    summary="Listar assinaturas",
    description="Retorna uma lista de assinaturas de um condomínio específico.",
    auth=AuthBearer(),
)
def listar_assinaturas(request, condominio_id: int):
    condominio = get_object_or_404(Condominio, id=condominio_id)
    return condominio.assinaturas.all()

# Atualizar uma assinatura
@router.put(
    "/assinaturas/{assinatura_id}/",
    response={200: AssinaturaOut, 400: dict, 404: dict},
    summary="Atualizar assinatura",
    description="Atualiza os dados de uma assinatura existente.",
    auth=AuthBearer(),
)
def atualizar_assinatura(request, assinatura_id: int, payload: AssinaturaIn):
    assinatura = get_object_or_404(Assinatura, id=assinatura_id)
    try:
        for field, value in payload.dict().items():
            if value is not None:
                setattr(assinatura, field, value)
        assinatura.save()
        return 200, assinatura
    except Exception as e:
        raise HttpError(400, {"detail": str(e)})

# Cancelar uma assinatura
@router.patch(
    "/assinaturas/{assinatura_id}/cancelar/",
    response={200: AssinaturaOut, 404: dict},
    summary="Cancelar assinatura",
    description="Cancela uma assinatura existente.",
    auth=AuthBearer(),
)
def cancelar_assinatura(request, assinatura_id: int):
    assinatura = get_object_or_404(Assinatura, id=assinatura_id)
    assinatura.ativo = False
    assinatura.save()
    return 200, assinatura