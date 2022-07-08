import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
from gui import ChessWindow
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from navbar import Navbar

print("File test __name__ is set to: {}" .format(__name__))
class RegisterLogin(QWidget):
    def __init__(self):
        super(RegisterLogin,self).__init__()
        loadUi("../wui/login_Register.ui",self)
        self.input_log_username.setFocusPolicy(Qt.StrongFocus)
        self.input_log_username.setFocus()
        self.input_log_username.returnPressed.connect(self.loginButton.click)
        self.input_log_pw.returnPressed.connect(self.loginButton.click)
        self.loginButton.clicked.connect(self.checkLogin)
        self.input_reg_username.returnPressed.connect(self.registerButton.click)
        self.input_reg_pw.returnPressed.connect(self.registerButton.click)
        self.input_reg_ingame.returnPressed.connect(self.registerButton.click)
        self.registerButton.clicked.connect(self.checkRegister)
    
    def checkRegister(self):
        reg_username = self.input_reg_username.text()
        reg_pw = self.input_reg_pw.text()
        reg_ingame = self.input_reg_ingame.text()
        if(not reg_username):
            self.inf_reg_usr.setText("Please enter your username")
            self.input_reg_username.setFocus()
        elif(not reg_pw):
            self.inf_reg_pw.setText("Please enter your password")
            self.input_reg_pw.setFocus()
        elif(not reg_ingame):
            self.inf_reg_ing.setText("Please enter your ingame")
            self.input_reg_ingame.setFocus()
        else:
            self.inf_reg_usr.setText("")
            self.inf_reg_pw.setText("")
            self.inf_reg_ing.setText("")
            print("Input username: " + reg_username + ", input password: " + reg_pw + ", input ingame: " + reg_ingame)
            # send the information to server to check
            self.gotoLogin()

    def checkLogin(self):
        log_username = self.input_log_username.text()
        log_pw = self.input_log_pw.text()
        if(not log_username):
            self.inf_log_usr.setText("Please enter your username")
            self.input_log_username.setFocus()
        elif(not log_pw):
            self.inf_log_pw.setText("Please enter your password")
            self.input_log_pw.setFocus()
        else:
            print("Input username: " + log_username + ", input password: " + log_pw)
            # send the information to server to check
            self.gotoHome()

    def gotoLogin(self):
        self.input_log_username.setFocus(True)

    def gotoHome(self):
        mainwindow.gotoHome()

class Home(QDialog):
    def __init__(self):
        super(Home,self).__init__()
        loadUi("../wui/home.ui",self)

class Profile(QDialog):
    def __init__(self):
        super(Profile,self).__init__()
        loadUi("../wui/profile.ui",self)
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
class MatchHistory(QDialog):
    def __init__(self):
        super(MatchHistory,self).__init__()
        loadUi("../wui/matchHistory.ui",self)     

class Friend(QDialog):
    def __init__(self):
        super(Friend,self).__init__()
        loadUi("../wui/friends.ui",self)
        self.getFriendList()
        self.addFriend()

    def addFriend(self):
        self.input_friendID.returnPressed.connect(self.add_friend.click)
        self.add_friend.clicked.connect(self.addFriendCheck)

    def addFriendCheck(self):
        friendID = self.input_friendID.text()
        # send friendID to server


    def getFriendList(self):
        for x in range(6):
            friendList = FriendList()
            self.verticalLayout.addWidget(friendList)
            friendList.ingame.setText("ingame " + f'{x + 1}')

class FriendList(QDialog):
    def __init__(self):
        super(FriendList,self).__init__()
        loadUi("../wui/friendList.ui",self)     

class Group(QDialog):
    def __init__(self):
        super(Group,self).__init__()
        loadUi("../wui/group_Joined.ui",self)
        self.getMembers()
    def getMembers(self):
        for x in range(6):
            memberList = Member()
            self.verticalLayout.addWidget(memberList)
            memberList.ingame.setText("ingame " + f'{x + 1}')
class Member(QDialog):
    def __init__(self):
        super(Member,self).__init__()
        loadUi("../wui/member.ui",self)
class Play(QDialog):
    def __init__(self):
        super(Play,self).__init__()
        loadUi("../wui/play.ui",self)
        self.create_pvp.clicked.connect(self.gotoPVP)
        self.create_custom.clicked.connect(self.gotoCustom)
        self.getRoom()

    def gotoPVP(self):
        pvp = PVP()
        widget.addWidget(pvp)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(pvp)

    def gotoCustom(self):
        custom = Custom()
        widget.addWidget(custom)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(custom)

    def getRoom(self):
        for x in range(8):
            openRoom = Room()
            self.verticalLayout_2.addWidget(openRoom)
            openRoom.roomID.setText("room " + f'{x + 1}')

class Room(QDialog):
    def __init__(self):
        super(Room,self).__init__()
        loadUi("../wui/room.ui",self)
class PVP(QDialog):
    def __init__(self):
        super(PVP,self).__init__()
        loadUi("../wui/pvp.ui",self)
        self.play.clicked.connect(self.gotoChessBoard)

    def gotoChessBoard(self):
        self.window = ChessWindow()
        self.window.show()
class Custom(QDialog):
    def __init__(self):
        super(Custom,self).__init__()
        loadUi("../wui/custom.ui",self)
        self.inputMessage.returnPressed.connect(self.sendMessage.click)
        self.sendMessage.clicked.connect(self.getMessage)
        self.play.clicked.connect(self.gotoChessBoard)

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

    def gotoChessBoard(self):
        self.window = ChessWindow()
        self.window.show()

class Chat(QDialog):
    def __init__(self):
        super(Chat,self).__init__()
        loadUi("../wui/chat.ui",self)

class Notification(QDialog):
    def __init__(self):
        super(Notification,self).__init__()
        loadUi("../wui/notification.ui",self)
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("../wui/mainwindow.ui",self)
        self.show()
        self.getNotification()
        Navbar.handler(self)

    def getNotification(self):
        # get from server
        notification = Notification()
        self.gridLayout_2.addWidget(notification)
        notification.noti.setText("")

    def gotoRegister(self):
        reglog=RegisterLogin()
        widget.removeWidget(widget.currentWidget())
        self.leftWidget.hide()
        self.rightWidget.hide()
        widget.addWidget(reglog)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(reglog)

    def gotoHome(self):
        home=Home()
        self.rightWidget.show()
        self.leftWidget.show()
        widget.removeWidget(widget.currentWidget())
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(home)

    def gotoProfile(self):
        profile=Profile()
        widget.removeWidget(widget.currentWidget())
        widget.addWidget(profile)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(profile)

    def gotoFriend(self):
        friend=Friend()
        widget.removeWidget(widget.currentWidget())
        widget.addWidget(friend)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(friend)

    def gotoGroup(self):
        group=Group()
        widget.removeWidget(widget.currentWidget())
        widget.addWidget(group)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(group)

    def gotoPlay(self):
        play=Play()
        widget.removeWidget(widget.currentWidget())
        widget.addWidget(play)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(play)

    def gotoLogout(self):
        reglog=RegisterLogin()
        widget.removeWidget(widget.currentWidget())
        self.leftWidget.hide()
        self.rightWidget.hide()
        widget.addWidget(reglog)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(reglog)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    mainwindow=MainWindow()
    widget =mainwindow.stackedWidget
    widget.setMinimumSize(600, 450)
    mainwindow.gotoRegister()
    app.exec_()