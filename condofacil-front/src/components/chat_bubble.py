import flet as ft

class ChatBubble(ft.Control):  # Herdar de UserControl
    def __init__(self):
        super().__init__()
        self.chat_open = False
        self.chat_content = ft.ListView(expand=True)
        self.message_field = ft.TextField(
            hint_text="Digite sua mensagem...",
            on_submit=self.send_message
        )

    def build(self):
        return ft.Stack(
            controls=[
                ft.FloatingActionButton(
                    icon=ft.icons.CHAT_BUBBLE_OUTLINE,
                    bgcolor="#2563EB",
                    on_click=self.toggle_chat,
                    animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE_OUT)
                ),
                ft.Container(
                    visible=self.chat_open,
                    animate_opacity=ft.animation.Animation(200),
                    content=ft.Card(
                        width=300,
                        height=400,
                        elevation=8,
                        content=ft.Column([
                            ft.ListTile(
                                title=ft.Text("Assistente Virtual", weight="bold"),
                                leading=ft.Icon(ft.icons.SUPPORT_AGENT)
                            ),
                            ft.Divider(height=1),
                            self.chat_content,
                            ft.Row([self.message_field], alignment="end")
                        ])
                    )
                )
            ]
        )

    def toggle_chat(self, e):
        self.chat_open = not self.chat_open
        self.update()

    def send_message(self, e):
        if self.message_field.value:
            self.chat_content.controls.append(
                ft.ListTile(
                    title=ft.Text(self.message_field.value),
                    leading=ft.Icon(ft.icons.PERSON)
                )
            )
            self.message_field.value = ""
            self.chat_content.update()
            self.message_field.focus()