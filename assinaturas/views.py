from django.shortcuts import render
from .models import Assinatura

def listar_assinaturas(request):
    assinaturas = Assinatura.objects.all()
    return render(request, 'assinaturas/listar.html', {'assinaturas': assinaturas})
