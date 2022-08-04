from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget, QMainWindow
from components.roomPassword import RoomPassword
from response import *
from request import *

class Room(QWidget):
    def __init__(self, mainwindow: QMainWindow, x):
        super(Room,self).__init__()
        loadUi("room.ui",self)
        self.mainwindow = mainwindow
        self.x = x
        self.eventHandler(self.x)
        self.join.clicked.connect(lambda: self.joinRoom(x))

    def eventHandler(self, x):
        roomid = x["roomid"]
        self.roomID.setText(roomid)
        if x["isPassword"]:
            self.isPassword.setText("require password")
        else:
            self.isPassword.setText("")

    def createPasswordDialog(self):
        dialog = RoomPassword()
        dialog.exec_()
        return dialog.getInputs()

    def joinRoom(self, x):
        roomid = x["roomid"]
        if x["isPassword"]:
            password = self.createPasswordDialog()
            joinRoomObject = JoinRoomObject(roomid, password)
        else: 
            joinRoomObject = JoinRoomObject(roomid, None)
        self.mainwindow.sendRequest(createRequest("JNRM",joinRoomObject))
        normalResponse: NormalResponse = self.mainwindow.getResponse("JNRM")
        if(normalResponse):
            if (normalResponse.code < 400):
                responseObject = json.loads(normalResponse.data)
                self.mainwindow.gotoCustom(responseObject)