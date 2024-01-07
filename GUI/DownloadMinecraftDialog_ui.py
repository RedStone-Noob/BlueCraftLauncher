# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DownloadMinecraftDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
                               QGridLayout, QGroupBox, QLabel, QRadioButton,
                               QSizePolicy, QVBoxLayout, QWidget)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.VersionLabel = QLabel(Dialog)
        self.VersionLabel.setObjectName(u"VersionLabel")

        self.gridLayout.addWidget(self.VersionLabel, 0, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.verticalLayout.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.groupBox)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.verticalLayout.addWidget(self.radioButton_5)

        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 2)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.accepted.connect(Dialog.download)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5b89\u88c5minecraft", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u5b89\u88c5\u7248\u672c\u786e\u8ba4\uff1a", None))
        self.VersionLabel.setText(QCoreApplication.translate("Dialog", u"1234567890", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"mod\u52a0\u8f7d\u5668\u9009\u62e9", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"\u539f\u7248", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"forge", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"fabric", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"quilt", None))
        self.radioButton_5.setText(QCoreApplication.translate("Dialog", u"neoforge", None))
    # retranslateUi
