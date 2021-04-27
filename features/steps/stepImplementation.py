import json

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


# ----------------------Step5---------------------


@given(u'the token, client id, adaccount id and pages endpoint')
def step_impl(context):
    endpoint = "{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), apiResources.getAdaccount,
                                   payload.getAdaccountID(), apiResources.pages)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}


@when(u'Pages GetAPI is executed')
def step_impl(context):
    context.pages_response = requests.get(context.url,
                                          headers=context.Authorization)
    context.pages_response_json = context.pages_response.json()


@when(u'the error response from getPages is false')
def step_impl(context):
    assert context.pages_response_json['error'] == False


@then(u'capture page ids when accessible is true')
def step_impl(context):
    values = []
    for result in context.pages_response_json['data']:
        if not result['error'] and result['accessible'] == True:
            values.append(result['value']['page_id'])
    print("{}{}".format('The page ids are ', values))
    payload.setPages(values)


# ----------------------Step6---------------------


@given(u'the token, client id, adaccount id and adaccounts endpoint')
def step_impl(context):
    endpoint = "{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), '/adaccount/', payload.getAdaccountID(),
                                   apiResources.instagram)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}


@when(u'adaccount GetAPI is executed')
def step_impl(context):
    context.instagram_response = requests.get(context.url,
                                              headers=context.Authorization)
    context.instagram_response_json = context.instagram_response.json()


@when(u'the error response from getAdaccounts is false')
def step_impl(context):
    assert context.instagram_response_json['error'] == False


@then(u'capture adaccount ids when accessible is true')
def step_impl(context):
    pass
    values = []
    for result in context.instagram_response_json['data']:
        if not result['error'] and result['accessible'] == True:
            values.append(result['value'])
    print("{}{}".format("The instagram account ids are ", values))
    payload.setInstagramAccounts(values)


# ----------------------Step7---------------------


@given(u'the token, client id, adaccount id and CustomAudience endpoint')
def step_impl(context):
    endpoint = "{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), '/adaccount/', payload.getAdaccountID(),
                                   apiResources.customAudience)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}


@when(u'CustomAudience GetAPI is executed')
def step_impl(context):
    context.customAudience_response = requests.get(context.url,
                                                   headers=context.Authorization)
    context.customAudience_response_json = context.customAudience_response.json()


@when(u'the error response from CustomAudience is false')
def step_impl(context):
    assert context.customAudience_response_json['error'] == False


@then(u'capture custom audience id')
def step_impl(context):
    values = []
    for result in context.customAudience_response_json['data']:
        values.append(result['value']['id'])
    payload.setAudienceID(values)
    print(payload.getAudienceID())


# ----------------------Step8---------------------


@given(u'the token, client account id, ad account id and createExperimentSetup endpoint')
def step_impl(context):
    endpoint = "{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), '/adaccount/', payload.getAdaccountID(),
                                   apiResources.createExpSetup)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}


@when(u'the json body is sent')
def step_impl(context):
    context.leadgen_body = payload.setLeadGenBody()


@when(u'createExperimentSetup postAPI is executed')
def step_impl(context):
    context.experiment_setup = requests.post(url=context.url,
                                             headers=context.Authorization,
                                             json=context.leadgen_body)
    context.experiment_setup_json = context.experiment_setup.json()


@then(u'verify if the error response is false')
def step_impl(context):
    print(context.url)
    print(context.experiment_setup.text)


@then(u'status of the experiment setup is Created')
def step_impl(context):
    assert context.experiment_setup_json['data']['status'] == 'Created'


@then(u'capture the Experiment Setup id')
def step_impl(context):
    payload.saveExperimentSetupID(context.experiment_setup_json['data']['id'])
    print(payload.getExperimentSetupID())


# ----------------------Step9---------------------

@given(u'the token, experiment setup ID and the getExperimentSetup endpoint')
def step_impl(context):
    endpoint = "{}{}{}".format(apiResources.getExpSetup, payload.getExperimentSetupID(), '/')
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}


@when(u'getExperimentSetup getAPI is executed')
def step_impl(context):
    context.getExperimentSetup_response = requests.get(context.url,
                                                       headers=context.Authorization)
    context.getExperimentSetup_response_json = context.getExperimentSetup_response.json()


@when(u'the error response from getExperimentSetup is false')
def step_impl(context):
    assert context.getExperimentSetup_response_json['error'] == False


@then(u'save the getExperimentSetup response')
def step_impl(context):
    payload.saveGetExperimentSetupResponse(context.getExperimentSetup_response_json)


# ----------------------Step10---------------------

@given(u'the token,experiment setup ID and the updateExperimentSetup endpoint')
def step_impl(context):
    endpoint = "{}{}{}".format(apiResources.getExpSetup, payload.getExperimentSetupID(), '/')
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}


@when(u'updateExperimentSetup putAPI is executed')
def step_impl(context):
    context.updateExperimentSetup_response = requests.put(context.url,
                                                          headers=context.Authorization,
                                                          json=payload.updateLeadGenBody())
    context.updateExperimentSetup_response_json = context.updateExperimentSetup_response.json()


@when(u'the error response from updateExperimentSetup is false')
def step_impl(context):
    assert context.updateExperimentSetup_response_json['error'] == False


@then(u'verify the status of the experiment setup is Updated')
def step_impl(context):
    assert context.updateExperimentSetup_response_json['data']['status'] == 'Updated'


# ----------------------Step11---------------------

@given(u'the client id, ad account id, experiment setup id and the getCreative endpoint')
def step_impl(context):
    endpoint = "{}{}{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), apiResources.getAdaccount,
                                       payload.getAdaccountID(), apiResources.experimentSetup,
                                       payload.getExperimentSetupID(), apiResources.getCreative)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}


@when(u'getCreative getAPI is executed')
def step_impl(context):
    context.getCreative_response = requests.get(context.url,
                                                headers=context.Authorization)
    context.getCreative_response_json = context.getCreative_response.json()


@when(u'the error response from getCreative is false')
def step_impl(context):
    assert context.getCreative_response_json['error'] == False


@then(u'verify that the data body is empty')
def step_impl(context):
    assert context.getCreative_response_json['data'] == {'data': []}


# ----------------------Step12---------------------

@given(u'the client id and the getCreativeFiles endpoint')
def step_impl(context):
    endpoint = "{}{}{}".format(apiResources.clients, payload.getClientID(), apiResources.getCreativeFiles)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}


@when(u'getCreativeFiles getAPI is executed')
def step_impl(context):
    context.getCreativeFiles_response = requests.get(context.url,
                                                     headers=context.Authorization)
    context.getCreativeFiles_response_json = context.getCreativeFiles_response.json()


@when(u'the error response from getCreativeFiles is false')
def step_impl(context):
    assert context.getCreativeFiles_response_json['error'] == False


@then(u'store the response that we get from getCreativeFiles')
def step_impl(context):
    payload.saveCreativeFiles(context.getCreativeFiles_response)


# ----------------------Step13---------------------


@given(u'the client id and the getCreativeTemplate endpoint')
def step_impl(context):
    endpoint = "{}{}{}".format(apiResources.clients, payload.getClientID(), apiResources.getCreativeTemplates)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}


@when(u'getCreativeTemplate getAPI is executed')
def step_impl(context):
    context.getCreativeTemplate_response = requests.get(context.url,
                                                        headers=context.Authorization)
    context.getCreativeTemplate_response_json = context.getCreativeTemplate_response.json()


@when(u'the error response from getCreativeTemplate is false')
def step_impl(context):
    assert context.getCreativeTemplate_response_json['error'] == False


@then(u'store the response that we get from getCreativeTemplate')
def step_impl(context):
    payload.saveCreativeTemplate(context.getCreativeTemplate_response_json)


# ----------------------Step14---------------------


@given(u'the client id and the getPixel endpoint')
def step_impl(context):
    endpoint = "{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), apiResources.getAdaccount,
                                   payload.getAdaccountID(), apiResources.getPixelIDs)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}
    print(context.url)


@when(u'getPixel getAPI is executed')
def step_impl(context):
    context.getPixel_response = requests.get(context.url,
                                             headers=context.Authorization)
    context.getPixel_response_json = context.getPixel_response.json()
    print(context.getPixel_response.text)


@when(u'the error response from getPixel is false')
def step_impl(context):
    assert context.getPixel_response_json['error'] == False


@then(u'store the pixel id if accessible is true')
def step_impl(context):
    values = []
    for result in context.getPixel_response_json['data']:
        if not result['error'] and result['accessible']:
            values.append(result['value']['pixel_id'])
    payload.savePixelID(values)
    print(payload.getPixelID())


# ----------------------Step15---------------------

@given(u'the client id, ad account id, experiment setup id and the postCreative endpoint')
def step_impl(context):
    endpoint = "{}{}{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), apiResources.getAdaccount,
                                       payload.getAdaccountID(), apiResources.experimentSetup,
                                       payload.getExperimentSetupID(), apiResources.getCreative)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}


@when(u'postCreative postAPI is executed')
def step_impl(context):
    context.postCreative_response = requests.post(context.url,
                                                  headers=context.Authorization,
                                                  json=payload.getPostCreativeBody())
    context.postCreative_response_json = context.postCreative_response.json()


@when(u'the error response from postCreative is false')
def step_impl(context):
    assert context.postCreative_response_json['error'] == False


@then(u'save the creative ID')
def step_impl(context):
    id = context.postCreative_response_json['data']['id']
    payload.saveCreativeID(id)
    print(payload.getCreativeID())


# ----------------------Step16---------------------

@then(u'store the json response from getCreative')
def step_impl(context):
    payload.saveCreatives(context.getCreative_response_json)
    print(payload.getCreatives())


# ----------------------Step17---------------------


@given(u'the experiment setup id and the storyname endpoint')
def step_impl(context):
    endpoint = "{}{}{}".format(apiResources.getExpSetup, payload.getExperimentSetupID(), apiResources.getStoryName)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}


@when(u'getStoryName getAPI is executed')
def step_impl(context):
    context.getStoryName_response = requests.get(context.url,
                                                 headers=context.Authorization)
    context.getStoryName_response_json = context.getStoryName_response.json()


@when(u'the error response from getStoryName is false')
def step_impl(context):
    context.getStoryName_response_json['error'] == False


@then(u'save the story id')
def step_impl(context):
    payload.saveStoryID(context.getStoryName_response_json['data']['story_id'])
    print(payload.getStoryID())


# ----------------------Step18---------------------


@given(u'client id, ad account id, experiment setup id and publish endpoint')
def step_impl(context):
    endpoint = "{}{}{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), apiResources.getAdaccount,
                                       payload.getAdaccountID(), apiResources.experimentSetup,
                                       payload.getExperimentSetupID(), apiResources.publish)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}


@when(u'publish postAPI is executed')
def step_impl(context):
    context.publish_response = requests.post(context.url,
                                             headers=context.Authorization,
                                             json=payload.getPublishBody())
    context.publish_response_json = context.publish_response.json()


@when(u'the error response from publish is false and status is requested')
def step_impl(context):
    assert context.publish_response_json['error'] == False
    assert context.publish_response_json['data']['status'] == 'requested'


@then(u'save the publish request id')
def step_impl(context):
    payload.setPublishRequestID(context.publish_response_json['data']['publish_request_id'])
    print(payload.getPublishRequestID)

