import payload
from behave import *
from payload import *

from Utilities.configurations import *
from Utilities.resources import *
import requests


@given('the URL and the login credentials {login} and {password}')
def step_impl(context, login, password):
    context.url = getConfig()['API']['endpoint'] + apiResources.login
    context.payload = loginPayload(login, password)


@when(u'the Login postAPI is executed')
def step_impl(context):
    context.loginResponse = requests.post(context.url,
                                          json=context.payload)


@when(u'the user should be logged in successfully')
def step_impl(context):
    context.response_json = context.loginResponse.json()
    print(context.response_json)


@then(u'I should receive a valid HTTP response code {status_code:d}')  # d to read it as a decimal
def step_impl(context, status_code):
    assert context.loginResponse.status_code == status_code


@then(u'validate error is False')
def step_impl(context):
    assert context.response_json['error'] == False


@then(u'extract token and save it')
def step_impl(context):
    context.token = context.response_json['data']['key']
    payload.setToken(context.token)
    print(payload.getToken())


# ----------------------Step2---------------------

@given('the Authorization')
def step_impl(context):
    context.url = getConfig()['API']['endpoint'] + apiResources.clients
    context.Authorization = {'Authorization': payload.getToken()}


@when(u'the Clients GetAPI is executed')
def step_impl(context):
    context.clientResponse = requests.get(context.url,
                                          headers=context.Authorization)
    context.response_json = context.clientResponse.json()


@when(u'error should be false')
def step_impl(context):
    assert context.response_json['error'] == False


@then(u'store the client ID {ClientName}')
def step_impl(context, ClientName):
    for result in context.response_json['data']['clients']:
        if (result['name']) == ClientName:
            payload.setClientID(result['id'])
            print(result['name'])
            print(payload.getClientID())
            break


# ----------------------Step3---------------------

@given(u'the token, client id and mpadaccounts endpoint')
def step_impl(context):
    endpoint = "{}{}{}".format(apiResources.clients, payload.getClientID(), apiResources.mpadaccounts)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}


@when(u'mpadaccount GetAPI is executed')
def step_impl(context):
    context.mpadaccounts_response = requests.get(context.url,
                                                 headers=context.Authorization)
    context.mpadaccounts_response_json = context.mpadaccounts_response.json()


@when(u'the error response from mpadaccount is false')
def step_impl(context):
    assert context.mpadaccounts_response_json['error'] == False


@then('store the id if adaccount name is {adaccountName}')
def step_impl(context, adaccountName):
    for result in context.mpadaccounts_response_json['data']['adaccounts']:
        if result['name'] == adaccountName:
            payload.setAdaccountID(result['id'])
            print(format(result['name']))
            print(payload.getAdaccountID())
            break

# ----------------------Step4---------------------


@given(u'the token and getCampaignSetupFormConfig endpoint')
def step_impl(context):
    context.url = getConfig()['API']['endpoint'] + apiResources.getCampaignSetupFormConfig
    context.Authorization = {'Authorization': payload.getToken()}


@when(u'getCampaignSetupFormConfig GetAPI is executed')
def step_impl(context):
    context.getCampaignSetupFormConfig_response = requests.get(context.url,
                                                               headers=context.Authorization)
    context.getCampaignSetupFormConfig_response_json = context.getCampaignSetupFormConfig_response.json()


@when(u'the error response from getCampaignSetupFormConfig is false')
def step_impl(context):
    assert context.getCampaignSetupFormConfig_response_json['error'] == False


@then(u'save the config file')
def step_impl(context):
    payload.saveConfig(context.getCampaignSetupFormConfig_response_json)

