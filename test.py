import os

path = "C:\\Intel\\PRJ\\nomerin-aitashy\\resources\\voice_aigul"

files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

for file in files:
    if " " in file:
        os.rename(path + "\\" + file, path + "\\" + file.replace(" ", ""))
