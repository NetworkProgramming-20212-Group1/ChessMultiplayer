from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget

class MatchHistory(QWidget):
    def __init__(self):
        super(MatchHistory,self).__init__()
        loadUi("matchHistory.ui",self)     