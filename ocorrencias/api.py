from ninja import Router
from django.shortcuts import get_object_or_404
from ninja.errors import HttpError
from .models import TipoOcorrencia, Ocorrencia, Comunicado
from .schemas import TipoOcorrenciaIn, TipoOcorrenciaOut, OcorrenciaIn, OcorrenciaOut, ComunicadoIn, ComunicadoOut
from auth_custom.api import AuthBearer

router = Router(tags=["Ocorrências e Comunicação"])

# Criar um tipo de ocorrência
@router.post(
    "/tipos-ocorrencia/",
    response={201: TipoOcorrenciaOut, 400: dict},
    summary="Criar tipo de ocorrência",
    description="Cria um novo tipo de ocorrência.",
    auth=AuthBearer(),
)
def criar_tipo_ocorrencia(request, payload: TipoOcorrenciaIn):
    try:
        tipo_ocorrencia = TipoOcorrencia.objects.create(**payload.dict())
        return 201, tipo_ocorrencia
    except Exception as e:
        raise HttpError(400, {"detail": str(e)})

# Listar tipos de ocorrência
@router.get(
    "/tipos-ocorrencia/",
    response=list[TipoOcorrenciaOut],
    summary="Listar tipos de ocorrência",
    description="Retorna uma lista de todos os tipos de ocorrência.",
    auth=AuthBearer(),
)
def listar_tipos_ocorrencia(request):
    return TipoOcorrencia.objects.all()

# Criar uma ocorrência
@router.post(
    "/ocorrencias/",
    response={201: OcorrenciaOut, 400: dict},
    summary="Criar ocorrência",
    description="Cria uma nova ocorrência (manutenção, reclamações, etc.).",
    auth=AuthBearer(),
)
def criar_ocorrencia(request, payload: OcorrenciaIn):
    try:
        condominio = get_object_or_404(Condominio, id=payload.condominio_id)
        tipo = get_object_or_404(TipoOcorrencia, id=payload.tipo_id)
        ocorrencia = Ocorrencia.objects.create(
            condominio=condominio,
            tipo=tipo,
            descricao=payload.descricao,
            usuario=request.user,
        )
        return 201, ocorrencia
    except Exception as e:
        raise HttpError(400, {"detail": str(e)})

# Listar ocorrências de um condomínio
@router.get(
    "/ocorrencias/{condominio_id}/",
    response=list[OcorrenciaOut],
    summary="Listar ocorrências",
    description="Retorna uma lista de ocorrências de um condomínio específico.",
    auth=AuthBearer(),
)
def listar_ocorrencias(request, condominio_id: int):
    condominio = get_object_or_404(Condominio, id=condominio_id)
    return condominio.ocorrencias.all()

# Marcar ocorrência como resolvida
@router.patch(
    "/ocorrencias/{ocorrencia_id}/resolver/",
    response={200: OcorrenciaOut, 404: dict},
    summary="Resolver ocorrência",
    description="Marca uma ocorrência como resolvida.",
    auth=AuthBearer(),
)
def resolver_ocorrencia(request, ocorrencia_id: int):
    ocorrencia = get_object_or_404(Ocorrencia, id=ocorrencia_id)
    ocorrencia.resolvido = True
    ocorrencia.save()
    return 200, ocorrencia

# Criar um comunicado
@router.post(
    "/comunicados/",
    response={201: ComunicadoOut, 400: dict},
    summary="Criar comunicado",
    description="Cria um novo comunicado para moradores e funcionários.",
    auth=AuthBearer(),
)
def criar_comunicado(request, payload: ComunicadoIn):
    try:
        condominio = get_object_or_404(Condominio, id=payload.condominio_id)
        comunicado = Comunicado.objects.create(
            condominio=condominio,
            titulo=payload.titulo,
            mensagem=payload.mensagem,
            usuario=request.user,
        )
        return 201, comunicado
    except Exception as e:
        raise HttpError(400, {"detail": str(e)})

# Listar comunicados de um condomínio
@router.get(
    "/comunicados/{condominio_id}/",
    response=list[ComunicadoOut],
    summary="Listar comunicados",
    description="Retorna uma lista de comunicados de um condomínio específico.",
    auth=AuthBearer(),
)
def listar_comunicados(request, condominio_id: int):
    condominio = get_object_or_404(Condominio, id=condominio_id)
    return condominio.comunicados.all()