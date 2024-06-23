# This file is part of Nomerin Aitashy.
#
# Nomerin Aitashy is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# Nomerin Aitashy is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with Nomerin Aitashy. If not, see <https://www.gnu.org/licenses/>.

welcome_message_txt = "Hello, fellow User, this applcation will teach how to count in Kazakh language \nPress Start to start your Kazakh language practice"
welcome_txt = "Welcome"
guide_txt = "Guide"
practice_txt = "Practice"
about_txt = "About Project"
start_txt = "Start"
settings_txt = "Settings"


import configparser


# TODO Create proper Text Controller and refactor every text getter
class txt_ctl:
    def __init__(self):
        pass

    @classmethod
    def __class_getitem__(self, name: str) -> str:
        config = configparser.RawConfigParser()
        config.read("language.properties")
        return config.get("en_US", name)


if __name__ == "__main__":
    print(txt_ctl["welcome_txt"])
