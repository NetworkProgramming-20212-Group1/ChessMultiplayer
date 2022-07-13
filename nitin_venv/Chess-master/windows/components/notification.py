from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget

class Notification(QWidget):
    def __init__(self):
        super(Notification,self).__init__()
        loadUi("notification.ui",self)