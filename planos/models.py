from django.db import models

class Plano(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Plano")
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)
    preco_mensal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço Mensal")
    limite_moradores = models.IntegerField(verbose_name="Limite de Moradores", default=0)
    limite_funcionarios = models.IntegerField(verbose_name="Limite de Funcionários", default=0)
    limite_espacos_comuns = models.IntegerField(verbose_name="Limite de Espaços Comuns", default=0)
    suporte_prioritario = models.BooleanField(default=False, verbose_name="Suporte Prioritário")
    relatorios_avancados = models.BooleanField(default=False, verbose_name="Relatórios Avançados")

    class Meta:
        verbose_name = "Plano"
        verbose_name_plural = "Planos"

    def __str__(self):
        return f"{self.nome} - R${self.preco_mensal}/mês"


class Assinatura(models.Model):
    condominio = models.OneToOneField('condominios.Condominio', on_delete=models.CASCADE, related_name="assinatura")
    plano = models.ForeignKey(Plano, on_delete=models.SET_NULL, null=True, related_name="assinaturas")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_renovacao = models.DateField(verbose_name="Data de Renovação", blank=True, null=True)
    ativo = models.BooleanField(default=True, verbose_name="Ativo")

    class Meta:
        verbose_name = "Assinatura"
        verbose_name_plural = "Assinaturas"

    def __str__(self):
        return f"Assinatura de {self.condominio.nome} - {self.plano.nome}"