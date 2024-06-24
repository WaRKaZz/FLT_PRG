# This file is part of Nomerin Aitashy.
#
# Nomerin Aitashy is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# Nomerin Aitashy is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with Nomerin Aitashy. If not, see <https://www.gnu.org/licenses/>.
import asyncio
import configparser


# TODO Create proper Text Controller and refactor every text getter
class Txt_Ctl:
    def __init__(self):
        pass

    @classmethod
    async def _async_get(cls, name: str, locale: str) -> str:
        config = configparser.RawConfigParser()
        try:
            await asyncio.to_thread(
                config.read, "language.properties", encoding="utf-8"
            )
        except FileNotFoundError:
            raise FileNotFoundError("Language file not found.")
        if not config.has_section(locale):
            raise ValueError("No en_US section found in language file.")
        if not config.has_option(locale, name):
            raise ValueError(f"No option '{name}' found in en_US section.")
        return config.get(locale, name)

    @classmethod
    def get(cls, name: str) -> str:
        locale = "en_US"
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        return loop.run_until_complete(cls._async_get(name, locale))


if __name__ == "__main__":
    print(Txt_Ctl.get("welcome_txt"))
