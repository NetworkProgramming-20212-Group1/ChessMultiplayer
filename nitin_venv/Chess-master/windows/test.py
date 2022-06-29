import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QStackedWidget
from PyQt5.uic import loadUi
from navbar import Navbar

class RegisterLogin(QDialog):
    def __init__(self):
        super(RegisterLogin,self).__init__()
        loadUi("wui/login_Register.ui",self)
        self.registerButton.clicked.connect(self.checkRegister)
        self.loginButton.clicked.connect(self.checkLogin)
    
    def checkRegister(self):
        reg_username = self.input_reg_username.text()
        reg_pw = self.input_reg_pw.text()
        reg_ingame = self.input_reg_ingame.text()
        if(not reg_username):
            self.inf_reg_usr.setText("Please enter your username")
        elif(not reg_pw):
            self.inf_reg_pw.setText("Please enter your password")
        elif(not reg_ingame):
            self.inf_reg_ing.setText("Please enter your ingame")
        else:
            print("Input username: " + reg_username + ", input password: " + reg_pw + ", input ingame: " + reg_ingame)
            # send the information to server to check
            self.gotoLogin()

    def checkLogin(self):
        log_username = self.input_log_username.text()
        log_pw = self.input_log_pw.text()
        if(not log_username):
            self.inf_log_usr.setText("Please enter your username")
        elif(not log_pw):
            self.inf_log_pw.setText("Please enter your password")
        else:
            print("Input username: " + log_username + ", input password: " + log_pw)
            # send the information to server to check
            self.gotoHome()

    def gotoLogin(self):
        self.input_log_username.setFocus(True)
    def gotoHome(self):
        MainWindow.gotoHome()
class Home(QDialog):
    def __init__(self):
        super(Home,self).__init__()
        loadUi("wui/home.ui",self)

class Profile(QDialog):
    def __init__(self):
        super(Profile,self).__init__()
        loadUi("wui/profile.ui",self)
        rank = self.getRank()
        level = self.getLevel()
        self.rank_inf.setText(rank)
        self.level_inf.setText(level)

    def getRank(self): 
        # get rank from server
        rank = "gold"
        return rank
    def getLevel(self):
        # get level from server
        level = "1"
        return level
    def getMatchHistory():
        # get match history from server
        pass

class Friend(QDialog):
    def __init__(self):
        super(Friend,self).__init__()
        loadUi("wui/friends.ui",self)
class Group(QDialog):
    def __init__(self):
        super(Group,self).__init__()
        loadUi("wui/group_Joined.ui",self)
class Play(QDialog):
    def __init__(self):
        super(Play,self).__init__()
        loadUi("wui/play.ui",self)
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("wui/mainwindow.ui",self)
        self.show()
        Navbar.handler(self)

    def gotoRegister(self):
        reglog=RegisterLogin(super(MainWindow, self))
        self.leftWidget.hide()
        widget.addWidget(reglog)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(reglog)

    def gotoHome(self):
        home=Home()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(home)

    def gotoProfile(self):
        profile=Profile()
        widget.addWidget(profile)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(profile)

    def gotoFriend(self):
        friend=Friend()
        widget.addWidget(friend)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(friend)

    def gotoGroup(self):
        group=Group()
        widget.addWidget(group)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(group)

    def gotoPlay(self):
        play=Play()
        widget.addWidget(play)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(play)

    def gotoLogout(self):
        reglog=RegisterLogin()
        widget.addWidget(reglog)
        # print(widget.currentIndex())
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(reglog)


app=QApplication(sys.argv)
mainwindow=MainWindow()
widget =mainwindow.stackedWidget
mainwindow.gotoRegister()
app.exec_()