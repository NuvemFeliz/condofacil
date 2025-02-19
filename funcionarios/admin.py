from django.contrib import admin
from .models import Cargo, Funcionario

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao")
    search_fields = ("nome",)

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ("usuario", "condominio", "cargo", "salario", "data_contratacao")
    search_fields = ("usuario__username", "condominio__nome", "cargo__nome")
    list_filter = ("cargo", "condominio")