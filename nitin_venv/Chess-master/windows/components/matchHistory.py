from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget

class MatchHistory(QWidget):
    def __init__(self, x):
        super(MatchHistory,self).__init__()
        loadUi("matchHistory.ui",self)    
        self.x = x
        self.eventhandler(self.x)

    def eventhandler(self, x):
        id = x["id"]
        self.matchID.setText(f"match ID: {id}")
        whiteIngame = x["white"]
        blackIngame = x["black"]
        self.color.setText(f"white: {whiteIngame}, black: {blackIngame}")
        type = x["type"]
        self.type.setText(f"mode: {type}")
        winnerIngame = x["winner"]
        self.winner.setText(f"winner: {winnerIngame}")
        move = x["state"]
        self.move.setText(move)