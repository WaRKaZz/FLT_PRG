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
from text_controller import (
    about_txt,
    guide_txt,
    practice_txt,
    settings_txt,
    welcome_txt,
)


def route_guide(page: ft.Page, navigation_bar: Master_Navigation_Bar):
    # TODO Better route management ex "/lesson1" -> "/guide/lesson1" and so on
    page.views.clear()
    page.views.append(Guide_Tab_View(navigation_bar, Master_App_Bar(guide_txt)))


def route_practice(page: ft.Page, navigation_bar: Master_Navigation_Bar):
    # TODO Better route management ex "/level1 " -> "/practice/level1" and so on
    page.views.clear()
    page.views.append(Practice_Tab_View(navigation_bar, Master_App_Bar(practice_txt)))


def route_about(page: ft.Page, navigation_bar: Master_Navigation_Bar):
    page.views.clear()
    page.views.append(About_Tab_View(navigation_bar, Master_App_Bar(about_txt)))


def route_setting(page: ft.Page, navigation_bar: Master_Navigation_Bar = None):
    page.views.append(
        Settings_Tab_View(navigation_bar, Master_App_Bar(settings_txt, icons.SETTINGS))
    )


def route_root(page: ft.Page, navigation_bar: Master_Navigation_Bar):
    # TODO Don't apper root page if start button pressed by user
    page.views.clear()
    page.views.append(Root_Tab_View(navigation_bar, Master_App_Bar(welcome_txt)))
