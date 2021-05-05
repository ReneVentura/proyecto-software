# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *



class Ui_LogScreen(object):
    def setupUi(self, LogScreen):
        if not LogScreen.objectName():
            LogScreen.setObjectName(u"LogScreen")
        LogScreen.resize(736, 481)
        self.centralwidget = QWidget(LogScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {	\n"
"	background-color: rgb(56, 58, 89);	\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(10, 40, 661, 61))
        font = QFont()
        font.setFamily(u"Poor Richard")
        font.setPointSize(30)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.user_login_txt = QLineEdit(self.dropShadowFrame)
        self.user_login_txt.setObjectName(u"user_login_txt")
        self.user_login_txt.setGeometry(QRect(160, 200, 381, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        self.user_login_txt.setFont(font1)
        self.user_login_txt.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgb(255,255,255);\n"
"color: rgb(255,255,255);\n"
"padding-bottom:7px")
        self.pass_login_txt = QLineEdit(self.dropShadowFrame)
        self.pass_login_txt.setObjectName(u"pass_login_txt")
        self.pass_login_txt.setGeometry(QRect(160, 270, 381, 31))
        self.pass_login_txt.setFont(font1)
        self.pass_login_txt.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgb(255,255,255);\n"
"color: rgb(255,255,255);\n"
"padding-bottom:7px")
        self.pass_login_txt.setEchoMode(QLineEdit.Password)
        self.loginButton = QPushButton(self.dropShadowFrame)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(222, 350, 251, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        self.loginButton.setFont(font2)
        self.loginButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginButton.setStyleSheet(u"QPushButton#loginButton{\n"
"background-color: rgb(144, 134, 255);\n"
"border-radius: 12px;\n"
"color:rgb(255,255,255);\n"
"\n"
"\n"
"}\n"
"QPushButton#loginButton::hover{\n"
"background-color:rgb(106, 116, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton#loginButton::pressed{\n"
"background-color:rgb(49, 49, 255);\n"
"}\n"
"\n"
"QPushButton #loginButton{\n"
"background-color:  rgb(144, 134, 255);\n"
"\n"
"}")
        self.signButton = QPushButton(self.dropShadowFrame)
        self.signButton.setObjectName(u"signButton")
        self.signButton.setGeometry(QRect(220, 400, 251, 31))
        self.signButton.setFont(font2)
        self.signButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.signButton.setStyleSheet(u"QPushButton#signButton{\n"
"background-color: rgb(255, 142, 229);\n"
"border-radius: 12px;\n"
"color:rgb(255,255,255);\n"
"\n"
"\n"
"}\n"
"QPushButton#signButton::hover{\n"
"background-color:rgb(255, 93, 239)\n"
"\n"
"}\n"
"\n"
"QPushButton#signButton::pressed{\n"
"background-color:rgb(255, 62, 236)\n"
"}\n"
"\n"
"QPushButton #signButton{\n"
"background-color:   rgb(255, 142, 229);\n"
"\n"
"}")
        self.closeAppBtn = QPushButton(self.dropShadowFrame)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setGeometry(QRect(680, 10, 28, 28))
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setStyleStrategy(QFont.PreferDefault)
        self.closeAppBtn.setFont(font3)
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setStyleSheet(u"QPushButton#closeAppBtn{\n"
"\n"
"background-color:rgb(56, 58, 89)\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))
        self.minimizeAppBtn = QPushButton(self.dropShadowFrame)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setGeometry(QRect(600, 10, 28, 28))
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimizeAppBtn.setStyleSheet(u"QPushButton#minimizeAppBtn{\n"
"background-color:rgb(56, 58, 89);\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.dropShadowFrame)

        LogScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(LogScreen)

        QMetaObject.connectSlotsByName(LogScreen)
    # setupUi

    def retranslateUi(self, LogScreen):
        LogScreen.setWindowTitle(QCoreApplication.translate("LogScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("LogScreen", u"<html><head/><body><p>SAFECHEST</p></body></html>", None))
        self.user_login_txt.setPlaceholderText(QCoreApplication.translate("LogScreen", u"  User", None))
        self.pass_login_txt.setPlaceholderText(QCoreApplication.translate("LogScreen", u"  Password", None))
        self.loginButton.setText(QCoreApplication.translate("LogScreen", u"L O G  I N", None))
        self.signButton.setText(QCoreApplication.translate("LogScreen", u"S I N G  UP", None))
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("LogScreen", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("LogScreen", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
    # retranslateUi

