from django.urls import path
from ninja import NinjaAPI
from .api import auth_router
from . import views  # Importe as views do seu app

# Cria a instância da API
api = NinjaAPI(title="Condofácil API", version="1.0.0")

# Adiciona o roteador apenas uma vez
api.add_router("/auth/", auth_router)

# Configura as URLs
urlpatterns = [
    # URLs tradicionais do Django
    path('', views.login_view, name='login'),  # Rota para a página de login
    path('signup/', views.signup_view, name='signup'),  # Rota para a página de cadastro
    path('logout/', views.logout_view, name='logout'),  # Rota para logout

    # URLs da API
    path('api/', api.urls),  # Inclui as URLs da API
]