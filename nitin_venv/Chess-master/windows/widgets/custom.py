from typing import Dict
from PyQt5.uic import loadUi
from components.chat import Chat
from PyQt5.QtWidgets import QWidget, QMainWindow, QMessageBox
from PyQt5 import QtCore
from response import *
from request import *
import threading
from threading import main_thread
should_go_to_play = threading.Event()

class Custom(QWidget):
    socketSignal = QtCore.pyqtSignal(object) #must be defined in class level

    def __init__(self, mainwindow: QMainWindow, responseObject: Dict):
        super(Custom,self).__init__()
        self.mainwindow = mainwindow
        loadUi("custom.ui",self)
        self.roomid = responseObject["id"]
        self.getRoomInfo(responseObject)
        self.leaveButton.clicked.connect(lambda: self.leaveRoom(responseObject))
        self.playButton.clicked.connect(lambda: self.play())
        self.inputMessage.returnPressed.connect(self.sendMessage.click)
        self.sendMessage.clicked.connect(self.getMessage)
        self.socketSignal.connect(self.getPlay)
        self.isWhiteOwner= responseObject["isWhiteOwner"]

        try:
            t1 = threading.Thread(target=self.checkJoin, args=(), daemon=True)
            t1.start()
        except:
            print ("create thread error")

                
    def setHost(self, isWhiteOwner: bool):
        self.isWhiteOwner = isWhiteOwner
        if(isWhiteOwner):
            self.ingame1.setStyleSheet("color: red")
            self.ingame2.setStyleSheet("color: green")
        else:
            self.ingame1.setStyleSheet("color: green")
            self.ingame2.setStyleSheet("color: red")

    def checkJoin(self ):
        while 1:
            leaveResponseObject: ActiveResponse = self.mainwindow.getActiveResponse("OLVR");
            if leaveResponseObject:
                leaveResponse = json.loads(leaveResponseObject.data)
                isWhiteOwner = leaveResponse["isWhiteOwner"]
                self.setHost(isWhiteOwner)
                if isWhiteOwner:
                    self.ingame2.setText("Guest")
                else:
                    self.ingame1.setText("Guest")

            activeResponse: ActiveResponse = self.mainwindow.getActiveResponse("JOIN");
            if activeResponse:
                responseObject = json.loads(activeResponse.data)
                ingame = responseObject["ingame"]
                if self.ingame1.text() == "Guest":
                    self.ingame1.setText(ingame)
                elif self.ingame2.text() == "Guest":
                    self.ingame2.setText(ingame)

            playResponse: ActiveResponse = self.mainwindow.getActiveResponse("STRT");
            if playResponse:
                responseObject = json.loads(playResponse.data)
                match = responseObject["match"]
                id = match["id"]
                self.socketSignal.emit({'id': id, 'match': match})

    def getRoomInfo(self, responseObject: Dict):
        isWhiteOwner = responseObject["isWhiteOwner"]
        self.room.setText("Room " + self.roomid)
        self.setHost(isWhiteOwner)
        if(isWhiteOwner):
            if "white" in responseObject:
                white = responseObject["white"]
                self.ingame1.setText(white)
            if "black" in responseObject:
                black = responseObject["black"]
                self.ingame2.setText(black)
        else:
            if "white" in responseObject:
                white = responseObject["white"]
                self.ingame1.setText(white)
            if "black" in responseObject:
                black = responseObject["black"]
                self.ingame2.setText(black)

    def getPlay(self, object):
        if self.isWhiteOwner and self.mainwindow.ingame == object["match"]["white"]:
            self.mainwindow.gotoChessBoard(object["id"],'W')
        else:
            self.mainwindow.gotoChessBoard(object["id"], 'B')

    def play(self):
        if self.ingame1.text() != "Guest" and self.ingame2.text() != "Guest":
            playObject = PlayObject(self.roomid)
            self.mainwindow.sendRequest(createRequest("PLAY",playObject))
            normalResponse: NormalResponse = self.mainwindow.getResponse("PLAY")
            if(normalResponse):
                if(normalResponse.code < 400):
                    responseObject = json.loads(normalResponse.data)
                    match = responseObject["match"]
                    id = match["id"]
                    if self.isWhiteOwner and self.mainwindow.ingame == match["white"]:
                        self.mainwindow.gotoChessBoard(id, 'W')
                    else:
                        self.mainwindow.gotoChessBoard(id, 'B')
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
        if(normalResponse):
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