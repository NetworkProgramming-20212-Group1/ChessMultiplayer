from PyQt5.uic import loadUi
from components.room import Room
from components.roomConfiguration import RoomConfiguration
from PyQt5.QtWidgets import QWidget, QMainWindow, QMessageBox
from response import *
from request import *

class Play(QWidget):
    def __init__(self, mainwindow: QMainWindow):
        super(Play,self).__init__()
        self.mainwindow = mainwindow
        loadUi("play.ui",self)
        self.eventHandler()
        self.getRoom()

    def eventHandler(self):
        self.create_pvp.clicked.connect(self.createPVPRoom)
        self.create_custom.clicked.connect(self.createCustomRoom)

    def createDialog(self):
        dialog = RoomConfiguration()
        dialog.exec_()
        return dialog.getInputs()

    def createCustomRoom(self): 
        roomConfig = self.createDialog()
        if roomConfig is not None:
            roomID = roomConfig[0]
            password = roomConfig[1]
            matchType = "CUSTOM"
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

    def getRoom(self):
        for x in range(8):
            openRoom = Room()
            self.verticalLayout_2.addWidget(openRoom)
            openRoom.roomID.setText("room " + f'{x + 1}')
