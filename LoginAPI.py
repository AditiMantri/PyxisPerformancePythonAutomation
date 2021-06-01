from payload import *

from Utilities.log import custom_logger as log

log = log()

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
#
# now = datetime.utcnow()
# print(now.strftime("%Y-%m-%dT%H:%M"))
#
# url = "https://report-staging.aiquire.com/api/api/clients/136/media-plans/?objective=CONVERSIONS"
# Authorization = {'Authorization': 'Token f0b3ff6d5da1431c3ba92dc690174a3183567490'}
# getMediaPlan_response = requests.get(url, headers=Authorization)
# json = getMediaPlan_response.json()
# values = []
# for result in json['data']:
#     values.append(result['id'])
# log.debug(values)
# log.debug("Max")
# log.debug(max(values))
#
# id1 = -1
# log.debug(len(values))
# for value in values:
#     id1 = id1 + 1
#     if value == max(values):
#         break
# log.debug(id1)
#
# log.debug(json['data'][id1])


hashCode = payload.get_token_hash({
            "client_id": 136,
            "media_plan_id": 888,
        })
print(hashCode)
