from django.contrib import admin
from .models import Morador,UnidadeHabitacional

@admin.register(Morador)
class MoradorAdmin(admin.ModelAdmin):
    list_display = ("usuario", "condominio", "unidade", "status", "data_cadastro")
    search_fields = ("usuario__username", "condominio__nome", "unidade__numero")
    list_filter = ("status", "condominio")
    
@admin.register(UnidadeHabitacional)
class UnidadeHabitacionalAdmin(admin.ModelAdmin):
    list_display = ("numero", "bloco", "condominio")  # Campos corretos do modelo UnidadeHabitacional
    search_fields = ("numero", "bloco", "condominio__nome")
    list_filter = ("condominio",)  # Filtro por condomínio