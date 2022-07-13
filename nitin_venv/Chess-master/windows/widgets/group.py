from PyQt5.uic import loadUi
from components.member import Member
from PyQt5.QtWidgets import QWidget

class Group(QWidget):
    def __init__(self):
        super(Group,self).__init__()
        loadUi("group_Joined.ui",self)
        self.getMembers()
    def getMembers(self):
        for x in range(6):
            memberList = Member()
            self.verticalLayout.addWidget(memberList)
            memberList.ingame.setText("ingame " + f'{x + 1}')