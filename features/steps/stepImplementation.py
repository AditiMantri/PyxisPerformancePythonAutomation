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
    context.Authorization = {'Authorization' : payload.getToken()}


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
        if(result['name']) == ClientName:
            payload.setClientID(result['id'])
            print(result['name'])
            print(payload.getClientID())
            break
    payload.setClientID(payload.setClientID(result['id']))

