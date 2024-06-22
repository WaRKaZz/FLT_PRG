import flet


def main(page: flet.Page):
    container1 = flet.Container(
        content=flet.Text("Container 1"),
        color=flet.Colors.BLUE,
        padding=10,
    )
    container2 = flet.Container(
        content=flet.Text("Container 2"),
        color=flet.Colors.GREEN,
        padding=10,
    )
    row = flet.Row(
        children=[container1, container2],
        alignment=flet.MainAxisAlignment.CENTER,
    )
    page.add(row)


flet.app(target=main)
