import string


class NormalResponse:
    code: int
    data: string
    type: string

    def __init__(self, type, code, data):
        self.code = code
        self.type = type
        self.data = data

class ActiveResponse:
    type: string
    data: string

    def __init__(self,type,data):
        self.type = type
        self.data = data