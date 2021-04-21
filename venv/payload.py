

def loginPayload():
    body = {
        "email" : "test@aiquire.com",
        "password" : "123456"
    }
    return body

class gettersAndSetters:

    def __init__(self, token = ""):
        self.token = token

    def setToken(self, token):
        self.token = "Token " + token

    def getToken(self):
        return self.token
