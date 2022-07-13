from typing import Dict
from PyQt5.uic import loadUi
from components.chat import Chat
from PyQt5.QtWidgets import QWidget, QMainWindow, QMessageBox
from response import *
from request import *

class Custom(QWidget):
    def __init__(self, mainwindow: QMainWindow, responseObject: Dict):
        super(Custom,self).__init__()
        self.mainwindow = mainwindow
        loadUi("custom.ui",self)
        self.getRoomInfo(responseObject)
        self.leaveButton.clicked.connect(lambda: self.leaveRoom(responseObject))
        self.playButton.clicked.connect(lambda: self.play(responseObject))
        self.inputMessage.returnPressed.connect(self.sendMessage.click)
        self.sendMessage.clicked.connect(self.getMessage)

    def getRoomInfo(self, responseObject: Dict):
        roomid = responseObject["id"]
        white = responseObject["white"]
        isWhiteOwner = responseObject["isWhiteOwner"]
        self.room.setText("Room " + roomid)
        if(isWhiteOwner):
            self.ingame1.setText(white + "(host)")
        else:
            if "black" in responseObject:
                black = responseObject["black"]
                self.ingame2.setText(black + "(host)")

    def play(self, responseObject: Dict):
        if "black" in responseObject:
            self.mainwindow.gotoChessBoard()
        else:
            self.playButton.setEnabled(False)
            msg = QMessageBox()
            msg.setWindowTitle("Cannot start the match")
            msg.setText("Opponent has not joined the room")
            msg.exec_()

    def leaveRoom(self, responseObject: Dict):
        roomid = responseObject["id"]
        leaveRoomObject = LeaveRoomObject(roomid)
        self.mainwindow.sendRequest(createRequest("LVRM",leaveRoomObject))
        normalResponse: NormalResponse = self.mainwindow.getResponse("LVRM")
        if(normalResponse.code < 400):
            self.mainwindow.gotoPlay()
            msg = QMessageBox()
            msg.setWindowTitle("")
            msg.setText("You have just left the room " + roomid)
            msg.exec_()
        # else:
        #     responseObject = json.loads(normalResponse.data)

    def getMessage(self):
        input_message = self.inputMessage.text()
        if(input_message):
            chat = Chat()
            area = self.scrollArea
            vbar = area.verticalScrollBar()
            vbar.setValue(vbar.maximum())
            self.grid.addWidget(chat)  
            self.inputMessage.setText("")      
            chat.message.setText("You: " + input_message)
        # get another client's message from server