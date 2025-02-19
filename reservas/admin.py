from django.contrib import admin
from .models import EspacoComum, Reserva

@admin.register(EspacoComum)
class EspacoComumAdmin(admin.ModelAdmin):
    list_display = ("nome", "condominio", "capacidade", "valor_reserva")
    search_fields = ("nome", "condominio__nome")
    list_filter = ("condominio",)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("espaco", "morador", "data_reserva", "valor_pago", "status")
    search_fields = ("espaco__nome", "morador__username")
    list_filter = ("status", "espaco__condominio")