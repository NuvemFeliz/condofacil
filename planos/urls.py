from django.urls import path
from . import views

urlpatterns = [
    path('planos/', views.listar_planos, name='listar_planos'),
    path('planos/criar/', views.criar_plano, name='criar_plano'),
    path('assinaturas/criar/', views.criar_assinatura, name='criar_assinatura'),
    path('assinaturas/<int:condominio_id>/', views.listar_assinaturas, name='listar_assinaturas'),
    path('assinaturas/atualizar/<int:assinatura_id>/', views.atualizar_assinatura, name='atualizar_assinatura'),
    path('assinaturas/cancelar/<int:assinatura_id>/', views.cancelar_assinatura, name='cancelar_assinatura'),
]