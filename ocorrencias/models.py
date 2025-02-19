from django.db import models
from condominios.models import Condominio
from auth_custom.models import User

class TipoOcorrencia(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipo de Ocorrência")
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)

    def __str__(self):
        return self.nome

class Ocorrencia(models.Model):
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='ocorrencias')
    tipo = models.ForeignKey(TipoOcorrencia, on_delete=models.CASCADE, related_name='ocorrencias')
    descricao = models.TextField(verbose_name="Descrição")
    data = models.DateTimeField(auto_now_add=True, verbose_name="Data da Ocorrência")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ocorrencias')
    resolvido = models.BooleanField(default=False, verbose_name="Resolvido")

    def __str__(self):
        return f"{self.tipo.nome} - {self.descricao[:50]}"

class Comunicado(models.Model):
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='comunicados')
    titulo = models.CharField(max_length=200, verbose_name="Título")
    mensagem = models.TextField(verbose_name="Mensagem")
    data = models.DateTimeField(auto_now_add=True, verbose_name="Data do Comunicado")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comunicados')

    def __str__(self):
        return self.titulo
