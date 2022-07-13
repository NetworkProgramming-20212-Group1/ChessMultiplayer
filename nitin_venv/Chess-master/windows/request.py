import string
import json

def createRequest(type:string, object):
    return type + ' ' + json.dumps(object.__dict__)

class LoginObject: 
    username: string
    password: string

    def __init__(self, username, password):
        self.username = username
        self.password = password

class RegisterObject:
    username: string
    password: string
    ingame: string

    def __init__(self, username, password, ingame):
        self.username = username
        self.password = password
        self.ingame = ingame

class LogoutObject:
    ingame: string

    def __init__(self, ingame):
        self.ingame = ingame

class AddFriendObject: 
    ingame: string

    def __init__(self, ingame):
        self.ingame = ingame

class CreateRoomObject:
    id: string
    password: string
    type: string

    def __init__(self, id, password, matchType):
        self.id = id
        self.password = password
        self.type = matchType

class LeaveRoomObject:
    roomid: string

    def __init__(self, roomid):
        self.roomid = roomid
        
class PlayObject: 
    roomid: string

    def __init__(self, roomid):
        self.roomid = roomid
