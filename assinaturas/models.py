from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Assinatura(models.Model):
    TIPO_CHOICES = [
        ('gratuito', 'Gratuito'),
        ('pago', 'Pago'),
    ]

    STATUS_CHOICES = [
        ('ativa', 'Ativa'),
        ('cancelada', 'Cancelada'),
        ('vencida', 'Vencida'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assinaturas', null=True, blank=True)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='gratuito')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ativa')
    data_inicio = models.DateField(default=timezone.now)
    data_vencimento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Assinatura {self.tipo} - {self.usuario.username if self.usuario else 'Sem usuário'}"

    def esta_vencida(self):
        return self.data_vencimento < timezone.now().date()

    def atualizar_status(self):
        if self.esta_vencida():
            self.status = 'vencida'
            self.save()
        return self.status

    class Meta:
        verbose_name = 'Assinatura'
        verbose_name_plural = 'Assinaturas'
        ordering = ['-data_vencimento']