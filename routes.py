# This file is part of Nomerin Aitashy.
#
# Nomerin Aitashy is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# Nomerin Aitashy is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with Nomerin Aitashy. If not, see <https://www.gnu.org/licenses/>.

import flet as ft
from flet import icons

from main_tab_views import (
    About_Tab_View,
    Guide_Tab_View,
    Practice_Tab_View,
    Root_Tab_View,
    Settings_Tab_View,
)
from master_parts import Master_App_Bar, Master_Navigation_Bar
from text_controller import TextController


async def route_guide(page: ft.Page, navigation_bar: Master_Navigation_Bar):
    # TODO Better route management ex "/lesson1" -> "/guide/lesson1" and so on
    page.views.clear()
    page.views.append(
        Guide_Tab_View(navigation_bar, Master_App_Bar(TextController.get("guide_txt")))
    )


async def route_practice(page: ft.Page, navigation_bar: Master_Navigation_Bar):
    # TODO Better route management ex "/level1 " -> "/practice/level1" and so on
    page.views.clear()
    page.views.append(
        Practice_Tab_View(navigation_bar, Master_App_Bar(TextController.get("practice_txt")))
    )


async def route_about(page: ft.Page, navigation_bar: Master_Navigation_Bar):
    page.views.clear()
    page.views.append(
        About_Tab_View(navigation_bar, Master_App_Bar(TextController.get("about_txt")))
    )


async def route_setting(page: ft.Page, navigation_bar: Master_Navigation_Bar = None):
    page.views.append(
        Settings_Tab_View(
            navigation_bar, Master_App_Bar(TextController.get("settings_txt"), icons.SETTINGS)
        )
    )


async def route_root(page: ft.Page, navigation_bar: Master_Navigation_Bar):
    # TODO Don't apper root page if start button pressed by user
    page.views.clear()
    page.views.append(
        Root_Tab_View(navigation_bar, Master_App_Bar(TextController.get("welcome_txt")))
    )
