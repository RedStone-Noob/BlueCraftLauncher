from GUI import DownloadMinecraftDialog_ui
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import launcher_core.downloadminecraft
from GUI import MainWindow_ui


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MainWindow_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.__initialization()
        self.MinecraftInstaller = None

    def startminecraft(self):
        pass

    def __initialization(self):
        MinecraftVersionModel = QStringListModel()
        MinecraftVersionModel.setStringList(launcher_core.downloadminecraft.getminecraftversionlist())
        self.ui.MinecraftVersionList.setModel(MinecraftVersionModel)

    def DownloadMinecraft(self):
        dialog = DownloadDialog(self.ui.MinecraftVersionList.selectedIndexes())
        dialog.exec()


class DownloadDialog(QDialog):
    def __init__(self, version: str = ""):
        super().__init__()
        self.ui = DownloadMinecraftDialog_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.__initialization()
        self.MinecraftInstaller = None
        self.version = version

    def __initialization(self):
        pass

    def DownloadMinecraft(self):
        self.MinecraftInstaller = launcher_core.downloadminecraft.MinecraftInstaller(
            self.ui.MinecraftVersionList.selectedItems()[0])

    def download(self):
        pass
