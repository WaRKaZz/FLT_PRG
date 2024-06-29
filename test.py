import flet as ft
from os import getcwd

def main(page: ft.Page):
    audio1 = ft.Audio(
        src="C:\\Intel\\PRJ\\nomerin-aitashy\\resources\\voice_aigul\\3.mp3",
        autoplay=True,
    )
    page.overlay.append(audio1)
    page.add(
        ft.Text("This is an app with background audio."),
        ft.ElevatedButton("Stop playing", on_click=lambda _: audio1.pause()),
    )


if __name__ == "__main__":
    print(getcwd())
    # ft.app(target=main)
