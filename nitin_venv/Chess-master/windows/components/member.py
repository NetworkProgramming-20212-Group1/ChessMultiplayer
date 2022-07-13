from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget

class Member(QWidget):
    def __init__(self):
        super(Member,self).__init__()
        loadUi("member.ui",self)