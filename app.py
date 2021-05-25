
# librerias-varias
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os.path 

import sys
import platform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# Log IN screen
from login import Ui_LogScreen
# Sign UP screen
from signup import Ui_SignScreen
from modules import *
from widgets import *

#Variables Globales
usertxt=""
passtext=""
widgets = None
usercont=0
userid=[]
#DB CONN
conn = psycopg2.connect(dbname="safechest",user="postgres", password="123", host="localhost")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()

print("conectado")
#SIGN UP SCREEN
class SignScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SignScreen()
        self.ui.setupUi(self)
         ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ##BUTTON ACTIONS
        self.ui.createButton.clicked.connect(self.ShowLogScreen)
    ##FUNCTIONS
    def GetTextFromUser(self):
        return self.ui.sign_user_txt.text()
    def GetTextFromPassword(self):
        return self.ui.sign_pass_txt.text()
    def ShowLogScreen(self):
        global usercont
        usercont+=1
        
        ####INSERT INTO USERS VA ACA
        usertxt = self.GetTextFromUser()
        passtext = self.GetTextFromPassword()
        cursor.execute("INSERT INTO users (name, password) VALUES('"+usertxt+"'"+","+"'"+passtext+"'"+")")
        print("funciona insert into users")
        #######################################
        
        self.close()
        self.log= LogScreen()
        self.log.show()

#LOG SCREEN
class LogScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_LogScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## close 
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())
        self.ui.minimizeAppBtn.setVisible(False)
        #login button
        self.ui.loginButton.clicked.connect(self.LogIN)
        #signup button
        self.ui.signButton.clicked.connect(self.ShowSignScreen)
        



        self.show()
    

    #functions
    def ShowSignScreen(self):
        self.close()
        self.sign= SignScreen()
        self.sign.show()

    def GetTextFromUserLog(self):
        return self.ui.user_login_txt.text()
    def GetTextFromPasswordLog(self):
        return self.ui.pass_login_txt.text()

    def LogIN(self):
        global userid
        loguser= self.GetTextFromUserLog()
        logpass= self.GetTextFromPasswordLog()
        
        print(logpass)
        print(loguser)
        print(usertxt)
        print(passtext)
        #dentro del if se hace un exist de select * from users where user= loguser and password= logpasss
        cursor.execute("SELECT * FROM users WHERE name= "+"'"+loguser+"' and password= "+"'"+logpass+"'")
        x = cursor.fetchone()
        if not(x):
            #mostrar el error
            return
        else:
            userid= self.GetUserId()
            print(userid)
            self.close()
            self.main=MainWindow()
            self.main.show()
        #########################################################################################################
    def GetUserId(self):
        
        loguser= self.GetTextFromUserLog()
        logpass= self.GetTextFromPasswordLog()
        print(logpass)
        print(loguser)
        cursor.execute("SELECT * FROM users WHERE name= "+"'"+loguser+"' and password= "+"'"+logpass+"'")
        
        return cursor.fetchone()[0]
        





class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "SafeChest"
        description = "SafeChest"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)
        
        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.ui.btn_logout.clicked.connect(self.Logout)
        self.ui.btn_print.setVisible(False)
        self.ui.btn_message.setVisible(False)
        self.ui.btn_widgets.setVisible(False)
        self.ui.btn_save.setVisible(False)
        self.ui.btn_exit.setVisible(False)
        self.ui.toggleLeftBox.setVisible(False)
        self.ui.titleRightInfo.setText("SafeChest")
        
        #////////////////////////////////Crear ADD Site//////////////////////////////////////
        ###################titulo##################
        self.AddTitle= QLabel(self.ui.new_page)
        self.AddTitle.setObjectName("addtitle")
        self.AddTitle.setGeometry(400,50,661,61)
        self.AddTitle.setStyleSheet("\n"
"#addtitle{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 30pt \"Poor Richard\";\n"
"}\n"
"\n")
        
        self.AddTitle.setText("AGREGUE   SU   SITIO")
        ###############################################################
        ################ nombre de sitio###################################
        self.siteName=QLineEdit(self.ui.new_page)
        self.siteName.setObjectName("sitename")
        self.siteName.setGeometry(350,200,441,41)
        self.siteName.setStyleSheet(
            "\n"
            "#sitename{\n"
            "background-color:rgb(40, 44, 52);\n"
            "color:rgb(250,250,250);\n"
            "border: 2px solid white;\n"
            "font: 12pt \"Poor Richard\";\n"
            "border-radius: 10px;\n"
            "}\n"
        )
        self.siteName.setPlaceholderText(" Nombre  de  su  sitio")
        ################################################################################
        #################################### url del sitio ##############################
        self.siteUrl=QLineEdit(self.ui.new_page)
        self.siteUrl.setObjectName("siteurl")
        self.siteUrl.setGeometry(350,300,441,41)
        self.siteUrl.setStyleSheet(
                  "\n"
            "#siteurl{\n"
            "background-color:rgb(40, 44, 52);\n"
            "color:rgb(250,250,250);\n"
            "border: 2px solid white;\n"
            "font: 12pt \"Poor Richard\";\n"
            "border-radius: 10px;\n"
            "}\n"
            
        )
        
        self.siteUrl.setPlaceholderText("URL del sitio web")
        ######################################## password del sitio ####################################
        self.sitePass=QLineEdit(self.ui.new_page)
        self.sitePass.setObjectName("sitepass")
        self.sitePass.setGeometry(350,400,441,41)
        self.sitePass.setStyleSheet(
                       "\n"
            "#sitepass{\n"
            "background-color:rgb(40, 44, 52);\n"
            "color:rgb(250,250,250);\n"
            "border: 2px solid white;\n"
            "font: 12pt \"Poor Richard\";\n"
            "border-radius: 10px;\n"
            "}\n"
            
        )
        self.sitePass.setEchoMode(QLineEdit.Password)
        self.sitePass.setPlaceholderText("Password del Sitio Web")

        ##################################### boton de insert a sites########################################
        self.siteIns= QPushButton(self.ui.new_page)
        self.siteIns.setObjectName("siteinsbtn")
        self.siteIns.setGeometry(450,500,250,30)
        self.siteIns.setStyleSheet(
            "\n"
            "#siteinsbtn{\n"
            "background-color: rgb(138, 138, 138);\n"
            "border-radius: 12px;\n"
            "color:rgb(255,255,255);\n"
            "font: 14pt \"Poor Richard\";\n"
            "\n"
            "}\n"
            "#siteinsbtn::hover{\n"
            "background-color:rgb(44, 44, 44)\n"
            "\n"
            "}\n"
        )
        self.siteIns.setText("Agregar Sitio")
        self.siteIns.clicked.connect(self.InsertSite)
                ###################mensaje exito##################
        self.Addm= QLabel(self.ui.new_page)
        self.Addm.setObjectName("addm")
        self.Addm.setGeometry(400,600,661,61)
        self.Addm.setStyleSheet("\n"
"#addm{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 12pt \"Poor Richard\";\n"
"}\n"
"\n")
        
        self.Addm.setText("INGRESO   SU   SITIO")
        self.Addm.setVisible(False)
        self.ui.btn_new.released.connect(self.Addm.setVisible(False))
        #////////////////////////////////Crear ADD Site//////////////////////////////////////
        #////////////////////////////////Crear View Sites//////////////////////////////////////
                
        self.viewTitle= QLabel(self.ui.home)
        self.viewTitle.setObjectName("viewtitle")
        self.viewTitle.setGeometry(400,50,661,61)
        self.viewTitle.setStyleSheet("\n"
"#viewtitle{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 30pt \"Poor Richard\";\n"
"}\n"
"\n")
        
        self.viewTitle.setText("SITIOS  DISPONIBLES")
        ###############################################################
        ############################## sitios disponibles############################
                      
        self.viewSites= QLabel(self.ui.home)
        self.viewSites.setObjectName("viewsites")
        self.viewSites.setGeometry(400,150,800,800)
        self.viewSites.setAlignment(Qt.AlignLeading|Qt.AlignLeft)
        self.viewSites.setStyleSheet("\n"
"#viewsites{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 16pt \"Segoe UI\";\n"
"}\n"
"\n")
        self.ui.btn_home.clicked.connect(self.getSites)
        self.viewSites.setText("Aqui van los sitios de la DB del id: "+str(userid))
        #////////////////////////////////Crear View Sites//////////////////////////////////////
        
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    #------------------- Insert Site Function-------------------------------------------#
    def GetSiteName(self):
        return self.siteName.text()
    def GetSiteUrl(self):
        return self.siteUrl.text()
    def GetSitePass(self):
        return self.sitePass.text()
    def InsertSite(self):
        name=self.GetSiteName()
        url= self.GetSiteUrl()
        pas= self.GetSitePass()
        cursor.execute("INSERT INTO sites(name,url,pass,id_user) values('"+name+"'"+","+"'"+url+"'"+","+"'"+pas+"'"+","+str(userid)+")")
        conn.commit()
        print("ingresado")
        
    
    ######################################################################################
        #------------------- View Site Function-------------------------------------------#
    def getSites(self):
                
        cursor.execute("select name from sites where id_user= "+str(userid))
        n = cursor.fetchall()
        cursor.execute("select id from sites where id_user= "+str(userid))
        ids = cursor.fetchall()
        
        cursor.execute("select url from sites where id_user= "+str(userid))
        u = cursor.fetchall()

        
        cursor.execute("select pass from sites where id_user= "+str(userid))
        p = cursor.fetchall()

        cont=1
        s=""
        while(cont <= len(n)):
            
            s+=" No.  " +str(ids[cont - 1][0])+"   Sitio:  "+ str(n[cont - 1][0])+"\n" +" URL:  "+ str(u[cont - 1][0])+"\n" +" Password:  "+ str(p[cont - 1][0])+"\n\n"
            
            cont = cont + 1
        self.viewSites.setText(s)
    ######################################################################################
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_save":
            print("Save BTN clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
    ##function logout
    def Logout(self):
        self.close()
        self.log=LogScreen()
        self.log.show()





        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = LogScreen()
    sys.exit(app.exec_())