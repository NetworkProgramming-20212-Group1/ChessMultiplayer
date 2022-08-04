from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget, QMainWindow, QMessageBox
from response import *
from request import *
class FriendList(QWidget):
    def __init__(self, mainwindow: QMainWindow, x):
        super(FriendList,self).__init__()
        loadUi("friendList.ui",self)   
        self.x = x
        self.eventhandler(self.x)
        self.unfriend_button.clicked.connect(lambda: self.unfriend(self.x))

    def eventhandler(self, x):
        ingame = x["ingame"]
        self.ingame.setText(ingame)
        status = x["isOnline"]
        if not status:
            self.status.setText("offline")
        else:
            self.status.setText("online")

    def unfriend(self, x):
        ingame = x["ingame"]
        unfriendObject = UnfriendObject(ingame)
        self.mainwindow.sendRequest(createRequest("UNFR",unfriendObject))
        normalResponse: NormalResponse = self.mainwindow.getResponse("UNFR")
        if(normalResponse):
            if (normalResponse.code < 400):
                responseObject = json.loads(normalResponse.data)
                unfriend_ingame = responseObject["ingame"]
                msg = QMessageBox() 
                msg.setWindowTitle("Unfriend")
                msg.setText(unfriend_ingame + " is deleted from your friend list")
                msg.exec_()