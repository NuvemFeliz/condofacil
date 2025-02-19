from django.db import models
from condominios.models import Condominio
from auth_custom.models import User

class EspacoComum(models.Model):
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name="espacos_comuns")
    nome = models.CharField(max_length=100, verbose_name="Nome do Espaço")
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)
    capacidade = models.IntegerField(verbose_name="Capacidade Máxima", default=0)
    valor_reserva = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor da Reserva", default=0)

    class Meta:
        verbose_name = "Espaço Comum"
        verbose_name_plural = "Espaços Comuns"

    def __str__(self):
        return f"{self.nome} - {self.condominio.nome}"


class Reserva(models.Model):
    espaco = models.ForeignKey(EspacoComum, on_delete=models.CASCADE, related_name="reservas")
    morador = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservas")
    data_reserva = models.DateTimeField(verbose_name="Data da Reserva")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Pago", default=0)
    comprovativo_pagamento = models.FileField(upload_to="comprovativos/", blank=True, null=True, verbose_name="Comprovativo de Pagamento")
    status = models.CharField(max_length=20, default="pendente", verbose_name="Status da Reserva")

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return f"Reserva de {self.espaco.nome} por {self.morador.username} em {self.data_reserva}"