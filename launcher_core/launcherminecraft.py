import os
import minecraft_launcher_lib as launcher
import json


class MinecraftLauncherInit(object):
    def __init__(self):
        super().__init__()
        if not os.path.exists(".minecraft"):
            os.makedirs(".minecraft")
        with open(".\\config.json", "w+") as self.file:
            if self.file.read() != open(".\\template.json", "r"):
                self.file.write(open(".\\template.json", "r").read())
            self.file.close()
