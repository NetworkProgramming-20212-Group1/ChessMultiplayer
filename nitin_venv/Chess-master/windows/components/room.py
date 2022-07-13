from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget

class Room(QWidget):
    def __init__(self):
        super(Room,self).__init__()
        loadUi("room.ui",self)