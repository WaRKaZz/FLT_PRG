# This file is part of Nomerin Aitashy.
#
# Nomerin Aitashy is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# Nomerin Aitashy is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with Nomerin Aitashy. If not, see <https://www.gnu.org/licenses/>.

from typing import TYPE_CHECKING

import flet as ft

if TYPE_CHECKING:
    from flet import AppBar
    from controller import TextController
    from master_parts import MasterNavigationBar

from master_parts import MasterSelectorContainer, MasterTabView


class GuideTabView(MasterTabView):
    def __init__(
        self,
        text_controller: "TextController",
        navigation_bar: "MasterNavigationBar",
        lessons: list,
        app_bar: "AppBar",
    ):
        super().__init__(app_bar=app_bar, navigation_bar=navigation_bar)
        self.route = "/guide"
        self.controls = [
            ft.ResponsiveRow(
                (lessons[i].container for i in range(len(lessons))),
            ),
        ]
        self.expand = True


class PracticeTabView(MasterTabView):
    def __init__(
        self,
        text_controller: "TextController",
        navigation_bar: "MasterNavigationBar",
        app_bar: "AppBar",
    ):
        super().__init__(app_bar=app_bar, navigation_bar=navigation_bar)
        self.route = "/practice"


class AboutTabView(MasterTabView):
    def __init__(
        self,
        text_controller: "TextController",
        navigation_bar: "MasterNavigationBar",
        app_bar: "AppBar",
    ):
        super().__init__(app_bar=app_bar, navigation_bar=navigation_bar)
        self.route = "/about"


class SettingsTabView(MasterTabView):
    def __init__(
        self,
        text_controller: "TextController",
        navigation_bar: "MasterNavigationBar",
        app_bar: "AppBar",
    ):
        super().__init__(app_bar=app_bar, navigation_bar=navigation_bar)
        self.route = "/settings"


class RootTabView(MasterTabView):
    def __init__(
        self,
        text_controller: "TextController",
        app_bar: "AppBar" = None,
    ):
        super().__init__(app_bar=app_bar)
        self.route = "/"
        self.scroll = None
        self.vertical_alignment = "center"
        self.horizontal_alignment = "center"
        self.controls = [
            ft.Text(
                value=text_controller.get("welcome_message_txt"),
                size=17,
                text_align=ft.TextAlign.CENTER,
            ),
            ft.ElevatedButton(
                content=ft.Text(text_controller.get("start_txt"), size=25),
                on_click=self.start,
            ),
        ]

    async def start(self, e):
        e.page.go("/practice")
