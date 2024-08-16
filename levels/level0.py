import asyncio
import random
from typing import TYPE_CHECKING

from flet import (
    Audio,
    Column,
    CrossAxisAlignment,
    ElevatedButton,
    IconButton,
    MainAxisAlignment,
    Row,
    Text,
    icons,
)

from master_parts import ContentView, MasterNavigationBar

if TYPE_CHECKING:
    from flet import AppBar

    from controller import TextController


class LevelZeroView(ContentView):
    def __init__(
        self,
        text_controller: "TextController",
        navigation_bar: "MasterNavigationBar",
        app_bar: "AppBar",
        voice: str,
    ):
        super().__init__(
            text_controller=text_controller,
            navigation_bar=navigation_bar,
            app_bar=app_bar,
            number=0,
            view_type="level",
            voice=voice,
        )
        self.current_digit = random.randint(0, 9)
        self.text_controller = text_controller
        self.feedback_text = Text(size=20, text_align="center")
        self.feedback_text.value = text_controller.get("level0_number_await")
        self.sound_button = IconButton(
            icon=icons.VOLUME_UP,
            icon_size=24,
            width=280,
            height=50,
            data=self.current_digit,
            on_click=self.button_sound_handler,
        )
        self.keyboard = self.create_keyboard()
        content = Column(
            [self.feedback_text, self.sound_button, self.keyboard],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=20,
        )
        self.number = 0
        self.route = "/level/0"
        self.controls = [content]
        self.expand = False

    def create_keyboard(self):
        def create_number_button(number):
            return ElevatedButton(
                text=str(number),
                width=80,
                height=50,
                data=str(number),
                on_click=self.button_clicked,
            )

        return Column(
            [
                Row(
                    [create_number_button(i) for i in range(7, 10)],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row(
                    [create_number_button(i) for i in range(4, 7)],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row(
                    [create_number_button(i) for i in range(1, 4)],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row([create_number_button(0)], alignment=MainAxisAlignment.CENTER),
            ],
            alignment=MainAxisAlignment.CENTER,
        )

    async def button_clicked(self, e):
        if int(e.control.data) == self.current_digit:
            self.feedback_text.value = self.text_controller.get("correct_txt")
            self.current_digit = random.randint(0, 9)
            self.sound_button.data = self.current_digit
            self._playsound(numbers=[str(self.current_digit)], e=e)
            await asyncio.sleep(0.3)
            self.page.update()
            self.feedback_text.value = self.text_controller.get("level0_number_await")
            self.page.update()
        else:
            self.feedback_text.value = self.text_controller.get("incorrect_txt")
            self.page.update()

    def _open(self, e):
        e.page.go("/practice/0")
