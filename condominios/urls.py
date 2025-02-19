from django.urls import path
from .views import listar_condominios

urlpatterns = [
    path('listar/', listar_condominios, name='listar_condominios'),
]