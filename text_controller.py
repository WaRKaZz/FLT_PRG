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
