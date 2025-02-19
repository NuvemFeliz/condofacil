from django.shortcuts import render

def planos_view(request):
    return render(request, "planos/planos.html")  # Renderiza o arquivo templates/planos.html
