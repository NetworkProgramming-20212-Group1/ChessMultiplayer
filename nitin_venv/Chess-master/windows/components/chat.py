from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget

class Chat(QWidget):
    def __init__(self, message):
        super(Chat,self).__init__()
        loadUi("chat.ui",self)
        self.message = message
        self.eventHandler(self.message)

    def eventHandler(self, message):
        self.input_message.setText(message)