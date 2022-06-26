
from PyQt5 import QtCore, QtGui, QtWidgets
from profile import Ui_profile
from friends import Ui_friends
from group_Joined import Ui_Group_Joined
from group_Not_Join import Ui_Group_Not_Joined
from play import Ui_play
from login_Register import Ui_account


class Nav_bar(object):
    def profile_Navbar(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_profile()
        self.ui.setupUi(self.window)
        self.window.show()
    def friends_Navbar(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_friends()
        self.ui.setupUi(self.window)
        self.window.show()
    def group_Navbar(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Group_Joined()
        self.ui.setupUi(self.window)
        self.window.show()
    def play_Navbar(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_play()
        self.ui.setupUi(self.window)
        self.window.show()
    def Logout_Navbar(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_account()
        self.ui.setupUi(self.window)
        self.window.show()

    