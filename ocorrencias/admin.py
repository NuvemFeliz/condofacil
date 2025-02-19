from django.contrib import admin
from .models import TipoOcorrencia, Ocorrencia, Comunicado

@admin.register(TipoOcorrencia)
class TipoOcorrenciaAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao")
    search_fields = ("nome",)

@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ("condominio", "tipo", "descricao", "data", "resolvido")
    search_fields = ("condominio__nome", "tipo__nome", "descricao")
    list_filter = ("tipo", "condominio", "resolvido")

@admin.register(Comunicado)
class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ("condominio", "titulo", "data", "usuario")
    search_fields = ("condominio__nome", "titulo", "usuario__username")
    list_filter = ("condominio",)