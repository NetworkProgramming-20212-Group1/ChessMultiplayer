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
        self.getBasicInfo()
        self.socketSignal.connect(self.addNewWidget)
        try:
            t1 = threading.Thread(target=self.getMatchHistory, args=(), daemon=True)
            t1.start()
        except:
            print ("create thread error")

    def getBasicInfo(self): 
        while True:
            profileObject = ProfileObject(self.ingame)
            self.mainwindow.sendRequest(createRequest("PROF", profileObject))
            normalResponse: NormalResponse = self.mainwindow.getResponse("PROF")
            if(normalResponse):
                    if(normalResponse.code < 400):
                        responseObject = json.loads(normalResponse.data)
                        rank = responseObject["rank"]
                        self.rank_inf.setText(rank)
                        level = responseObject["level"]
                        self.level_inf.setText(level)
                        matchHistory = responseObject["matchHistory"]
                        for x in matchHistory:
                            self.socketSignal.emit(x)
            self.clearDisplay()
            time.sleep(10)

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