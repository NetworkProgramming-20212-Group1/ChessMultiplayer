
class Navbar():
    def handler(home):
        home.home_button.clicked.connect(home.gotoHome)
        home.profile_button.clicked.connect(home.gotoProfile)
        home.friend_button.clicked.connect(home.gotoFriend)
        home.play_button.clicked.connect(home.gotoPlay)
        home.logout_button.clicked.connect(home.gotoLogout)   

