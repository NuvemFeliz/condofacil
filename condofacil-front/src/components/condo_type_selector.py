import flet as ft

class CondoTypeSelector(ft.Control):  # Herdar de Control
    def _get_control_name(self):
        return "condo_type_selector"  # Nome único em snake_case

    def build(self):
        return ft.Tabs(
            selected_index=0,
            on_change=self.on_tab_change,
            tabs=[
                ft.Tab(
                    text="Edifício Alto",
                    icon=ft.icons.APARTMENT,
                    content=ft.Container(
                        padding=ft.padding.all(20),
                        content=ft.Column([
                            ft.Text("Número de Andares"),
                            ft.Slider(
                                min=15,
                                max=50,
                                divisions=35,
                                label="{value} andares",
                                on_change=self.on_slider_change
                            )
                        ])
                    )
                ),
                ft.Tab(
                    text="Moradia Isolada",
                    icon=ft.icons.HOUSE,
                    content=ft.Container(
                        padding=ft.padding.all(20),
                        content=ft.Column([
                            ft.Text("Configuração para casas isoladas"),
                            ft.Text("Aqui você pode configurar moradias isoladas.")
                        ])
                    )
                )
            ]
        )

    def on_tab_change(self, e):
        print(f"Tab selecionada: {self.tabs[e.control.selected_index].text}")

    def on_slider_change(self, e):
        print(f"Valor do slider: {e.control.value}")