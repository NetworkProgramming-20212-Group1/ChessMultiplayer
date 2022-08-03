from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget, QMainWindow, QMessageBox
from response import *
from request import *
import threading
class Notification(QWidget):
    
    def __init__(self, mainwindow: QMainWindow):
        super(Notification,self).__init__()
        loadUi("notification.ui",self)
        self.mainwindow = mainwindow
        self.yes.hide()
        self.no.hide()
        self.request_from_ingame = ""
        self.yes.clicked.connect(lambda: self.acceptFriendRequest(self.request_from_ingame))
        self.no.clicked.connect(lambda: self.denyFriendRequest(self.request_from_ingame))
        try:
            t1 = threading.Thread(target=self.action, args=(), daemon=True)
            t1.start()
        except:
            print ("create thread error")

    def action(self):
        while True:
            friend_requestResponseObject: ActiveResponse = self.mainwindow.getActiveResponse("FRRQ")
            if friend_requestResponseObject:
                friend_request = json.loads(friend_requestResponseObject.data)
                self.request_from_ingame = friend_request["ingame"]
                print("Friend request from " + self.request_from_ingame)
                self.noti.setText(self.request_from_ingame + " has sent you a friend request")
                self.yes.show()
                self.no.show()

    def acceptFriendRequest(self, ingame):
        self.deleteLater()
        accept_friendObject = AcceptFriendObject(ingame)
        self.mainwindow.sendRequest(createRequest("ACFR", accept_friendObject))
        normalResponse: NormalResponse = self.mainwindow.getResponse("ACFR")
        if(normalResponse):
            if(normalResponse.code < 400):
                msg = QMessageBox()
                msg.setWindowTitle("")
                msg.setText(ingame + " was added to your friend list")
                msg.exec_()

            else:
                responseObject = json.loads(normalResponse.data)
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText(responseObject["message"])
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()

    def denyFriendRequest(self, ingame):
        self.yes.hide()
        self.no.hide()
        self.noti.setText("Friend request from " + ingame + " was denied")
 