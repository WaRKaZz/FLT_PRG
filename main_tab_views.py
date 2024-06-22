import flet as ft

from master_parts import Master_Selector_Container, Master_Tab_View
from text_controller import start_txt, welcome_message_txt


class Guide_Tab_View(Master_Tab_View):
    def __init__(self, navigation_bar, app_bar):
        super().__init__(navigation_bar, app_bar)
        self.route = "/guide"
        self.controls = [
            ft.ResponsiveRow(
                [
                    # Temp for testing will be replaced with view manager
                    Master_Selector_Container("hello", "world", None),
                    Master_Selector_Container("goodbye", "world", None),
                    Master_Selector_Container("hello", "world", None),
                    Master_Selector_Container("goodbye", "world", None),
                    Master_Selector_Container("hello", "world", None),
                    Master_Selector_Container("goodbye", "world", None),
                    Master_Selector_Container("hello", "world", None),
                    Master_Selector_Container("goodbye", "world", None),
                    Master_Selector_Container("hello", "world", None),
                    Master_Selector_Container("goodbye", "world", None),
                    Master_Selector_Container("hello", "world", None),
                ],
            ),
        ]
        self.expand = True


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
        self.scroll = None
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

    async def start(self, e):
        self.page.go("/practice")
