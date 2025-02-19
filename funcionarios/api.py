from ninja import Router
from django.shortcuts import get_object_or_404
from ninja.errors import HttpError
from .models import Cargo, Funcionario
from .schemas import CargoIn, CargoOut, FuncionarioIn, FuncionarioOut
from auth_custom.api import AuthBearer

router = Router(tags=["Funcionários"])

# Criar um cargo
@router.post(
    "/cargos/",
    response={201: CargoOut, 400: dict},
    summary="Criar cargo",
    description="Cria um novo cargo para funcionários.",
    auth=AuthBearer(),
)
def criar_cargo(request, payload: CargoIn):
    try:
        cargo = Cargo.objects.create(**payload.dict())
        return 201, cargo
    except Exception as e:
        raise HttpError(400, {"detail": str(e)})

# Listar cargos
@router.get(
    "/cargos/",
    response=list[CargoOut],
    summary="Listar cargos",
    description="Retorna uma lista de todos os cargos.",
    auth=AuthBearer(),
)
def listar_cargos(request):
    return Cargo.objects.all()

# Criar um funcionário
@router.post(
    "/funcionarios/",
    response={201: FuncionarioOut, 400: dict},
    summary="Criar funcionário",
    description="Cria um novo funcionário com os dados fornecidos.",
    auth=AuthBearer(),
)
def criar_funcionario(request, payload: FuncionarioIn):
    try:
        condominio = get_object_or_404(Condominio, id=payload.condominio_id)
        usuario = get_object_or_404(User, id=payload.usuario_id)
        cargo = get_object_or_404(Cargo, id=payload.cargo_id)
        funcionario = Funcionario.objects.create(
            condominio=condominio,
            usuario=usuario,
            cargo=cargo,
            tipo_contratacao=payload.tipo_contratacao,  # Novo campo
            salario=payload.salario,
            data_contratacao=payload.data_contratacao,
            horas_extras=payload.horas_extras,
            vales=payload.vales,
            remuneracao_adicional=payload.remuneracao_adicional,
        )
        return 201, funcionario
    except Exception as e:
        raise HttpError(400, {"detail": str(e)})

# Listar funcionários de um condomínio
@router.get(
    "/funcionarios/{condominio_id}/",
    response=list[FuncionarioOut],
    summary="Listar funcionários",
    description="Retorna uma lista de funcionários de um condomínio específico.",
    auth=AuthBearer(),
)
def listar_funcionarios(request, condominio_id: int):
    condominio = get_object_or_404(Condominio, id=condominio_id)
    return condominio.funcionarios.all()

# Atualizar um funcionário
@router.put(
    "/funcionarios/{funcionario_id}/",
    response={200: FuncionarioOut, 400: dict, 404: dict},
    summary="Atualizar funcionário",
    description="Atualiza os dados de um funcionário existente.",
    auth=AuthBearer(),
)
def atualizar_funcionario(request, funcionario_id: int, payload: FuncionarioIn):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    try:
        for field, value in payload.dict().items():
            if value is not None:
                setattr(funcionario, field, value)
        funcionario.save()
        return 200, funcionario
    except Exception as e:
        raise HttpError(400, {"detail": str(e)})

# Excluir um funcionário
@router.delete(
    "/funcionarios/{funcionario_id}/",
    response={204: None, 404: dict},
    summary="Excluir funcionário",
    description="Exclui um funcionário existente.",
    auth=AuthBearer(),
)
def excluir_funcionario(request, funcionario_id: int):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    funcionario.delete()
    return 204, None