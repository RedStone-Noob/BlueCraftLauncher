import minecraft_launcher_lib as launcher
import threading
import tkinter
from ttkbootstrap import toast
from tkinter import messagebox
import json
import requests


class MinecraftInstaller(threading.Thread):
    def __init__(self, minecraftdir, version: str = "", master: tkinter.Toplevel = None):
        threading.Thread.__init__(self)
        self.dir = minecraftdir
        self.version = version
        self.master = master

    def run(self):
        if self.version == "":
            raise ValueError("未指定版本号！")
        launcher.install.install_minecraft_version(self.version, self.dir)
        toast.ToastNotification(title="安装完成！", message=f"成功安装Minecraft{self.version}！").show_toast()
        self.master.destroy()

    def getminecraftversionlist(self,
                                url: str = "https://bmclapi2.bangbang93.com/mc/game/version_manifest_v2.json"
                                ) -> list:
        """
        获取Minecraft版本列表
        :param url:设置minecraft版本列表的url，默认为bmclapi2.bangbang93.com/mc/game/version_manifest_v2.json
        :return:返回minecraft版本列表
        """
        try:
            response = requests.get(url)
            data = json.loads(response.text)
            return list(item["id"] for item in data["versions"])
        except OSError:
            messagebox.Message().show(master=self, title="错误", message="无法连接到网络，请检查网络连接")
