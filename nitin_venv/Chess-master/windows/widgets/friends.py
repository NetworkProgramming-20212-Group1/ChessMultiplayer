import time
from PyQt5.uic import loadUi
from components.friendList import FriendList
from PyQt5.QtWidgets import QWidget, QMainWindow, QMessageBox
from PyQt5 import QtCore
from request import *
from response import *
import threading

class Friend(QWidget):
    socketSignal = QtCore.pyqtSignal(object)

    def __init__(self, mainwindow: QMainWindow):
        super(Friend,self).__init__()
        loadUi("friends.ui",self)
        self.mainwindow = mainwindow
        self.ingame = self.mainwindow.ingame
        self.addFriend()
        self.socketSignal.connect(self.addNewWidget)
        try:
            t1 = threading.Thread(target=self.getFriendList, args=(), daemon=True)
            t1.start()
        except:
            print ("create thread error")

    def addFriend(self):
        self.input_friendIngame.returnPressed.connect(self.add_friend.click)
        self.add_friend.clicked.connect(self.addFriendCheck)

    def addFriendCheck(self):
        friendIngame = self.input_friendIngame.text()
        add_friendObject = AddFriendObject(friendIngame)
        self.mainwindow.sendRequest(createRequest("ADFR",add_friendObject))
        self.input_friendIngame.setText("")
        normalResponse: NormalResponse = self.mainwindow.getResponse("ADFR")
        if(normalResponse):
            if(normalResponse.code < 400):
                msg = QMessageBox() 
                msg.setWindowTitle("")
                msg.setText("Request sent")
                msg.exec_()
            else:
                responseObject = json.loads(normalResponse.data)
                msg = QMessageBox()
                msg.setWindowTitle("Cannot add " + friendIngame)
                msg.setText(responseObject["message"])
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()

    def getFriendList(self):
        while True:
            getFriendListObject = FriendListObject(self.ingame)
            self.mainwindow.sendRequest(createRequest("FRND", getFriendListObject))
            normalResponse: NormalResponse = self.mainwindow.getResponse("FRND")
            if(normalResponse):
                if(normalResponse.code < 400):
                    responseObject = json.loads(normalResponse.data)
                    for x in responseObject:
                        self.socketSignal.emit(x)
            self.clearDisplay()
            time.sleep(3)

    def addNewWidget(self, x):
        friendList = FriendList(x)
        self.verticalLayout.addWidget(friendList)


    def clearDisplay(self):
        for i in reversed(range(self.verticalLayout.count())): 
            widgetToRemove = self.verticalLayout.itemAt(i).widget()
            # remove it from the layout list
            self.verticalLayout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.deleteLater()
