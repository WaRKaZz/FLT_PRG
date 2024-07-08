from typing import TYPE_CHECKING
from os.path import join

from flet import (
    Audio,
    DataCell,
    DataColumn,
    DataRow,
    DataTable,
    ElevatedButton,
    Text,
    icons,
)

from master_parts import ContentView, MasterNavigationBar

if TYPE_CHECKING:
    from flet import AppBar

    from controller import TextController


class LessonZeroView(ContentView):
    def __init__(
        self,
        text_controller: "TextController",
        navigation_bar: "MasterNavigationBar",
        app_bar: "AppBar",
    ):
        super().__init__(
            text_controller=text_controller,
            navigation_bar=navigation_bar,
            app_bar=app_bar,
            number=0,
            view_type="lesson",
        )
        cyrillic = [
            "нөл",
            "бір",
            "екі",
            "үш",
            "төрт",
            "бес",
            "алты",
            "жеті",
            "сегіз",
            "тоғыз",
        ]
        latin = [
            "nöl",
            "bir",
            "eki",
            "üş",
            "tört",
            "bes",
            "alty",
            "jeti",
            "segiz",
            "toğyz",
        ]

        columns = [
            DataColumn(Text(text_controller.get("digit_txt"))),
            DataColumn(Text(text_controller.get("cyrillic_txt"))),
            DataColumn(Text(text_controller.get("latin_txt"))),
        ]
        rows = [
            DataRow(
                cells=[
                    DataCell(
                        ElevatedButton(
                            text=str(i),
                            icon=icons.PLAY_ARROW,
                            width=70,
                            height=40,
                            data=i,
                            on_click=self._playsound,
                        )
                    ),
                    DataCell(Text(cyrillic[i])),
                    DataCell(Text(latin[i])),
                ]
            )
            for i in range(10)
        ]
        title = Text(text_controller.get("lesson0_title"))
        examples = Text(
            text_controller.get("lesson0_examples"),
        )
        self.number = 0
        self.route = "/guide/0"
        self.controls = [title, DataTable(columns=columns, rows=rows), examples]
        self.expand = True

    def _playsound(self, e):
        if e.page.client_storage.contains_key("settings_voice"):
            self.voice = e.page.client_storage.get("settings_voice")
        audio_src = join(self._get_voice_location(self.voice), f"{e.control.data}.mp3")
        print(audio_src)
        audio = Audio(
            src=audio_src,
            autoplay=True,
        )
        e.page.overlay.append(audio)
        e.page.update()
        e.page.overlay.remove(audio)

    def _open(self, e):
        e.page.go("/guide/0")
