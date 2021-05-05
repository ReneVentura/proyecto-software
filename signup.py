# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_SignScreen(object):
    def setupUi(self, SignScreen):
        if not SignScreen.objectName():
            SignScreen.setObjectName(u"SignScreen")
        SignScreen.resize(750, 337)
        self.centralwidget = QWidget(SignScreen)
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
        self.label_title_2 = QLabel(self.dropShadowFrame)
        self.label_title_2.setObjectName(u"label_title_2")
        self.label_title_2.setGeometry(QRect(30, 20, 661, 61))
        font = QFont()
        font.setFamily(u"Poor Richard")
        font.setPointSize(30)
        self.label_title_2.setFont(font)
        self.label_title_2.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.label_title_2.setAlignment(Qt.AlignCenter)
        self.sign_user_txt = QLineEdit(self.dropShadowFrame)
        self.sign_user_txt.setObjectName(u"sign_user_txt")
        self.sign_user_txt.setGeometry(QRect(160, 110, 411, 41))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        self.sign_user_txt.setFont(font1)
        self.sign_user_txt.setStyleSheet(u"QLineEdit#sign_user_txt{\n"
"background-color:rgb(56, 58, 89);\n"
"color:rgb(255, 255, 255);\n"
" border: 2px solid white;\n"
" border-radius: 10px;\n"
"}\n"
"")
        self.sign_pass_txt = QLineEdit(self.dropShadowFrame)
        self.sign_pass_txt.setObjectName(u"sign_pass_txt")
        self.sign_pass_txt.setGeometry(QRect(160, 180, 411, 41))
        self.sign_pass_txt.setFont(font1)
        self.sign_pass_txt.setStyleSheet(u"QLineEdit#sign_pass_txt{\n"
"background-color:rgb(56, 58, 89);\n"
"color:rgb(255, 255, 255);\n"
" border: 2px solid white;\n"
" border-radius: 10px;\n"
"}\n"
"")
        self.createButton = QPushButton(self.dropShadowFrame)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setGeometry(QRect(230, 240, 251, 31))
        self.createButton.setFont(font1)
        self.createButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.createButton.setStyleSheet(u"QPushButton#createButton{\n"
"background-color: rgb(255, 142, 229);\n"
"border-radius: 12px;\n"
"color:rgb(255,255,255);\n"
"\n"
"\n"
"}\n"
"QPushButton#createButton::hover{\n"
"background-color:rgb(255, 93, 239)\n"
"\n"
"}\n"
"\n"
"QPushButton#createButton::pressed{\n"
"background-color:rgb(255, 62, 236)\n"
"}\n"
"\n"
"QPushButton #createButton{\n"
"background-color:   rgb(255, 142, 229);\n"
"\n"
"}")

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SignScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SignScreen)

        QMetaObject.connectSlotsByName(SignScreen)
    # setupUi

    def retranslateUi(self, SignScreen):
        SignScreen.setWindowTitle(QCoreApplication.translate("SignScreen", u"MainWindow", None))
        self.label_title_2.setText(QCoreApplication.translate("SignScreen", u"<html><head/><body><p>SIGN UP</p></body></html>", None))
        self.sign_user_txt.setPlaceholderText(QCoreApplication.translate("SignScreen", u"    Nombre de Usuario", None))
        self.sign_pass_txt.setPlaceholderText(QCoreApplication.translate("SignScreen", u"    Escriba su Password", None))
        self.createButton.setText(QCoreApplication.translate("SignScreen", u"S I N G  UP", None))
    # retranslateUi

