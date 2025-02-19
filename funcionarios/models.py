from django.db import models
from condominios.models import Condominio
from auth_custom.models import User

class Cargo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Cargo")
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    # Opções para Tipo de Contratação
    TC = "TC"
    PJ = "PJ"
    ESTAGIO = "Estágio"
    INDETERMINADO = "Tempo Indeterminado"
    TEMPORARIO = "Temporário"

    TIPOS_CONTRATACAO = [
        (TC, "TC (Termo Certo)"),
        (PJ, "Pessoa Jurídica (PJ)"),
        (ESTAGIO, "Estágio"),
        (INDETERMINADO, "Tempo Indeterminado"),
        (TEMPORARIO, "Temporário"),
    ]

    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name="funcionarios")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="funcionarios")
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name="funcionarios")

    # Novo campo: Tipo de Contratação
    tipo_contratacao = models.CharField(
        max_length=20,
        choices=TIPOS_CONTRATACAO,
        default=TC,
        verbose_name="Tipo de Contratação"
    )

    salario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Salário")
    data_contratacao = models.DateField(verbose_name="Data de Contratação")
    horas_extras = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="Horas Extras")
    vales = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Vales")
    remuneracao_adicional = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Remuneração Adicional")

    def __str__(self):
        return f"{self.usuario.username} - {self.cargo.nome} ({self.tipo_contratacao})"
