from django.db import models
from condominios.models import Condominio
from auth_custom.models import User


class UnidadeHabitacional(models.Model):
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name="unidades")
    numero = models.CharField(max_length=10, verbose_name="Número da Unidade")
    bloco = models.CharField(max_length=20, verbose_name="Bloco", blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["condominio", "numero", "bloco"], name="unique_unidade_por_condominio")
        ]
        verbose_name = "Unidade Habitacional"
        verbose_name_plural = "Unidades Habitacionais"

    def __str__(self):
        return f"Bloco {self.bloco}, Unidade {self.numero} - {self.condominio.nome}" if self.bloco else f"Unidade {self.numero} - {self.condominio.nome}"


class Morador(models.Model):
    PROPRIETARIO = "Proprietário"
    INQUILINO = "Inquilino"

    STATUS_MORADOR_CHOICES = [
        (PROPRIETARIO, "Proprietário"),
        (INQUILINO, "Inquilino"),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="morador")
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name="moradores")
    unidade = models.ForeignKey(UnidadeHabitacional, on_delete=models.SET_NULL, related_name="moradores", null=True, blank=True)

    status = models.CharField(max_length=20, choices=STATUS_MORADOR_CHOICES, verbose_name="Status do Morador")
    telefone = models.CharField(max_length=15, verbose_name="Telefone", blank=True, null=True)
    documento = models.CharField(max_length=18, verbose_name="BI/NIF", unique=True)  # CPF (14) ou CNPJ (18)

    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["usuario", "condominio"], name="unique_morador_por_condominio")
        ]
        verbose_name = "Morador"
        verbose_name_plural = "Moradores"

    def __str__(self):
        unidade_info = f" - Unidade {self.unidade.numero}" if self.unidade else ""
        return f"{self.usuario.username} - {self.condominio.nome}{unidade_info} ({self.status})"


class Divida(models.Model):
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE, related_name="dividas")
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor da Dívida")
    descricao = models.TextField(verbose_name="Descrição")
    data_vencimento = models.DateField(verbose_name="Data de Vencimento")
    pago = models.BooleanField(default=False, verbose_name="Pago")

    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    class Meta:
        ordering = ["-data_vencimento"]
        verbose_name = "Dívida"
        verbose_name_plural = "Dívidas"

    def __str__(self):
        return f"Dívida de {self.morador.usuario.username} - Akz{self.valor} ({'Paga' if self.pago else 'Em aberto'})"
