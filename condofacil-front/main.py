import flet as ft
from src.pages.landing import LandingPage
from src.components.whatsapp_button import WhatsAppButton
from src.components.chat_bubble import ChatBubble

def main(page: ft.Page):
    page.title = "Condofácil - Gestão Condominial Inteligente"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.fonts = {
        "Poppins": "fonts/Poppins-Regular.ttf",
        "Poppins-Bold": "fonts/Poppins-Bold.ttf"
    }
    page.bgcolor = "#F8FAFC"
    
    # Configuração responsiva
    page.window_min_width = 360
    page.window_min_height = 640
    
    # Componentes fixos
    page.overlay.extend([
        WhatsAppButton(),
        ChatBubble()
    ])
    
    # Navegação
    landing = LandingPage()
    page.add(landing)

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)