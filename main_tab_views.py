import flet as ft

from master_parts import Master_Tab_View
from text_controller import start_txt, welcome_message_txt


class Guide_Tab_View(Master_Tab_View):
    def __init__(self, navigation_bar, app_bar):
        super().__init__(navigation_bar, app_bar)
        self.route = "/guide"


class Practice_Tab_View(Master_Tab_View):
    def __init__(self, navigation_bar, app_bar):
        super().__init__(navigation_bar, app_bar)
        self.route = "/practice"


class About_Tab_View(Master_Tab_View):
    def __init__(self, navigation_bar, app_bar):
        super().__init__(navigation_bar, app_bar)
        self.route = "/about"


class Settings_Tab_View(Master_Tab_View):
    def __init__(self, navigation_bar, app_bar):
        super().__init__(navigation_bar, app_bar)
        self.route = "/settings"


class Root_Tab_View(Master_Tab_View):
    def __init__(self, navigation_bar, app_bar):
        super().__init__(navigation_bar, app_bar)
        self.route = "/"
        self.vertical_alignment = "center"
        self.horizontal_alignment = "center"
        self.controls = [
            ft.Text(
                value=welcome_message_txt,
                size=17,
                text_align=ft.TextAlign.CENTER,
            ),
            ft.ElevatedButton(
                content=ft.Text(start_txt, size=25),
                on_click=self.start,
            ),
        ]

    def start(self, e):
        self.page.go("/practice")
