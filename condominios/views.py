from django.shortcuts import render
from .models import Condominio

def listar_condominios(request):
    """
    View para listar todos os condomínios cadastrados.
    """
    condominios = Condominio.objects.all()  # Obtém todos os condomínios
    return render(request, 'condominios/listar.html', {'condominios': condominios})
