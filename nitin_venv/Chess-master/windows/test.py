import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from navbar import Navbar

class RegisterLogin(QDialog):
    def __init__(self):
        super(RegisterLogin,self).__init__()
        loadUi("login_Register.ui",self)
        self.registerButton.clicked.connect(self.checkRegister)
        self.loginButton.clicked.connect(self.checkLogin)

    def checkRegister(self):
        self.gotoLogin()
    def checkLogin(self):
        self.gotoHome()
    def gotoLogin(self):
        self.input_log_username.setFocus(True)
    def gotoHome(self):
        home=Home()
        widget.addWidget(home)
        print(widget.currentIndex())
        widget.setCurrentIndex(widget.currentIndex()+1)

class Home(QDialog):
    def __init__(self):
        super(Home,self).__init__()
        loadUi("home.ui",self)
        Navbar.handler(self)

    def gotoProfile(self):
        profile=Profile()
        widget.addWidget(profile)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoFriend(self):
        friend=Friend()
        widget.addWidget(friend)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoGroup(self):
        group=Group()
        widget.addWidget(group)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoPlay(self):
        play=Play()
        widget.addWidget(play)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoLogout(self):
        reglog=RegisterLogin()
        widget.addWidget(reglog)
        print(widget.currentIndex())
        widget.setCurrentIndex(widget.currentIndex()+1)

class Profile(QDialog):
    def __init__(self):
        super(Profile,self).__init__()
        loadUi("profile.ui",self)
        Navbar.handler(self)

    def gotoProfile(self):
        pass
    def gotoFriend(self):
        friend=Friend()
        widget.addWidget(friend)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoGroup(self):
        group=Group()
        widget.addWidget(group)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoPlay(self):
        play=Play()
        widget.addWidget(play)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoLogout(self):
        reglog=RegisterLogin()
        widget.addWidget(reglog)
        print(widget.currentIndex())
        widget.setCurrentIndex(widget.currentIndex()+1)

class Friend(QDialog):
    def __init__(self):
        super(Friend,self).__init__()
        loadUi("friends.ui",self)
        Navbar.handler(self)

    def gotoProfile(self):
        profile=Profile()
        widget.addWidget(profile)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoFriend(self):
        pass
    def gotoGroup(self):
        group=Group()
        widget.addWidget(group)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoPlay(self):
        play=Play()
        widget.addWidget(play)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoLogout(self):
        reglog=RegisterLogin()
        widget.addWidget(reglog)
        print(widget.currentIndex())
        widget.setCurrentIndex(widget.currentIndex()+1)            

class Group(QDialog):
    def __init__(self):
        super(Group,self).__init__()
        loadUi("group_Joined.ui",self)
        Navbar.handler(self)

    def gotoProfile(self):
        profile=Profile()
        widget.addWidget(profile)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoFriend(self):
        friend=Friend()
        widget.addWidget(friend)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoGroup(self):
        pass
    def gotoPlay(self):
        play=Play()
        widget.addWidget(play)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoLogout(self):
        reglog=RegisterLogin()
        widget.addWidget(reglog)
        print(widget.currentIndex())
        widget.setCurrentIndex(widget.currentIndex()+1)

class Play(QDialog):
    def __init__(self):
        super(Play,self).__init__()
        loadUi("play.ui",self)
        Navbar.handler(self)

    def gotoProfile(self):
        profile=Profile()
        widget.addWidget(profile)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoFriend(self):
        friend=Friend()
        widget.addWidget(friend)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoGroup(self):
        group=Group()
        widget.addWidget(group)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoPlay(self):
        pass
    def gotoLogout(self):
        reglog=RegisterLogin()
        widget.addWidget(reglog)
        print(widget.currentIndex())
        widget.setCurrentIndex(widget.currentIndex()+1)

app=QApplication(sys.argv)
mainwindow=RegisterLogin()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setMinimumSize(850, 600)
widget.setMaximumSize(1000, 800)
widget.show()
app.exec_()