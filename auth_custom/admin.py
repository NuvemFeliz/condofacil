from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "is_proprietario", "is_morador", "is_funcionario")
    search_fields = ("username", "email")
    list_filter = ("is_proprietario", "is_morador", "is_funcionario")

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "foto_perfil", "endereco")
    search_fields = ("user__username", "endereco")