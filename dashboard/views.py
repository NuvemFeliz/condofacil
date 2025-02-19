from django.shortcuts import render
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta
from condominios.models import Condominio
from moradores.models import Morador, Divida
from funcionarios.models import Funcionario
from reservas.models import Reserva
from financeiro.models import Transacao, Despesa
from ocorrencias.models import Ocorrencia
from assinaturas.models import Assinatura
from django.contrib.auth.models import User
from django.shortcuts import render
from django.db.models import Sum
from financeiro.models import Transacao, TipoTransacao



def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')  # Confirme se esse template existe


def dashboard(request):
    # Estatísticas básicas
    total_condominios = Condominio.objects.count()
    total_moradores = Morador.objects.count()
    total_funcionarios = Funcionario.objects.count()
    total_reservas = Reserva.objects.count()
    transacoes_recentes = Transacao.objects.order_by('-data')[:5]
    ocorrencias_pendentes = Ocorrencia.objects.filter(resolvido=False).count()
    total_assinantes = Assinatura.objects.count()
    
        # Buscar o tipo "entrada" corretamente
    tipo_entrada = TipoTransacao.objects.filter(nome="entrada").first()

    # Se o tipo "entrada" existir, faz os cálculos corretamente
    if tipo_entrada:
        total_caixa = Transacao.objects.filter(forma_pagamento='caixa', tipo=tipo_entrada).aggregate(total=Sum('valor'))['total'] or 0
        total_banco = Transacao.objects.filter(forma_pagamento='banco', tipo=tipo_entrada).aggregate(total=Sum('valor'))['total'] or 0
    else:
        total_caixa = 0
        total_banco = 0

    disponibilidade_financeira = total_caixa + total_banco

    context = {
        'total_caixa': total_caixa,
        'total_banco': total_banco,
        'disponibilidade_financeira': disponibilidade_financeira,
    }

    return render(request, 'dashboard/index.html', context)

    # Dívidas
    total_divida = Divida.objects.aggregate(total=Sum('valor'))['total'] or 0
    dois_meses_atras = timezone.now() - timedelta(days=60)
    devedores_mais_2_meses = Divida.objects.filter(data_vencimento__lte=dois_meses_atras).count()

    # Despesas (confira se o campo correto está sendo usado)
    despesas_pagas = Despesa.objects.filter(categoria='paga').aggregate(total=Sum('valor'))['total'] or 0
    despesas_por_pagar = Despesa.objects.filter(categoria='pendente').aggregate(total=Sum('valor'))['total'] or 0

    # Disponibilidade financeira
    total_caixa = Transacao.objects.filter(tipo='caixa', tipo_id='entrada').aggregate(total=Sum('valor'))['total'] or 0
    total_banco = Transacao.objects.filter(tipo='banco', tipo_id='entrada').aggregate(total=Sum('valor'))['total'] or 0
    disponibilidade_financeira = total_caixa + total_banco

    # Usuários logados
    vinte_quatro_horas_atras = timezone.now() - timedelta(hours=24)
    usuarios_logados_24h = User.objects.filter(last_login__gte=vinte_quatro_horas_atras).count()

    # Assinaturas
    assinaturas_pagas = Assinatura.objects.filter(tipo='pago').count()
    assinaturas_gratuitas = Assinatura.objects.filter(tipo='gratuito').count()
    assinaturas_canceladas = Assinatura.objects.filter(status='cancelada').count()
    assinaturas_vencidas = Assinatura.objects.filter(status='vencida').count()

    # Contexto para o template
    context = {
        'total_condominios': total_condominios,
        'total_moradores': total_moradores,
        'total_funcionarios': total_funcionarios,
        'total_reservas': total_reservas,
        'transacoes_recentes': transacoes_recentes,
        'ocorrencias_pendentes': ocorrencias_pendentes,
        'total_assinantes': total_assinantes,
        'assinaturas_pagas': assinaturas_pagas,
        'assinaturas_gratuitas': assinaturas_gratuitas,
        'assinaturas_canceladas': assinaturas_canceladas,
        'assinaturas_vencidas': assinaturas_vencidas,
        'usuarios_logados_24h': usuarios_logados_24h,
        'disponibilidade_financeira': disponibilidade_financeira,
        'despesas_pagas': despesas_pagas,
        'despesas_por_pagar': despesas_por_pagar,
        'total_divida': total_divida,
        'devedores_mais_2_meses': devedores_mais_2_meses,
    }

    return render(request, 'dashboard/dashboard.html', context)  # Confirme o nome e o local do template!
