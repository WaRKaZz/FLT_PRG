import asyncio
import random
from flet import (
    Page, ElevatedButton, IconButton, Column, Row, Text,
    MainAxisAlignment, CrossAxisAlignment, icons, app, audio
)

class DigitGame:
    def __init__(self, page: Page):
        self.page = page
        self.current_digit = None
        self.audio = audio.Audio()
        self.page.overlay.append(self.audio)
        self.
        self.feedback_text = Text(size=20, text_align="center")
        self.sound_button = IconButton(
            icon=icons.VOLUME_UP,
            icon_size=24,
            width=280,
            height=50,
            data="sound",
            on_click=self.play_sound
        )

        self.keyboard = self.create_keyboard()
        self.content = Column(
            [self.feedback_text, self.sound_button, self.keyboard],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=20,
        )

    def create_keyboard(self):
        def create_number_button(number):
            return ElevatedButton(
                text=str(number),
                width=80,
                height=50,
                data=str(number),
                on_click=self.button_clicked
            )

        return Column(
            [
                Row(
                    [create_number_button(i) for i in range(7, 10)],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    [create_number_button(i) for i in range(4, 7)],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    [create_number_button(i) for i in range(1, 4)],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    [create_number_button(0)],
                    alignment=MainAxisAlignment.CENTER
                ),
            ],
            alignment=MainAxisAlignment.CENTER,
        )

    def generate_digit(self):
        self.current_digit = random.randint(0, 9)

    async def play_sound(self, _):
        self.audio.src = f"{self.current_digit}.mp3"
        await self.audio.play()
        await self.update_feedback("Please input digit")

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

    async def start_game(self):
        await self.generate_digit()

async def main(page: Page):
    page.title = "Digit Recognition Game"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    game = DigitGame(page)
    page.add(game.content)

    await game.start_game()

app(target=main)