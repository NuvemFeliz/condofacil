from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_proprietario = models.BooleanField(default=False)
    is_morador = models.BooleanField(default=False)
    is_funcionario = models.BooleanField(default=False)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    nif = models.CharField(max_length=14, unique=True, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)

    # Defina related_name exclusivos para evitar conflitos
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='auth_custom_user_set',  # Nome exclusivo
        related_query_name='auth_custom_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='auth_custom_user_set',  # Nome exclusivo
        related_query_name='auth_custom_user',
    )

    def __str__(self):
        return self.username

    class Meta:
        app_label = 'auth_custom'  # Define o app_label para o modelo

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'
