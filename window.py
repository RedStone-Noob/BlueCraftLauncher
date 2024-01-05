import tkinter as ttk
from tkinter import *
from tkinter import font
from tkinter import ttk
import ttkbootstrap
from ttkbootstrap.constants import *
from ttkbootstrap import tooltip
import launcher_core.downloadminecraft
import launcher_core.launcherminecraft
from typing import Literal


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.MinecraftInit = launcher_core.launcherminecraft.MinecraftLauncherInit()
        self.ThemesManager = ttkbootstrap.Style
        self.FontSettings = font.Font(font="TkDefaultFont")
        self.FontSettings.config(family="Microsoft YaHei UI", size=10)
        self.option_add("*Font", self.FontSettings)
        self.executeFunctions = False
        self.geometry("400x300")
        self.minsize(400, 300)
        self.title("BlueCraftLauncher")
        self.iconphoto(False, PhotoImage(file="resources/icon.png"))
        self.MinecraftInstaller = launcher_core.downloadminecraft.MinecraftInstaller(".minecraft")
        self.tabcontrol = ttk.Notebook(self)
        self.StartPanel = ttk.Frame()
        self.StartPanelTabControl = ttk.Notebook(self.StartPanel)
        self.MinecraftStartPanel = ttk.Frame()
        # ----------------MinecraftStartPanel界面实现开始--------------------------------------
        ttk.Label(self.MinecraftStartPanel, text="账户选择").grid(row=0, column=0)
        self.AccountSelectBox = ttk.Combobox(self.MinecraftStartPanel, values=["未登录", "已登录"])
        self.AccountSelectBox.grid(row=0, column=1)
        # ----------------MinecraftStartPanel界面实现结束--------------------------------------
        self.StartPanelTabControl.add(self.MinecraftStartPanel, text="启动游戏")
        self.AccountManagerPanel = ttk.Frame()
        # ----------------AccountManagerPanel界面实现开始--------------------------------------
        self.AccountList = Listbox(self.AccountManagerPanel)
        self.AccountList.pack(fill="both", expand=True, side=LEFT)
        self.MinecraftDownloadListScrollBar = ttk.Scrollbar(self.AccountManagerPanel, orient="vertical",
                                                            command=self.AccountList.yview)
        self.MinecraftDownloadListScrollBar.pack(side=RIGHT, fill="y")
        self.AccountList.config(yscrollcommand=self.MinecraftDownloadListScrollBar.set)
        self.AccountPanelToolBar = ttk.Frame(self.AccountManagerPanel)
        self.CreateAccountButton = ttk.Button(self.AccountPanelToolBar,
                                              text="创建新账户",
                                              command=self.create_account_window)
        self.CreateAccountButton.grid(row=0, sticky=W + E)
        self.DeleteAccountButton = ttk.Button(self.AccountPanelToolBar,
                                              text="删除账户",
                                              command=self.AccountList.delete("active"))
        self.DeleteAccountButton.grid(row=1, sticky=W + E)
        self.AccountPanelToolBar.pack(fill="x")
        # ----------------AccountManagerPanel界面实现结束--------------------------------------
        self.StartPanelTabControl.add(self.AccountManagerPanel, text="账户管理")
        self.StartPanelTabControl.pack(fill="both", expand=True)
        self.tabcontrol.add(self.StartPanel, text="启动")
        self.GameManagerPanel = ttk.Frame()
        self.GameManagerTabControl = ttk.Notebook(self.GameManagerPanel)
        self.MinecraftClientDownloadPanel = ttk.Frame()
        # ------------------MinecraftClientDownloadPanel界面实现开始---------------------------
        self.MinecraftDownloadList = Listbox(self.MinecraftClientDownloadPanel)
        for item in self.MinecraftInstaller.getminecraftversionlist():
            self.MinecraftDownloadList.insert(END, item)
        self.MinecraftDownloadList.pack(side=LEFT, fill="both", expand=True)
        self.MinecraftDownloadListScrollBar = ttk.Scrollbar(self.MinecraftClientDownloadPanel, orient="vertical",
                                                            command=self.MinecraftDownloadList.yview)
        self.MinecraftDownloadListScrollBar.pack(side=RIGHT, fill="y")
        self.MinecraftDownloadList.config(yscrollcommand=self.MinecraftDownloadListScrollBar.set)
        self.MinecraftClientDownloadPanelToolBar = ttk.Frame(self.MinecraftClientDownloadPanel)
        (ttk.Button(self.MinecraftClientDownloadPanelToolBar, text="更新列表", command=self.updatelist())
         .grid(row=0, sticky=W + E))
        ttk.Button(self.MinecraftClientDownloadPanelToolBar, text="安装", command=self.minecraftinstaller).grid(row=1,
                                                                                                                sticky=W + E)
        self.MinecraftClientDownloadPanelToolBar.pack(fill="x")
        # ------------------MinecraftClientDownloadPanel界面实现结束---------------------------
        self.GameManagerTabControl.add(self.MinecraftClientDownloadPanel, text="下载minecraft")
        self.GameManagerTabControl.pack(fill="both", expand=True)
        self.tabcontrol.add(self.GameManagerPanel, text="游戏管理")
        self.SettingsPanel = ttk.Frame()
        self.SettingsPanelTabControl = ttk.Notebook(self.SettingsPanel)
        self.PersonalizePanel = ttk.Frame()
        # ------------------PersonalizePanel界面实现开始---------------------------------------
        ttk.Label(self.PersonalizePanel, text="主题选择").grid(row=0, column=0)
        self.themeSelectionBox = ttk.Combobox(self.PersonalizePanel, values=["yeti",
                                                                             "cosmo",
                                                                             "flatly",
                                                                             "journal",
                                                                             "literal",
                                                                             "lumen",
                                                                             "minty",
                                                                             "pulse",
                                                                             "sandstone",
                                                                             "united",
                                                                             "cyborg",
                                                                             "darkly",
                                                                             "solar",
                                                                             "superhero"])
        self.themeSelectionBox.bind("<<ComboboxSelected>>", self.switch_themes)
        self.themeSelectionBox.grid(row=0, column=1)
        # ------------------PersonalizePanel界面实现结束---------------------------------------
        self.SettingsPanelTabControl.add(self.PersonalizePanel, text="个性化")
        self.GameSettingsPanel = ttk.Frame()
        # ------------------GameSettingsPanel界面实现开始---------------------------------------
        ttk.Label(self.GameSettingsPanel, text="设置Java路径").grid(row=0, column=0)
        self.JavaPath = ttk.Entry(self.GameSettingsPanel)
        self.JavaPath.grid(row=0, column=1)
        self.EnableJavaSearch = ttk.Checkbutton(self.GameSettingsPanel, text="根据游戏版本自动查找和选择Java")
        self.EnableJavaSearch.grid(row=0, column=2)
        # ------------------GameSettingsPanel界面实现结束---------------------------------------
        self.SettingsPanelTabControl.add(self.GameSettingsPanel, text="游戏设置")
        self.SettingsPanelTabControl.pack(fill="both", expand=True)
        self.tabcontrol.add(self.SettingsPanel, text="设置")
        self.tabcontrol.pack(fill="both", expand=True)
        self.executeFunctions = True

    def updatelist(self):
        if self.executeFunctions:
            for item in self.MinecraftInstaller.getminecraftversionlist():
                self.MinecraftDownloadList.insert(END, item)

    def minecraftinstaller(self):
        if self.executeFunctions:
            download_version = self.MinecraftDownloadList.get(ACTIVE)
            download = DownloadWindow(master=self, executefunctions=self.executeFunctions,
                                      downloadversion=download_version)
            download.mainloop()

    def create_account_window(self):
        if self.executeFunctions:
            account_window = AccountWindow(master=self, executefunctions=self.executeFunctions)
            account_window.mainloop()

    def switch_themes(self) -> None:
        if self.executeFunctions:
            self.ThemesManager.theme = self.themeSelectionBox.get()


class DownloadWindow(Toplevel):
    def __init__(self, downloadversion: str, master=None, executefunctions: bool = False):
        super().__init__(master)
        self.MinecraftInstaller = launcher_core.downloadminecraft.MinecraftInstaller(minecraftdir=".minecraft"
                                                                                     , version=downloadversion
                                                                                     , master=self)
        self.title("下载" + downloadversion)
        self.executeFunctions = executefunctions
        self.geometry("300x200")
        self.resizable(False, False)
        self.downloadversion = downloadversion
        ttk.Label(self, text=f"确认下载：{self.downloadversion}").grid(row=0, column=0, columnspan=2, sticky=W + E)
        ttk.Button(self, text="确认", command=self.download).grid(row=1, column=0)
        ttk.Button(self, text="取消", command=self.destroy).grid(row=1, column=1)
        ttk.Label(self, text="下载进度").grid(row=2, column=0)
        self.ProcessBar = ttk.Progressbar(self, orient=HORIZONTAL, length=200, mode='determinate', bootstyle=SUCCESS)
        self.ProcessBar.grid(row=2, column=1, columnspan=2, sticky=W + E)
        self.DownloadProgress = ttk.Label(self)

    def download(self):
        if self.executeFunctions:
            self.MinecraftInstaller.start()


class AccountWindow(Toplevel):
    def __init__(self, master=None, executefunctions: bool = True):
        super().__init__(master)
        self.MinecraftInit = launcher_core.launcherminecraft.MinecraftLauncherInit()
        self.OfflinePage = ttk.Frame(self)
        self.OnlinePage = ttk.Frame(self)
        self.var = IntVar()
        self.var.set(0)
        self.executeFunctions = executefunctions
        self.title("创建一个新的账户")
        self.geometry("300x200")
        self.resizable(False, False)
        ttk.Label(self, text="账户类型选择", bootstyle=INFO).grid(row=0, column=0, columnspan=2, sticky=W + E)
        self.RadioFrame = ttk.Frame(self)
        ttk.Radiobutton(self.RadioFrame, text="离线账户", variable=self.var, value=0, command=self.switch).grid(row=0, column=0)
        ttk.Radiobutton(self.RadioFrame, text="微软账户", variable=self.var, value=1, command=self.switch).grid(row=0, column=1)
        self.RadioFrame.grid(row=1, column=0, columnspan=2, sticky=W + E)
        ttk.Label(self.OfflinePage, text="输入游戏名").grid(row=0, column=0)
        self.OfflineUserName = ttk.Entry(self.OfflinePage)
        self.OfflineUserName.grid(row=0, column=1, sticky=W + E)
        ttk.Button(self.OfflinePage, text="创建", bootstyle=(SUCCESS, OUTLINE)).grid(row=1,
                                                                                     column=0,
                                                                                     columnspan=2,
                                                                                     sticky=W + E)
        ttk.Button(self.OnlinePage, text="点我在浏览器中打开登录窗口", bootstyle=(SUCCESS, OUTLINE)).grid(row=1,
                                                                                     column=0,
                                                                                     columnspan=2,
                                                                                     sticky=W + E)
        self.OfflinePage.grid(row=3, column=0)

    def switch(self):
        self.OfflinePage.grid_remove()
        self.OnlinePage.grid_remove()
        if self.var.get() == 0:
            self.OfflinePage.grid(row=3, column=0)
        elif self.var.get() == 1:
            self.OnlinePage.grid(row=3, column=0)
    def __create_outline_account(self):
        pass