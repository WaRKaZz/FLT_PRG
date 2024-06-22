import asyncio

import flet as ft
from flet import Page

from master_parts import Master_Navigation_Bar
from routes import route_about, route_guide, route_practice, route_root, route_setting


async def main(page: Page):
    navigation_bar = Master_Navigation_Bar()

    async def route_change(e: ft.RouteChangeEvent):
        if e.route == "/":
            await route_root(page=page, navigation_bar=None)
        elif e.route.startswith("/guide"):
            await route_guide(page=page, navigation_bar=navigation_bar)
        elif e.route.startswith("/about"):
            await route_about(page=page, navigation_bar=navigation_bar)
        elif e.route.startswith("/practice"):
            await route_practice(page=page, navigation_bar=navigation_bar)
        elif e.route.startswith("/settings"):
            await route_setting(page=page, navigation_bar=navigation_bar)
        else:
            page.go("/")
        page.update()

    async def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_view_pop = view_pop
    page.on_route_change = route_change
    page.go(page.route)


if __name__ == "__main__":
    asyncio.run(ft.app(target=main))
