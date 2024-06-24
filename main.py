# This file is part of Nomerin Aitashy.
#
# Nomerin Aitashy is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# Nomerin Aitashy is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with Nomerin Aitashy. If not, see <https://www.gnu.org/licenses/>.

import asyncio

import flet as ft
from flet import Page

from controller import Controller, TextController


async def main(page: Page):

    text_controller = TextController()
    await text_controller.load_config()
    controller = Controller(page=page, text_controller=text_controller)

    page.on_view_pop = controller.view_pop
    page.on_route_change = controller.routechange
    page.go(page.route)


if __name__ == "__main__":
    asyncio.run(ft.app(target=main))
