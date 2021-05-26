import random

import payload
from payload import *
from Utilities.configurations import *
from Utilities.resources import *
import requests
from Utilities.log import custom_logger as log
from Utilities.configurations import *
from Utilities.resources import *

# url = getConfig()["API"]['endpoint'] + apiResources.login
#
# loginResponse = requests.post(url,
#                               json=loginPayload())
# response_json = loginResponse.json()
# print(response_json)
# token = response_json['data']['key']
# setToken(token)
# print(getToken())

# assert loginResponse.status_code == 200
# assert response_json['error'] == False

# for next apis use auth for authentication - tokens
# api.response = requests.get(url, auth=('token', 'token value'))


# endpoint = '/api/experiment_setup/clients/122/adaccount/112/create/'
# url = getConfig()['API']['endpoint'] + endpoint
# Authorization = {'Authorization': 'Token f0b3ff6d5da1431c3ba92dc690174a3183567490'}
#
# check = requests.post(url=url,
#                       headers=Authorization,
#                       json=payload.setLeadGenBody())
# print(check)
# print(check.text)

# check = requests.post(url=url, headers=Authorization, json=json.load("C:\\Users\\Aditi
# Mantri\\PycharmProjects\\PyxisPerformancePythonAutomation\\jsonBody\\CreateExpSetupLeadGen")) print(check.text)
#
# print("{}{}{}".format(apiResources.getExpSetup, 106, '/'))

endpoint = "{}{}{}{}".format(apiResources.api, apiResources.getAdaccount, "2/",
                             apiResources.metric)
url = getConfig()['API']['endpoint'] + endpoint
print(url)
Auth = {'Authorization': "Token f0b3ff6d5da1431c3ba92dc690174a3183567490"}
header = {
    "date_preset": "last_60d",
    "objective": "CONVERSIONS",
    "event": "fb_primary_actions_offsite_conversion_custom_519972278674063"
}
response = requests.get(url, headers=Auth, params=header)
print(response.text)
