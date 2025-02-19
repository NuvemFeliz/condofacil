from django.urls import path
from ninja import NinjaAPI
from .api import router as assinaturas_router

# Cria a API principal
api = NinjaAPI()

# Registra o router das assinaturas na API
api.add_router("/assinaturas/", assinaturas_router)

urlpatterns = [
    path("api/", api.urls),  # Endpoint principal da API
]