import string
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget

class Home(QWidget):
    def __init__(self, inGame: string):
        super(Home,self).__init__()
        loadUi("home.ui",self)
        self.inGame = inGame
        self.label_welcome.setText("Welcome " + self.inGame + " !")