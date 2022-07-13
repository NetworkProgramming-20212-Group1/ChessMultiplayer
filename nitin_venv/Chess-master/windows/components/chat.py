from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget

class Chat(QWidget):
    def __init__(self):
        super(Chat,self).__init__()
        loadUi("chat.ui",self)