from ast import Dict

class HttpRequest:
    def __init__(self, body: Dict = None, param: Dict = None):
        self.body = body 
        self.param = param 