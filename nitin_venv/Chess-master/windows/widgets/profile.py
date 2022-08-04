import time
from PyQt5.uic import loadUi
from components.matchHistory import MatchHistory
from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore
from request import *
from response import *
import threading

class Profile(QWidget):
    socketSignal = QtCore.pyqtSignal(object)

    def __init__(self, mainwindow: QMainWindow):
        super(Profile,self).__init__()
        loadUi("profile.ui",self)
        self.mainwindow = mainwindow
        self.ingame = self.mainwindow.ingame
        self.socketSignal.connect(self.addNewWidget)
        try:
            self.t1 = threading.Thread(target=self.getBasicInfo, args=(), daemon=True)
            self.t1.start()
        except:
            print ("create thread error")

    def getBasicInfo(self): 
        profileWidgetIndex = self.mainwindow.getCurrentIndex() + 1
        # print(profileWidgetIndex)
        while True:
            profileObject = ProfileObject(self.ingame)
            self.mainwindow.sendRequest(createRequest("INFO", profileObject))
            normalResponse: NormalResponse = self.mainwindow.getResponse("INFO")
            if(normalResponse):
                if(normalResponse.code < 400):
                    responseObject = json.loads(normalResponse.data)
                    userObject = responseObject["user"]
                    username = userObject["username"]
                    password = userObject["password"]
                    self.username_inf.setText(username)
                    self.password_inf.setText(password)
                    matchHistory = responseObject["matches"]
                    for x in matchHistory:
                        self.socketSignal.emit(x)
            self.clearDisplay()
            time.sleep(200)
            currentWidgetIndex = self.mainwindow.getCurrentIndex()
            # print(currentWidgetIndex)
            if (profileWidgetIndex != currentWidgetIndex):
                break

    def addNewWidget(self, x):
        matchHistory =  MatchHistory(x)
        self.verticalLayout.addWidget(matchHistory)

    def clearDisplay(self):
        for i in reversed(range(self.verticalLayout.count())): 
            widgetToRemove = self.verticalLayout.itemAt(i).widget()
            # remove it from the layout list
            self.verticalLayout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.deleteLater()