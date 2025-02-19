from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI
from django.views.generic import TemplateView  # Para páginas HTML simples

# Importação das Views para renderizar HTML
from dashboard.views import dashboard_view
from planos.views import planos_view
from auth_custom.views import login_view

# Importação dos Routers de API
from auth_custom.api import router as auth_router
from condominios.api import router as condominio_router
from financeiro.api import router as financeiro_router
from ocorrencias.api import router as ocorrencias_router
from funcionarios.api import router as funcionarios_router
from moradores.api import router as moradores_router
from reservas.api import router as reservas_router
from planos.api import router as planos_router
from assinaturas.api import router as assinaturas_router

# Criando a API apenas uma vez
class SingletonAPI:
    _instance = None

    @staticmethod
    def get_instance():
        if SingletonAPI._instance is None:
            print("Criando a instância única da API Condofácil...")
            SingletonAPI._instance = NinjaAPI(
                title="Condofácil API",
                version="1.0.0",
                description="API para sistema de gestão de condomínios.",
            )

            # Adicionando as rotas da API
            SingletonAPI._instance.add_router("/auth/", auth_router, tags=["Autenticação"])
            SingletonAPI._instance.add_router("/condominio/", condominio_router, tags=["Condomínios"])
            SingletonAPI._instance.add_router("/financeiro/", financeiro_router, tags=["Financeiro"])
            SingletonAPI._instance.add_router("/ocorrencias/", ocorrencias_router, tags=["Ocorrências"])
            SingletonAPI._instance.add_router("/funcionarios/", funcionarios_router, tags=["Funcionários"])
            SingletonAPI._instance.add_router("/moradores/", moradores_router, tags=["Moradores"])
            SingletonAPI._instance.add_router("/reservas/", reservas_router, tags=["Reservas"])
            SingletonAPI._instance.add_router("/planos/", planos_router, tags=["Planos"])
            SingletonAPI._instance.add_router("/assinaturas/", assinaturas_router, tags=["Assinaturas"])

        return SingletonAPI._instance

# Obtendo a instância única da API
api = SingletonAPI.get_instance()

# Definição das Rotas Principais
urlpatterns = [
    path("admin/", admin.site.urls),  # Painel Admin
    path("api/", api.urls),  # API do Django Ninja
    
]

