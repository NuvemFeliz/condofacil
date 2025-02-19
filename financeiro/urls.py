from django.db import models
from condominios.models import Condominio
from auth_custom.models import User

class TipoTransacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Transação")
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='transacoes')
    tipo = models.ForeignKey(TipoTransacao, on_delete=models.CASCADE, related_name='transacoes')
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    data = models.DateTimeField(auto_now_add=True, verbose_name="Data da Transação")
    comprovativo = models.FileField(upload_to='comprovativos/', blank=True, null=True, verbose_name="Comprovante")
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transacoes')

    def __str__(self):
        return f"{self.tipo.nome} - {self.valor}"

class Despesa(models.Model):
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='despesas')
    descricao = models.TextField(verbose_name="Descrição")
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    data = models.DateTimeField(auto_now_add=True, verbose_name="Data da Despesa")
    categoria = models.CharField(max_length=100, verbose_name="Categoria")  # Ex: Pessoal, Manutenção, etc.

    def __str__(self):
        return f"{self.descricao} - {self.valor}"