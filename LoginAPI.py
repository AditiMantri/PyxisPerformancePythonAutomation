from payload import *
from Utilities.configurations import *
from Utilities.resources import *
import requests

url = getConfig()['API']['endpoint'] + apiResources.login

loginResponse = requests.post(url,
                              json=loginPayload())
response_json = loginResponse.json()
print(response_json)
token = response_json['data']['key']
setToken(token)

assert loginResponse.status_code == 200
assert response_json['error'] == False
