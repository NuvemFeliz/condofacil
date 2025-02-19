from ninja import Router, UploadedFile, File
from django.shortcuts import get_object_or_404
from ninja.errors import HttpError
from .models import EspacoComum, Reserva
from .schemas import EspacoComumOut, ReservaIn, ReservaOut
from auth_custom.api import AuthBearer
from typing import Optional


router = Router(tags=["Reservas"])

# Criar um espaço comum
@router.post(
    "/espacos/",
    response={201: EspacoComumOut, 400: dict},
    summary="Criar espaço comum",
    description="Cria um novo espaço comum no condomínio.",
    auth=AuthBearer(),
)
def criar_espaco_comum(request, nome: str, descricao: Optional[str] = None, capacidade: int = 0, valor_reserva: float = 0):
    try:
        condominio = request.user.condominio  # Supondo que o usuário autenticado seja o proprietário do condomínio
        espaco = EspacoComum.objects.create(
            condominio=condominio,
            nome=nome,
            descricao=descricao,
            capacidade=capacidade,
            valor_reserva=valor_reserva,
        )
        return 201, espaco
    except Exception as e:
        raise HttpError(400, {"detail": str(e)})

# Listar espaços comuns de um condomínio
@router.get(
    "/espacos/{condominio_id}/",
    response=list[EspacoComumOut],
    summary="Listar espaços comuns",
    description="Retorna uma lista de espaços comuns de um condomínio específico.",
    auth=AuthBearer(),
)
def listar_espacos_comuns(request, condominio_id: int):
    condominio = get_object_or_404(Condominio, id=condominio_id)
    return condominio.espacos_comuns.all()

# Criar uma reserva
@router.post(
    "/reservas/",
    response={201: ReservaOut, 400: dict},
    summary="Criar reserva",
    description="Cria uma nova reserva de espaço comum.",
    auth=AuthBearer(),
)
def criar_reserva(request, payload: ReservaIn, comprovante: UploadedFile = File(None)):
    try:
        espaco = get_object_or_404(EspacoComum, id=payload.espaco_id)
        morador = get_object_or_404(User, id=payload.morador_id)
        reserva = Reserva.objects.create(
            espaco=espaco,
            morador=morador,
            data_reserva=payload.data_reserva,
            valor_pago=payload.valor_pago,
        )
        if comprovante:
            reserva.comprovante_pagamento.save(comprovante.name, comprovante)
        return 201, reserva
    except Exception as e:
        raise HttpError(400, {"detail": str(e)})

# Listar reservas de um morador
@router.get(
    "/reservas/morador/{morador_id}/",
    response=list[ReservaOut],
    summary="Listar reservas do morador",
    description="Retorna uma lista de reservas de um morador específico.",
    auth=AuthBearer(),
)
def listar_reservas_morador(request, morador_id: int):
    morador = get_object_or_404(User, id=morador_id)
    return morador.reservas.all()

# Listar reservas de um espaço comum
@router.get(
    "/reservas/espaco/{espaco_id}/",
    response=list[ReservaOut],
    summary="Listar reservas do espaço",
    description="Retorna uma lista de reservas de um espaço comum específico.",
    auth=AuthBearer(),
)
def listar_reservas_espaco(request, espaco_id: int):
    espaco = get_object_or_404(EspacoComum, id=espaco_id)
    return espaco.reservas.all()

# Atualizar status de uma reserva
@router.patch(
    "/reservas/{reserva_id}/status/",
    response={200: ReservaOut, 400: dict, 404: dict},
    summary="Atualizar status da reserva",
    description="Atualiza o status de uma reserva existente.",
    auth=AuthBearer(),
)
def atualizar_status_reserva(request, reserva_id: int, status: str):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    try:
        reserva.status = status
        reserva.save()
        return 200, reserva
    except Exception as e:
        raise HttpError(400, {"detail": str(e)})

# Excluir uma reserva
@router.delete(
    "/reservas/{reserva_id}/",
    response={204: None, 404: dict},
    summary="Excluir reserva",
    description="Exclui uma reserva existente.",
    auth=AuthBearer(),
)
def excluir_reserva(request, reserva_id: int):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    reserva.delete()
    return 204, None