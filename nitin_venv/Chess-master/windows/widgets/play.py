from PyQt5.uic import loadUi
from components.room import Room
from components.roomConfiguration import RoomConfiguration
from PyQt5.QtWidgets import QWidget, QMainWindow, QMessageBox
from PyQt5 import QtCore
from response import *
from request import *
import time
import threading


class Play(QWidget):
    socketSignal = QtCore.pyqtSignal(object)

    def __init__(self, mainwindow: QMainWindow):
        super(Play,self).__init__()
        self.mainwindow = mainwindow
        loadUi("play.ui",self)
        self.eventHandler()
        self.socketSignal.connect(self.addNewWidget)
        try:
            t1 = threading.Thread(target=self.getRoom, args=(), daemon=True)
            t1.start()
        except:
            print ("create thread error")

    def eventHandler(self):
        self.create_pvp.clicked.connect(self.createPVPRoom)
        self.create_custom.clicked.connect(self.createCustomRoom)

    def createRoomDialog(self):
        dialog = RoomConfiguration()
        dialog.exec_()
        return dialog.getInputs()

    def createCustomRoom(self): 
        roomConfig = self.createRoomDialog()
        if roomConfig is not None:
            roomID = roomConfig[0]
            password = roomConfig[1]
            matchType = "CUSTOM"
            if not password:
                createRoomObject = CreateRoomObject(roomID, None, matchType)
            else:
                createRoomObject = CreateRoomObject(roomID, password, matchType)
            self.mainwindow.sendRequest(createRequest("CRRM",createRoomObject))
            normalResponse: NormalResponse = self.mainwindow.getResponse("CRRM")
            responseObject = json.loads(normalResponse.data)
            if(normalResponse.code < 400):
                self.mainwindow.gotoCustom(responseObject)
            else:
                msg = QMessageBox()
                msg.setWindowTitle("")
                msg.setText(responseObject["message"])
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()
                self.createCustomRoom()

    def createPVPRoom(self):
        self.mainwindow.gotoPVP()

# hien thi phong co pw hay ko 
    def getRoom(self):
        self.mainwindow.sendRequest(createRequest("ROOM", None))
        normalResponse: NormalResponse = self.mainwindow.getResponse("ROOM")
        if normalResponse:
            if normalResponse.code < 400:
                responseObject = json.loads(normalResponse.data)
                for x in responseObject:
                    self.socketSignal.emit(x)
        self.clearDisplay()
        time.sleep(3)
        
    def addWidget(self, x):
        openRoom = Room(self.mainwindow, x)
        self.verticalLayout_2.addWidget(openRoom)

    def clearDisplay(self):
        for i in reversed(range(self.verticalLayout_2.count())): 
            widgetToRemove = self.verticalLayout_2.itemAt(i).widget()
            # remove it from the layout list
            self.verticalLayout_2.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.deleteLater()
