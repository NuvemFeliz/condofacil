from django.contrib import admin
from .models import TipoTransacao, Transacao, Despesa

@admin.register(TipoTransacao)
class TipoTransacaoAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao")
    search_fields = ("nome",)

@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = ("condominio", "tipo", "valor", "data", "usuario")
    search_fields = ("condominio__nome", "tipo__nome", "usuario__username")
    list_filter = ("tipo", "condominio")

@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ("condominio", "descricao", "valor", "data", "categoria")
    search_fields = ("condominio__nome", "descricao", "categoria")
    list_filter = ("categoria", "condominio")