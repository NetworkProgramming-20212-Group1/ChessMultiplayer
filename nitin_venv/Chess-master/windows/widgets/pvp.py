from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget, QMainWindow
from response import *
from request import *

class PVP(QWidget):
    def __init__(self, mainwindow: QMainWindow):
        super(PVP,self).__init__()
        self.mainwindow = mainwindow
        loadUi("pvp.ui",self)
        self.eventHandler()
    
    def eventHandler(self):
        self.playButton.clicked.connect(self.findOpponent)
        self.cancelButton.clicked.connect(self.cancel)
        # self.playButton.clicked.connect(self.mainwindow.gotoChessBoard)

    def findOpponent(self):
        self.status.setText("Finding your opponent...")

    def cancel(self):
        self.status.setText("Click play to find your opponent")
