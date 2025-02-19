from django.urls import path
from . import views  # Importa o módulo views dentro do mesmo app

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Define a rota para a view "dashboard"
]
