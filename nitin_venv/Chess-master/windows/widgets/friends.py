from PyQt5.uic import loadUi
from components.friendList import FriendList
from PyQt5.QtWidgets import QWidget, QMainWindow, QMessageBox
from request import *
from response import *

class Friend(QWidget):
    def __init__(self, mainwindow: QMainWindow):
        super(Friend,self).__init__()
        self.mainwindow = mainwindow
        loadUi("friends.ui",self)
        self.getFriendList()
        self.addFriend()

    def addFriend(self):
        self.input_friendIngame.returnPressed.connect(self.add_friend.click)
        self.add_friend.clicked.connect(self.addFriendCheck)

    def addFriendCheck(self):
        friendIngame = self.input_friendIngame.text()
        add_friendObject = AddFriendObject(friendIngame)
        self.mainwindow.sendRequest(createRequest("ADFR",add_friendObject))
        self.input_friendIngame.setText("")
        normalResponse: NormalResponse = self.mainwindow.getResponse("ADFR")
        if(normalResponse.code < 400):
            msg = QMessageBox()
            msg.setWindowTitle("")
            msg.setText(friendIngame + " was added to your friend list")
            msg.exec_()
        else:
            responseObject = json.loads(normalResponse.data)
            msg = QMessageBox()
            msg.setWindowTitle("Cannot add " + friendIngame)
            msg.setText(responseObject["message"])
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

    def getFriendList(self):
        for x in range(6):
            friendList = FriendList()
            self.verticalLayout.addWidget(friendList)
            friendList.ingame.setText("ingame " + f'{x + 1}')