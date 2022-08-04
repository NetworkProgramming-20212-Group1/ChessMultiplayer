from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget, QMessageBox, QMainWindow
from request import *
from response import *

class RegisterLogin(QWidget):
    def __init__(self, mainwindow: QMainWindow):
        super(RegisterLogin,self).__init__()
        self.mainwindow = mainwindow
        loadUi("login_Register.ui",self)
        self.input_log_username.setFocusPolicy(Qt.StrongFocus)
        self.input_log_username.setFocus()
        self.eventHandler()

    def eventHandler(self):
        self.input_log_username.returnPressed.connect(self.loginButton.click)
        self.input_log_pw.returnPressed.connect(self.loginButton.click)
        self.input_reg_username.returnPressed.connect(self.registerButton.click)
        self.input_reg_pw.returnPressed.connect(self.registerButton.click)
        self.input_reg_ingame.returnPressed.connect(self.registerButton.click)
        self.registerButton.clicked.connect(self.inputRegister)
        self.loginButton.clicked.connect(self.inputLogin)
    
    def clearInf (self):
        self.inf_reg_usr.setText("")
        self.inf_reg_pw.setText("")
        self.inf_reg_ing.setText("")
        self.inf_log_usr.setText("")
        self.inf_log_pw.setText("")

    def clearInput(self):
        self.input_reg_username.setText("")
        self.input_reg_pw.setText("")
        self.input_reg_ingame.setText("")
        self.input_log_username.setText("")
        self.input_log_pw.setText("")

    def inputRegister(self):
        reg_username = self.input_reg_username.text()
        reg_pw = self.input_reg_pw.text()
        reg_ingame = self.input_reg_ingame.text()
        if(not reg_username):
            self.inf_reg_usr.setText("Please enter your username")
            self.input_reg_username.setFocus()
        elif(not reg_pw):
            self.inf_reg_pw.setText("Please enter your password")
            self.input_reg_pw.setFocus()
        elif(not reg_ingame):
            self.inf_reg_ing.setText("Please enter your ingame")
            self.input_reg_ingame.setFocus()
        else:
            self.clearInf()
            self.clearInput()
            registerObject = RegisterObject(reg_username, reg_pw, reg_ingame)
            self.mainwindow.sendRequest(createRequest("REGT",registerObject))
            normalResponse: NormalResponse = self.mainwindow.getResponse("REGT")
            if (normalResponse.code < 400):
                self.clearInput()
                self.input_log_username.setFocus(True)
                msg = QMessageBox()
                msg.setWindowTitle("")
                msg.setText("Register successfully!")
                msg.exec_()
            else:
                responseObject = json.loads(normalResponse.data)
                msg = QMessageBox()
                msg.setWindowTitle("")
                msg.setText(responseObject["message"])
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()
                self.input_reg_username.setFocus()

    def inputLogin(self):
        log_username = self.input_log_username.text()
        log_pw = self.input_log_pw.text()
        if(not log_username):
            self.inf_log_usr.setText("Please enter your username")
            self.input_log_username.setFocus()
        elif(not log_pw):
            self.inf_log_pw.setText("Please enter your password")
            self.input_log_pw.setFocus()
        else:
            self.clearInf()
            self.clearInput()
            loginObject = LoginObject(log_username, log_pw)
            self.mainwindow.sendRequest(createRequest("LOGN",loginObject))
            # send the information to server to check
            normalResponse: NormalResponse = self.mainwindow.getResponse("LOGN")
            responseObject = json.loads(normalResponse.data)
            if (normalResponse.code < 400):
                self.mainwindow.ingame = responseObject["inGame"]
                self.mainwindow.gotoHome()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("")
                msg.setText(responseObject["message"])
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()
                self.input_log_username.setFocus()
