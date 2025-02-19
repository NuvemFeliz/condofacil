from django.db import models
from django.core.exceptions import ValidationError
from auth_custom.models import User  # Importe o modelo de usuário personalizado

# Opções para o campo "provincia" (apenas para Angola)
PROVINCIA_CHOICES = [
    ('Bengo', 'Bengo'),
    ('Cuanza-Norte', 'Cuanza-Norte'),
    ('Cuanza-Sul', 'Cuanza-Sul'),
    ('Huambo', 'Huambo'),
    ('Bié', 'Bié'),
    ('Moxico', 'Moxico'),
    ('Moxico-Leste', 'Moxico-Leste'),
    ('Lunda-Norte', 'Lunda-Norte'),
    ('Lunda-Sul', 'Lunda-Sul'),
    ('Ecolo e Bengo', 'Ecolo e Bengo'),
    ('Huíla', 'Huíla'),
    ('Cunene', 'Cunene'),
    ('Cabinda', 'Cabinda'),
    ('Zaire', 'Zaire'),
    ('Uíge', 'Uíge'),
    ('Malanje', 'Malanje'),
    ('Cuando', 'Cuando'),
    ('Cubango', 'Cubango'),
    ('Luanda', 'Luanda'),
]

# Opções para o campo "pais" (países da CPLP)
PAIS_CHOICES = [
    ('Angola', 'Angola'),
    ('Brasil', 'Brasil'),
    ('Cabo Verde', 'Cabo Verde'),
    ('Guiné-Bissau', 'Guiné-Bissau'),
    ('Guiné Equatorial', 'Guiné Equatorial'),
    ('Moçambique', 'Moçambique'),
    ('Portugal', 'Portugal'),
    ('São Tomé e Príncipe', 'São Tomé e Príncipe'),
    ('Timor-Leste', 'Timor-Leste'),
]

# Opções para o campo "tipo_condominio"
TIPO_CONDOMINIO_CHOICES = [
    ('predio', 'Prédio'),
    ('vivenda', 'Vivenda'),
]

class Condominio(models.Model):
    nome = models.CharField(
        max_length=100,
        verbose_name="Nome do Condomínio",
        help_text="Nome completo do condomínio."
    )
    endereco = models.CharField(
        max_length=200,
        verbose_name="Endereço",
        help_text="Endereço completo do condomínio."
    )
    provincia = models.CharField(
        max_length=50,
        choices=PROVINCIA_CHOICES,
        default='Luanda',
        blank=True,
        null=True,
        verbose_name="Província",
        help_text="Província onde o condomínio está localizado (apenas para Angola)."
    )
    estado = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Estado/Província",
        help_text="Estado ou província onde o condomínio está localizado (para países fora de Angola)."
    )
    nif = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="NIF",
        help_text="Número de Identificação Fiscal do condomínio."
    )
    pais = models.CharField(
        max_length=50,
        choices=PAIS_CHOICES,
        default='Angola',
        verbose_name="País",
        help_text="País onde o condomínio está localizado."
    )
    data_cadastro = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de Cadastro",
        help_text="Data e hora em que o condomínio foi cadastrado."
    )
    tipo_condominio = models.CharField(
        max_length=10,
        choices=TIPO_CONDOMINIO_CHOICES,
        default='predio',
        verbose_name="Tipo de Condomínio",
        help_text="Tipo de condomínio (Prédio ou Vivenda)."
    )
    numero_andares = models.IntegerField(
        verbose_name="Número de Andares",
        help_text="Número total de andares do condomínio (apenas para prédios).",
        blank=True,
        null=True,
    )
    numero_apartamentos = models.IntegerField(
        verbose_name="Número de Apartamentos",
        help_text="Número total de apartamentos no condomínio (apenas para prédios).",
        blank=True,
        null=True,
    )
    numero_vivendas = models.IntegerField(
        verbose_name="Número de Vivendas",
        help_text="Número total de vivendas no condomínio (apenas para condomínios de vivendas).",
        blank=True,
        null=True,
    )
    logo = models.ImageField(
        upload_to='condominios/logos/',
        blank=True,
        null=True,
        verbose_name="Logo",
        help_text="Logo do condomínio."
    )
    proprietario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='condominios',
        verbose_name="Proprietário",
        help_text="Proprietário responsável pelo condomínio."
    )

    def __str__(self):
        return self.nome

    def clean(self):
        """
        Validação personalizada para garantir que:
        - Se o país for Angola, o campo "provincia" é obrigatório e "estado" deve ser nulo.
        - Se o país não for Angola, o campo "estado" é obrigatório e "provincia" deve ser nulo.
        - Se o tipo de condomínio for "predio", os campos "numero_andares" e "numero_apartamentos" são obrigatórios.
        - Se o tipo de condomínio for "vivenda", o campo "numero_vivendas" é obrigatório.
        """
        super().clean()
        
        # Validação de país e província/estado
        if self.pais == 'Angola':
            if not self.provincia:
                raise ValidationError({"provincia": "O campo 'Província' é obrigatório para Angola."})
            self.estado = None  # Garante que o campo "estado" seja nulo
        else:
            if not self.estado:
                raise ValidationError({"estado": "O campo 'Estado/Província' é obrigatório para países fora de Angola."})
            self.provincia = None  # Garante que o campo "provincia" seja nulo

        # Validação de tipo de condomínio
        if self.tipo_condominio == 'predio':
            if not self.numero_andares:
                raise ValidationError({"numero_andares": "O campo 'Número de Andares' é obrigatório para prédios."})
            if not self.numero_apartamentos:
                raise ValidationError({"numero_apartamentos": "O campo 'Número de Apartamentos' é obrigatório para prédios."})
            self.numero_vivendas = None  # Garante que o campo "numero_vivendas" seja nulo
        elif self.tipo_condominio == 'vivenda':
            if not self.numero_vivendas:
                raise ValidationError({"numero_vivendas": "O campo 'Número de Vivendas' é obrigatório para condomínios de vivendas."})
            self.numero_andares = None  # Garante que o campo "numero_andares" seja nulo
            self.numero_apartamentos = None  # Garante que o campo "numero_apartamentos" seja nulo

    class Meta:
        verbose_name = "Condomínio"
        verbose_name_plural = "Condomínios"