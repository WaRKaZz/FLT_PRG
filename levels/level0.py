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
    ):
        super().__init__(
            text_controller=text_controller,
            navigation_bar=navigation_bar,
            app_bar=app_bar,
            number=0,
            view_type="level",
        )
        self.current_digit = random.randint(0, 9)
        self.feedback_text.value = text_controller.get("level0_number_await")
        sound_button = IconButton(
            icon=icons.VOLUME_UP,
            icon_size=24,
            width=280,
            height=50,
            data="sound",
            on_click=self._playsound,
        )

        self.feedback_text = Text(size=20, text_align="center")
        keyboard = self.create_keyboard()

        content = Column(
            [sound_button, keyboard],
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
            await self.update_feedback("Correct!")
            await asyncio.sleep(2)
            await self.generate_digit()
        else:
            await self.update_feedback("Incorrect")

    async def update_feedback(self, message):
        self.feedback_text.value = message
        await self.page.update_async()

    async def generate_digit(self):
        self.current_digit = random.randint(0, 9)

    def _open(self, e):
        e.page.go("/practice/0")
