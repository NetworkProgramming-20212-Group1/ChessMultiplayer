from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget

class FriendList(QWidget):
    def __init__(self):
        super(FriendList,self).__init__()
        loadUi("friendList.ui",self)   