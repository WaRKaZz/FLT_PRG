from os import getcwd
from typing import TYPE_CHECKING

from master_parts import MasterSelectorContainer, MasterTabView

if TYPE_CHECKING:
    from flet import AppBar

    from controller import TextController
    from master_parts import MasterNavigationBar


class LessonView(MasterTabView):
    def __init__(
        self,
        text_controller: "TextController",
        navigation_bar: "MasterNavigationBar",
        app_bar: "AppBar",
        number: int,
    ):
        super().__init__(navigation_bar, app_bar)
        self.voice = "aigul"
        self.number = None

        self.container = MasterSelectorContainer(
            text_controller.get(f"lesson{str(number)}_upper_text"),
            text_controller.get(f"lesson{str(number)}_lower_text"),
            self._open,
        )

    def _get_voice_location(self, voice):
        root = getcwd()
        if voice == "aigul":
            return root + "\\resources\\voice_aigul"
        elif voice == "siri":
            return root + "\\resources\\voice_siri"
        else:
            return root + "\\resources\\voice_aigul"
