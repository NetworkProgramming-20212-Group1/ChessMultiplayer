import string
import sys, os
import time
from typing import Dict
os.chdir('../wui')
from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from components.navbar import Navbar
from components.notification import Notification
from widgets.loginregister import RegisterLogin
from widgets.home import Home
from widgets.profile import Profile
from widgets.friends import Friend
from widgets.play import Play
from widgets.custom import Custom
from widgets.pvp import PVP
from gui import *
import socket
import threading
from datetime import datetime
from request import *
from response import *
class MainWindow(QMainWindow):
    normal_response = []
    active_response = []
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("mainwindow.ui",self)
        self.center()
        self.show()
        Navbar.handler(self)
        global ingame
        host = '127.0.0.1'
        port = 1234
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect((host,port))
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def gotoRegister(self):
        reglog=RegisterLogin(mainwindow)
        # widget.removeWidget(widget.currentWidget())
        self.leftWidget.hide()
        self.scrollArea.hide()
        widget.addWidget(reglog)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(reglog)

    def gotoHome(self):
        home=Home(self.ingame)
        self.scrollArea.show()
        self.leftWidget.show()
        # widget.removeWidget(widget.currentWidget())
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(home)
        self.getNotification(mainwindow)

    def getNotification(self, mainwindow):
        notification = Notification(mainwindow)
        self.verticalLayout_3.addWidget(notification)

    def gotoProfile(self):
        profile=Profile(mainwindow)
        # widget.removeWidget(widget.currentWidget())
        widget.addWidget(profile)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(profile)

    def gotoFriend(self):
        friend=Friend(mainwindow)
        # widget.removeWidget(widget.currentWidget())
        widget.addWidget(friend)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(friend)

    def gotoPlay(self):
        play=Play(mainwindow)
        # widget.removeWidget(widget.currentWidget())
        widget.addWidget(play)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(play)

    def gotoPVP(self):
        pvp = PVP(mainwindow)
        widget.addWidget(pvp)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(pvp)

    def gotoCustom(self, responseObject: Dict):
        custom = Custom(mainwindow, responseObject)
        widget.addWidget(custom)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(custom)

    def gotoLogout(self):
        logoutObject = LogoutObject(self.ingame)
        self.sendRequest(createRequest("LOUT",logoutObject))
        reglog=RegisterLogin(mainwindow)
        # widget.removeWidget(widget.currentWidget())
        self.leftWidget.hide()
        self.scrollArea.hide()
        widget.addWidget(reglog)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(reglog)
        msg = QMessageBox()
        msg.setWindowTitle("")
        msg.setText("Logout successfully!")
        msg.exec_()

    def gotoChessBoard(self, id, color):
        self.chessWindow = ChessWindow(mainwindow, id, color)
        self.chessWindow.show()
        
    def getCurrentIndex(self):
        return widget.currentIndex()

    def sendRequest(self, message: string):
        if message=="close":
            self.s.close()
        message+='\n'
        print(message)
        self.s.send(message.encode('ascii'))

    def getResponse(self,rtype: string) -> NormalResponse:
        #get request from mainwindow
        timeout = 1   # [seconds]
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            x: NormalResponse
            for x in self.normal_response:
                if x.type == rtype:
                    self.normal_response.remove(x)
                    # print(x)        
                    return x
            # if more than 1s -> break;
        return None

    def getActiveResponse(self, rtype: string) -> ActiveResponse:
        #get request from mainwindow
        timeout = 1   # [seconds]
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            x: ActiveResponse 
            for x in self.active_response:
                if x.type == rtype:
                    self.active_response.remove(x)
                    return x
            # if more than 1s -> break;
        return None

def getRequest(s, normal_response, active_response):
    while True:
        # print(normal_response)
        data: string = s.recv(10000).decode('ascii')
        begin = data[0:4]
        if begin == "REPL":
            response = [data[0:4],data[5:9], data[10:13], data[14:]]
            normal_response.append(NormalResponse(response[1], int(response[2]), response[3]))
        else :
            response = [data[0:4],data[5:]]
            active_response.append(ActiveResponse(response[0], response[1]))

        with open('../windows/server_response.txt', 'a') as f:
            output = '['+datetime.now().strftime("%H:%M:%S")+']: '+data
            f.write(output)

           

if __name__ == "__main__":
    app=QApplication(sys.argv)
    mainwindow=MainWindow()
    widget =mainwindow.stackedWidget
    widget.setMinimumSize(800, 600)
    mainwindow.gotoRegister()
   
    try:
        t1 = threading.Thread(target=getRequest, args=(mainwindow.s,mainwindow.normal_response, mainwindow.active_response))
        t1.start()
    except:
        print ("error")

    app.exec_()