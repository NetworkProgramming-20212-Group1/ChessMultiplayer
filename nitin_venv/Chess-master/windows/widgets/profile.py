from PyQt5.uic import loadUi
from components.matchHistory import MatchHistory
from PyQt5.QtWidgets import QWidget

class Profile(QWidget):
    def __init__(self):
        super(Profile,self).__init__()
        loadUi("profile.ui",self)
        rank = self.getRank()
        level = self.getLevel()
        self.rank_inf.setText(rank)
        self.level_inf.setText(level)
        self.getMatchHistory()

    def getRank(self): 
        # get rank from server
        rank = "gold"
        return rank
    def getLevel(self):
        # get level from server
        level = "1"
        return level
    def getMatchHistory(self):
        for x in range(6):
            matchHistory = MatchHistory()
            self.verticalLayout.addWidget(matchHistory)
            matchHistory.Match.setText("match " + f'{x + 1}')