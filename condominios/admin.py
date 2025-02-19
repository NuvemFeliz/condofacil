from django.contrib import admin
from .models import Condominio

# Importação segura de UnidadeHabitacional para evitar erro
try:
    from .models import UnidadeHabitacional
except ImportError:
    UnidadeHabitacional = None  # Evita erro caso o modelo ainda não esteja carregado

@admin.register(Condominio)
class CondominioAdmin(admin.ModelAdmin):
    list_display = ("nome", "endereco", "pais", "data_cadastro")  # Certifique-se de que esses campos existem no modelo
    search_fields = ("nome", "endereco")
    list_filter = ("pais", "data_cadastro")

# Registra UnidadeHabitacional apenas se a importação for bem-sucedida
if UnidadeHabitacional:
    @admin.register(UnidadeHabitacional)
    class UnidadeHabitacionalAdmin(admin.ModelAdmin):
        list_display = ("numero", "bloco", "condominio")
        search_fields = ("numero", "bloco", "condominio__nome")
        list_filter = ("condominio",)
