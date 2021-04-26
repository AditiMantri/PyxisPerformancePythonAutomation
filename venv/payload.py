import payload
#
# #global variable
# token = "Key value comes here"
# clientID = 0
# adaccountID = 0


def loginPayload(login, password):
    body = {
        "email" : login,
        "password" : password
    }
    return body

def setToken(token):
    payload.token = token

def getToken():
    return "Token "+token

def setClientID(clientID):
    payload.clientID = clientID

def getClientID():
    return payload.clientID

def setAdaccountID(adaccountnID):
    payload.adaccountID = adaccountnID

def getAdaccountID():
    return payload.adaccountID;

def saveConfig(config):
    payload.config = config
