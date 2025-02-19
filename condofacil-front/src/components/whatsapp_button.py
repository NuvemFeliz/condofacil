import flet as ft
import os
from dotenv import load_dotenv

load_dotenv()

class WhatsAppButton(ft.Control):  # Herdar de Control
    def _get_control_name(self):
        return "whatsapp_button"  # Nome único em snake_case

    def build(self):
        return ft.Container(
            width=56,
            height=56,
            border_radius=56,
            bgcolor="#25D366",
            alignment=ft.alignment.center,
            content=ft.IconButton(
                icon=ft.Image(
                    src="assets/whatsapp-icon.svg",
                    width=32,
                    height=32,
                    color="white"
                ),
                on_click=self.open_whatsapp,
                style=ft.ButtonStyle(
                    padding=ft.padding.all(12),
                    overlay_color=ft.colors.TRANSPARENT
                )
            ),
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=8,
                color=ft.colors.BLACK54,
                offset=ft.Offset(0, 4)
            ),
            animate=ft.animation.Animation(300, ft.AnimationCurve.EASE_OUT),
            ink=True
        )

    def open_whatsapp(self, e):
        phone = os.getenv("WHATSAPP_NUMBER")
        url = f"https://wa.me/{phone}"
        e.page.launch_url(url)