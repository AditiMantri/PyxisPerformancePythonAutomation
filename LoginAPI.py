from payload import *
from Utilities.configurations import *
from Utilities.resources import *
import requests

url = getConfig()["API"]['endpoint'] + apiResources.login

loginResponse = requests.post(url,
                              json=loginPayload())
response_json = loginResponse.json()
print(response_json)
token = response_json['data']['key']
setToken(token)
print(getToken())

assert loginResponse.status_code == 200
assert response_json['error'] == False

# for next apis use auth for authentication - tokens
# api.response = requests.get(url, auth=('token', 'token value'))
