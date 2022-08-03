from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget

class FriendList(QWidget):
    def __init__(self, x):
        super(FriendList,self).__init__()
        loadUi("friendList.ui",self)   
        self.x = x
        self.eventhandler(self.x)

    def eventhandler(self, x):
        ingame = x["ingame"]
        self.ingame.setText(ingame)
        status = x["isOnline"]
        if not status:
            self.status.setText("offline")
        else:
            self.status.setText("online")
