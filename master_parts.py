# This file is part of Nomerin Aitashy.
#
# Nomerin Aitashy is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# Nomerin Aitashy is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with Nomerin Aitashy. If not, see <https://www.gnu.org/licenses/>.


from os import getcwd, path
from typing import TYPE_CHECKING

import flet as ft
from flet import (
    AppBar,
    Audio,
    Container,
    NavigationBar,
    NavigationBarDestination,
    NavigationBarLabelBehavior,
    Text,
    View,
    icons,
)

if TYPE_CHECKING:
    from controller import TextController


# class MasterAppBar(AppBar):
#     def __init__(self, text, icon=icons.SETTINGS_OUTLINED):
#         super().__init__()
#         self.title = Text(text)
#         self.actions = [IconButton(icon=icon, on_click=self.goto_settings)]

#     async def goto_settings(self, e):
#         if e.page.route != "/settings":
#             e.page.go("/settings")
#         else:
#             e.page.views.pop()
#             e.page.go(e.page.views[-1].route)


class MasterTabView(View):
    """
    Initializes a Master_View object.

    Args:
        navigation_bar: NavigationBar object for the view.
        app_bar: AppBar object for the view.
    """

    def __init__(
        self,
        app_bar: AppBar = None,
        navigation_bar: "NavigationBar" = None,
    ):
        super().__init__()
        self.scroll = ft.ScrollMode.AUTO
        self.appbar = app_bar
        self.navigation_bar = navigation_bar


class ContentView(MasterTabView):
    def __init__(
        self,
        text_controller: "TextController",
        navigation_bar: "MasterNavigationBar",
        app_bar: "AppBar",
        number: int,
        view_type: str,
        voice: str = "aigul",
    ):
        super().__init__(navigation_bar, app_bar)

        self.voice = voice
        self.container = MasterSelectorContainer(
            text_controller.get(f"{view_type}{str(number)}_upper_text"),
            text_controller.get(f"{view_type}{str(number)}_lower_text"),
            self._open,
        )

    def _get_voice_location(self, voice):
        if voice == "aigul":
            return path.join(getcwd(), "assets", "voice_aigul")
        elif voice == "siri":
            return path.join(getcwd(), "assets", "voice_siri")
        else:
            return path.join(getcwd(), "assets", "voice_aigul")

    def button_sound_handler(self, e):
        numbers = str(e.control.data).split(" ")
        print("im here")
        self._playsound(numbers, e)

    def _playsound(self, numbers, e):
        voice_path = self._get_voice_location(self.voice)

        def play_next_audio(index):
            if index < len(numbers):
                audio = Audio(
                    src=path.join(voice_path, f"{numbers[index]}.mp3"),
                    autoplay=True,
                    on_state_changed=lambda event: on_audio_state_changed(event, index),
                )
                e.page.overlay.append(audio)
                e.page.update()
            else:
                e.page.overlay.clear()
                e.page.update()

        def on_audio_state_changed(event, index):
            if event.data == "completed":
                e.page.overlay.clear()
                play_next_audio(index + 1)

        play_next_audio(0)


class MasterSelectorContainer(Container):
    def __init__(self, upper_text, lower_text, action):
        super().__init__()
        self.column1 = ft.Column(
            [
                ft.Text(upper_text, theme_style=ft.TextThemeStyle.TITLE_LARGE),
                ft.Text(lower_text),
            ],
            alignment=ft.alignment.center_left,
            width=80,
            col={"xs": 10, "sm": 10, "md": 10, "xl": 9},
        )
        self.column2 = ft.Column(
            [
                ft.IconButton(
                    adaptive=True,
                    icon=ft.icons.ARROW_FORWARD,
                    on_click=action,
                    alignment=ft.alignment.center,
                )
            ],
            width=20,
            col={"xs": 2, "sm": 2, "md": 2, "xl": 3},
            alignment=ft.alignment.center_right,
        )
        self.padding = 20
        self.border_radius = 10
        # self.ink = True
        self.border = ft.border.all(1, ft.colors.BLACK)
        self.width = 100
        self.content = ft.ResponsiveRow([self.column1, self.column2])
        self.col = {"sm": 6, "md": 4, "xl": 4}


class MasterNavigationBar(NavigationBar):
    def __init__(self, text_controller: "TextController"):
        super().__init__()
        self.adaptive = True
        self.label_behavior = NavigationBarLabelBehavior.ONLY_SHOW_SELECTED
        self.on_change = self.select_tab
        self.selected_index = 1
        self.destinations = [
            NavigationBarDestination(
                icon=icons.BOOK_OUTLINED,
                selected_icon=icons.BOOK,
                label=text_controller.get("guide_txt"),
            ),
            NavigationBarDestination(
                icon=icons.MENU,
                selected_icon=icons.MENU_OPEN,
                label=text_controller.get("practice_txt"),
            ),
            NavigationBarDestination(
                icon=icons.SETTINGS,
                selected_icon=icons.INFO,
                label=text_controller.get("settings_txt"),
            ),
        ]

    async def select_tab(self, e):
        assert e is not None
        assert e.control is not None
        assert e.page is not None

        selected_index = e.control.selected_index

        if selected_index == 0:
            e.page.route = "/guide"
        elif selected_index == 1:
            e.page.route = "/practice"
        elif selected_index == 2:
            e.page.route = "/about"
        else:
            raise ValueError(f"Unexpected selected_index: {selected_index}")

        e.page.update()
