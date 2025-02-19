import flet as ft
from src.components.condo_type_selector import CondoTypeSelector

class LandingPage(ft.Column):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.alignment = ft.MainAxisAlignment.CENTER
        self.controls = [
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        "Gestão Condominial para Todas as Arquiteturas",
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        font_family="Poppins-Bold",
                        text_align=ft.TextAlign.CENTER,
                        color="#1E293B"
                    ),
                    ft.Text(
                        "Do arranha-céu à casa isolada - controle completo em tempo real",
                        size=20,
                        color="#64748B",
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Divider(height=40, color="transparent"),
                    CondoTypeSelector(),
                    ft.ElevatedButton(
                        "Iniciar Teste Gratuito",
                        icon=ft.icons.ROCKET_LAUNCH,
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor="#2563EB",
                            color="white"
                        ),
                        on_click=lambda e: e.page.go("/signup")
                    )
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=ft.padding.symmetric(horizontal=20)
            )
        ]