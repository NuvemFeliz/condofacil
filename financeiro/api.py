from ninja import Router, UploadedFile, File
from django.shortcuts import get_object_or_404
from ninja.errors import HttpError
from .models import TipoTransacao, Transacao, Despesa
from .schemas import TipoTransacaoIn, TipoTransacaoOut, TransacaoIn, TransacaoOut, DespesaIn, DespesaOut
from auth_custom.api import AuthBearer

router = Router(tags=["Financeiro"])

# Criar um tipo de transação
@router.post(
    "/tipos-transacao/",
    response={201: TipoTransacaoOut, 400: dict},
    summary="Criar tipo de transação",
    description="Cria um novo tipo de transação.",
    auth=AuthBearer(),
)
def criar_tipo_transacao(request, payload: TipoTransacaoIn):
    try:
        tipo_transacao = TipoTransacao.objects.create(**payload.dict())
        return 201, tipo_transacao
    except Exception as e:
        raise HttpError(400, {"detail": str(e)})

# Listar tipos de transação
@router.get(
    "/tipos-transacao/",
    response=list[TipoTransacaoOut],
    summary="Listar tipos de transação",
    description="Retorna uma lista de todos os tipos de transação.",
    auth=AuthBearer(),
)
def listar_tipos_transacao(request):
    return TipoTransacao.objects.all()

# Criar uma transação
@router.post(
    "/transacoes/",
    response={201: TransacaoOut, 400: dict},
    summary="Criar transação",
    description="Cria uma nova transação (pagamento de taxas, reservas, doações, etc.).",
    auth=AuthBearer(),
)
def criar_transacao(request, payload: TransacaoIn, comprovativo: UploadedFile = File(None)):
    try:
        condominio = get_object_or_404(Condominio, id=payload.condominio_id)
        tipo = get_object_or_404(TipoTransacao, id=payload.tipo_id)
        transacao = Transacao.objects.create(
            condominio=condominio,
            tipo=tipo,
            valor=payload.valor,
            descricao=payload.descricao,
            usuario=request.user,
        )
        if comprovativo:
            transacao.comprovativo.save(comprovativo.name, comprovativo)
        return 201, transacao
    except Exception as e:
        raise HttpError(400, {"detail": str(e)})

# Listar transações de um condomínio
@router.get(
    "/transacoes/{condominio_id}/",
    response=list[TransacaoOut],
    summary="Listar transações",
    description="Retorna uma lista de transações de um condomínio específico.",
    auth=AuthBearer(),
)
def listar_transacoes(request, condominio_id: int):
    condominio = get_object_or_404(Condominio, id=condominio_id)
    return condominio.transacoes.all()

# Criar uma despesa
@router.post(
    "/despesas/",
    response={201: DespesaOut, 400: dict},
    summary="Criar despesa",
    description="Cria uma nova despesa (pessoal, manutenção, etc.).",
    auth=AuthBearer(),
)
def criar_despesa(request, payload: DespesaIn):
    try:
        condominio = get_object_or_404(Condominio, id=payload.condominio_id)
        despesa = Despesa.objects.create(
            condominio=condominio,
            descricao=payload.descricao,
            valor=payload.valor,
            categoria=payload.categoria,
        )
        return 201, despesa
    except Exception as e:
        raise HttpError(400, {"detail": str(e)})

# Listar despesas de um condomínio
@router.get(
    "/despesas/{condominio_id}/",
    response=list[DespesaOut],
    summary="Listar despesas",
    description="Retorna uma lista de despesas de um condomínio específico.",
    auth=AuthBearer(),
)
def listar_despesas(request, condominio_id: int):
    condominio = get_object_or_404(Condominio, id=condominio_id)
    return condominio.despesas.all()