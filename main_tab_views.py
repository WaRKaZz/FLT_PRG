# This file is part of Nomerin Aitashy.
#
# Nomerin Aitashy is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# Nomerin Aitashy is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with Nomerin Aitashy. If not, see <https://www.gnu.org/licenses/>.

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
