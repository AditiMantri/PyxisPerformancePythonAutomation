import json
import random

import payload
from behave import *
from payload import *

from Utilities.log import custom_logger as log
from Utilities.configurations import *
from Utilities.resources import *
import requests

log = log()
log.info("\n\n****************************NEW RUN****************************\n\n")


@given('the URL and the login credentials {login} and {password}')
def step_impl(context, login, password):
    log.info("\n\n---------------Step 1 - Login---------------")
    context.url = getConfig()['API']['endpoint'] + apiResources.login
    context.payload = loginPayload(login, password)
    log.info(f"URL is set to: " + context.url)


@when(u'the Login postAPI is executed')
def step_impl(context):
    context.loginResponse = requests.post(context.url,
                                          json=context.payload)


@when(u'the user should be logged in successfully')
def step_impl(context):
    context.response_json = context.loginResponse.json()
    log.info("{}{}".format("Login response: ", context.response_json))


@then(u'I should receive a valid HTTP response code {status_code:d}')  # d to read it as a decimal
def step_impl(context, status_code):
    assert context.loginResponse.status_code == status_code
    log.info(f"Login status: " + str(context.loginResponse.status_code))


@then(u'validate error is False')
def step_impl(context):
    assert context.response_json['error'] == False
    log.info("{}{}".format("Login error status: ", context.response_json['error']))


@then(u'extract token and save it')
def step_impl(context):
    context.token = context.response_json['data']['key']
    payload.setToken(context.token)
    log.info("Token: " + payload.getToken())


# ----------------------Step2---------------------

@given('the Authorization')
def step_impl(context):
    log.info("\n\n---------------Step 2 - Get clients associated with the logged in user---------------")
    context.url = getConfig()['API']['endpoint'] + apiResources.clients
    context.Authorization = {'Authorization': payload.getToken()}
    log.info(f"URL is set to: " + context.url)


@when(u'the Clients GetAPI is executed')
def step_impl(context):
    context.clientResponse = requests.get(context.url,
                                          headers=context.Authorization)
    context.response_json = context.clientResponse.json()


@when(u'error should be false')
def step_impl(context):
    assert context.response_json['error'] == False
    log.info("{}{}".format("Login error status: ", context.response_json['error']))


@then(u'store the client ID {ClientName}')
def step_impl(context, ClientName):
    for result in context.response_json['data']['clients']:
        if (result['name']) == ClientName:
            payload.setClientID(result['id'])
            log.info("{}{}".format("Client Name is: ", result['name']))
            log.info("{}{}".format("Client ID is: ", payload.getClientID()))
            break


# ----------------------Step3---------------------

@given(u'the token, client id and mpadaccounts endpoint')
def step_impl(context):
    log.info("\n\n---------------Step 3 - Get mpadaccounts data with logged in user---------------")
    endpoint = "{}{}{}".format(apiResources.clients, payload.getClientID(), apiResources.mpadaccounts)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}
    log.info(f"URL is set to: " + context.url)


@when(u'mpadaccount GetAPI is executed')
def step_impl(context):
    context.mpadaccounts_response = requests.get(context.url,
                                                 headers=context.Authorization)
    context.mpadaccounts_response_json = context.mpadaccounts_response.json()


@when(u'the error response from mpadaccount is false')
def step_impl(context):
    assert context.mpadaccounts_response_json['error'] == False
    log.info("{}{}".format("Login error status: ", context.mpadaccounts_response_json['error']))


@then('store the id if adaccount name is {adaccountName}')
def step_impl(context, adaccountName):
    for result in context.mpadaccounts_response_json['data']['adaccounts']:
        if result['name'] == adaccountName:
            payload.setAdaccountID(result['id'])
            log.info("{}{}".format("Ad account name", result['name']))
            log.info("{}{}".format("Ad account ID: ", payload.getAdaccountID()))
            break


# ----------------------Step4---------------------


@given(u'the token and getCampaignSetupFormConfig endpoint')
def step_impl(context):
    log.info("\n\n---------------Step 4 - Get Campaign Setup Form Config---------------")
    context.url = getConfig()['API']['endpoint'] + apiResources.getCampaignSetupFormConfig
    context.Authorization = {'Authorization': payload.getToken()}
    log.info(f"URL is set to: " + context.url)


@when(u'getCampaignSetupFormConfig GetAPI is executed')
def step_impl(context):
    context.getCampaignSetupFormConfig_response = requests.get(context.url,
                                                               headers=context.Authorization)
    context.getCampaignSetupFormConfig_response_json = context.getCampaignSetupFormConfig_response.json()


@when(u'the error response from getCampaignSetupFormConfig is false')
def step_impl(context):
    assert context.getCampaignSetupFormConfig_response_json['error'] == False
    log.info("{}{}".format("Login error status: ", context.getCampaignSetupFormConfig_response_json['error']))


@then(u'save the config file')
def step_impl(context):
    payload.saveConfig(context.getCampaignSetupFormConfig_response_json)


# ----------------------Step5---------------------


@given(u'the token, client id, adaccount id and pages endpoint')
def step_impl(context):
    log.info("\n\n---------------Step 5 - Get pages---------------")
    endpoint = "{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), apiResources.getAdaccount,
                                   payload.getAdaccountID(), apiResources.pages)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}
    log.info(f"URL is set to: " + context.url)


@when(u'Pages GetAPI is executed')
def step_impl(context):
    context.pages_response = requests.get(context.url,
                                          headers=context.Authorization)
    context.pages_response_json = context.pages_response.json()
    payload.setPagejson(context.pages_response_json)


@when(u'the error response from getPages is false')
def step_impl(context):
    assert context.pages_response_json['error'] == False
    log.info("{}{}".format("Login error status: ", context.pages_response_json['error']))


@then(u'capture page ids when accessible is true')
def step_impl(context):
    values = []
    for result in context.pages_response_json['data']:
        if not result['error'] and result['accessible'] == True:
            values.append(result['value']['page_id'])
    log.info("{}{}".format('The page ids are ', values))
    payload.setPages(values)


# ----------------------Step6---------------------


@given(u'the token, client id, adaccount id and adaccounts endpoint')
def step_impl(context):
    log.info("\n\n---------------Step 6 - Get Instagram account---------------")
    endpoint = "{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), '/adaccount/', payload.getAdaccountID(),
                                   apiResources.instagram)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}
    log.info(f"URL is set to: " + context.url)


@when(u'adaccount GetAPI is executed')
def step_impl(context):
    context.instagram_response = requests.get(context.url,
                                              headers=context.Authorization)
    context.instagram_response_json = context.instagram_response.json()


@when(u'the error response from getAdaccounts is false')
def step_impl(context):
    assert context.instagram_response_json['error'] == False
    log.info("{}{}".format("Login error status: ", context.instagram_response_json['error']))


@then(u'capture adaccount ids when accessible is true')
def step_impl(context):
    pass
    values = []
    for result in context.instagram_response_json['data']:
        if not result['error'] and result['accessible'] == True:
            values.append(result['value'])
    log.info("{}{}".format("The instagram account ids are ", values))
    payload.setInstagramAccounts(values)


# ----------------------Step7---------------------


@given(u'the token, client id, adaccount id and CustomAudience endpoint')
def step_impl(context):
    log.info("\n\n---------------Step 7 - Get Custom Audience---------------")
    endpoint = "{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), '/adaccount/', payload.getAdaccountID(),
                                   apiResources.customAudience)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}
    log.info(f"URL is set to: " + context.url)


@when(u'CustomAudience GetAPI is executed')
def step_impl(context):
    context.customAudience_response = requests.get(context.url,
                                                   headers=context.Authorization)
    context.customAudience_response_json = context.customAudience_response.json()


@when(u'the error response from CustomAudience is false')
def step_impl(context):
    assert context.customAudience_response_json['error'] == False
    log.info("{}{}".format("Login error status: ", context.customAudience_response_json['error']))


@then(u'capture custom audience id')
def step_impl(context):
    values = []
    for result in context.customAudience_response_json['data']:
        values.append(result['value']['id'])
    payload.setAudienceID(values)
    log.info("{}{}".format("Audience ID is: ", payload.getAudienceID()))


# ----------------------Step8---------------------


@given(u'the token, client account id, ad account id and createExperimentSetup endpoint')
def step_impl(context):
    log.info("\n\n---------------Step 8 - Post experiment setup campaign details---------------")
    endpoint = "{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), '/adaccount/', payload.getAdaccountID(),
                                   apiResources.createExpSetup)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}
    log.info(f"URL is set to: " + context.url)


@when(u'the json body is sent with {CampaignName}, {DailyBudget}, {AdsetStartTime} for Leadgen')
def step_impl(context, CampaignName, DailyBudget, AdsetStartTime):
    page = payload.getPages()
    randomint = random.randint(1, len(page))
    val = page[randomint - 1]
    context.leadgen_body = payload.setLeadGenBody(CampaignName, DailyBudget, AdsetStartTime, val)
    pagejson = getPagejson()
    for result in pagejson['data']:
        if result['value']['page_id'] == val:
            pageName = result['label']
            break
    log.info("The data that is sent to post API are, Campaign Name = " + CampaignName + ", Daily Budget = " +
             str(DailyBudget) + ", Ad set Start Time = " + AdsetStartTime + " Page id = " + str(val) +
             " and Page name is = " + pageName)


@when(u'the json body is sent with {CampaignName}, {DailyBudget}, {AdsetStartTime} for Traffic')
def step_impl(context, CampaignName, DailyBudget, AdsetStartTime):
    page = payload.getPages()
    randomint = random.randint(1, len(page))
    val = page[randomint - 1]
    context.traffic_json_body = payload.setTrafficBody(CampaignName, DailyBudget, AdsetStartTime, val)
    pagejson = getPagejson()
    for result in pagejson['data']:
        if result['value']['page_id'] == val:
            pageName = result['label']
            break
    log.info("The data that is sent to post API are, Campaign Name = " + CampaignName + ", Daily Budget = " +
             str(DailyBudget) + ", Ad set Start Time = " + AdsetStartTime + " Page id = " + str(val) +
             " and Page name is = " + pageName)


@when(u'create ExperimentSetup postAPI is executed for Traffic')
def step_impl(context):
    context.experiment_setup = requests.post(url=context.url,
                                             headers=context.Authorization,
                                             json=context.traffic_json_body)
    context.experiment_setup_json = context.experiment_setup.json()


@when(u'create ExperimentSetup postAPI is executed for Leadgen')
def step_impl(context):
    context.experiment_setup = requests.post(url=context.url,
                                             headers=context.Authorization,
                                             json=context.leadgen_body)
    context.experiment_setup_json = context.experiment_setup.json()


@then(u'verify if the error response is false')
def step_impl(context):
    assert context.experiment_setup_json['error'] == False
    log.info("{}{}".format("Login error status: ", context.experiment_setup_json['error']))


@then(u'status of the experiment setup is Created')
def step_impl(context):
    assert context.experiment_setup_json['data']['status'] == 'Created'
    log.info("{}{}".format("Status of Experiment setup: ", context.experiment_setup_json['data']['status']))


@then(u'capture the Experiment Setup id')
def step_impl(context):
    payload.saveExperimentSetupID(context.experiment_setup_json['data']['id'])
    log.info("Experiment setup id is: " + str(payload.getExperimentSetupID()))


# ----------------------Step9---------------------

@given(u'the token, experiment setup ID and the getExperimentSetup endpoint')
def step_impl(context):
    log.info("\n\n---------------Step 9 - Get experiment setup---------------")
    endpoint = "{}{}{}".format(apiResources.getExpSetup, payload.getExperimentSetupID(), '/')
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}
    log.info(f"URL is set to: " + context.url)


@when(u'getExperimentSetup getAPI is executed')
def step_impl(context):
    context.getExperimentSetup_response = requests.get(context.url,
                                                       headers=context.Authorization)
    context.getExperimentSetup_response_json = context.getExperimentSetup_response.json()


@when(u'the error response from getExperimentSetup is false')
def step_impl(context):
    assert context.getExperimentSetup_response_json['error'] == False
    log.info("{}{}".format("Login error status: ", context.getExperimentSetup_response_json['error']))


@then(u'save the getExperimentSetup response')
def step_impl(context):
    payload.saveGetExperimentSetupResponse(context.getExperimentSetup_response_json)


# ----------------------Step10---------------------

@given(u'the token,experiment setup ID and the updateExperimentSetup endpoint')
def step_impl(context):
    log.info("\n\n---------------Step 10 - Update experiment setup---------------")
    endpoint = "{}{}{}".format(apiResources.getExpSetup, payload.getExperimentSetupID(), '/')
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}
    log.info(f"URL is set to: " + context.url)


@when(u'updateExperimentSetup putAPI is executed with maxAge={maxAge} and minAge={minAge} for Leadgen')
def step_impl(context, maxAge, minAge):
    context.updateExperimentSetup_response = requests.put(context.url,
                                                          headers=context.Authorization,
                                                          json=payload.updateLeadGenBody(maxAge, minAge))
    context.updateExperimentSetup_response_json = context.updateExperimentSetup_response.json()
    log.info("Update the experiment setup with the following details: Min age = "
             + str(minAge) + "and Max age = " + str(maxAge))


@when(u'updateExperimentSetup putAPI is executed with maxAge={maxAge} and minAge={minAge} for Traffic')
def step_impl(context, maxAge, minAge):
    context.updateExperimentSetup_response = requests.put(context.url,
                                                          headers=context.Authorization,
                                                          json=payload.updateTraffic(maxAge, minAge))
    context.updateExperimentSetup_response_json = context.updateExperimentSetup_response.json()
    log.info("Update the experiment setup with the following details: Min age = "
             + str(minAge) + "and Max age = " + str(maxAge))


@when(u'the error response from updateExperimentSetup is false')
def step_impl(context):
    assert context.updateExperimentSetup_response_json['error'] == False
    log.info("{}{}".format("Login error status: ", context.updateExperimentSetup_response_json['error']))


@then(u'verify the status of the experiment setup is Updated')
def step_impl(context):
    assert context.updateExperimentSetup_response_json['data']['status'] == 'Updated'
    log.info("The status of the updated experiment setup is : "
             + context.updateExperimentSetup_response_json['data']['status'])


# ----------------------Step11---------------------

@given(u'the client id, ad account id, experiment setup id and the getCreative endpoint')
def step_impl(context):
    log.info("\n\n---------------Step 11 - Get creative---------------")
    endpoint = "{}{}{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), apiResources.getAdaccount,
                                       payload.getAdaccountID(), apiResources.experimentSetup,
                                       payload.getExperimentSetupID(), apiResources.getCreative)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}
    log.info(f"URL is set to: " + context.url)


@when(u'getCreative getAPI is executed')
def step_impl(context):
    context.getCreative_response = requests.get(context.url,
                                                headers=context.Authorization)
    context.getCreative_response_json = context.getCreative_response.json()


@when(u'the error response from getCreative is false')
def step_impl(context):
    assert context.getCreative_response_json['error'] == False
    log.info("{}{}".format("Login error status: ", context.getCreative_response_json['error']))


@then(u'verify that the data body is empty')
def step_impl(context):
    assert context.getCreative_response_json['data'] == {'data': []}


# ----------------------Step12---------------------

@given(u'the client id and the getCreativeFiles endpoint')
def step_impl(context):
    log.info("\n\n---------------Step 12 - Get creative files---------------")
    endpoint = "{}{}{}".format(apiResources.clients, payload.getClientID(), apiResources.getCreativeFiles)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}
    log.info(f"URL is set to: " + context.url)


@when(u'getCreativeFiles getAPI is executed')
def step_impl(context):
    context.getCreativeFiles_response = requests.get(context.url,
                                                     headers=context.Authorization)
    context.getCreativeFiles_response_json = context.getCreativeFiles_response.json()


@when(u'the error response from getCreativeFiles is false')
def step_impl(context):
    assert context.getCreativeFiles_response_json['error'] == False
    log.info("{}{}".format("Login error status: ", context.getCreativeFiles_response_json['error']))


@then(u'store the response that we get from getCreativeFiles')
def step_impl(context):
    payload.saveCreativeFiles(context.getCreativeFiles_response)


# ----------------------Step13---------------------


@given(u'the client id and the getCreativeTemplate endpoint')
def step_impl(context):
    log.info("\n\n---------------Step 13 - Get creative template files---------------")
    endpoint = "{}{}{}".format(apiResources.clients, payload.getClientID(), apiResources.getCreativeTemplates)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}
    log.info(f"URL is set to: " + context.url)


@when(u'getCreativeTemplate getAPI is executed')
def step_impl(context):
    context.getCreativeTemplate_response = requests.get(context.url,
                                                        headers=context.Authorization)
    context.getCreativeTemplate_response_json = context.getCreativeTemplate_response.json()


@when(u'the error response from getCreativeTemplate is false')
def step_impl(context):
    assert context.getCreativeTemplate_response_json['error'] == False
    log.info("{}{}".format("Login error status: ", context.getCreativeTemplate_response_json['error']))


@then(u'store the response that we get from getCreativeTemplate')
def step_impl(context):
    payload.saveCreativeTemplate(context.getCreativeTemplate_response_json)


# ----------------------Step14---------------------


@given(u'the client id and the getPixel endpoint')
def step_impl(context):
    log.info("\n\n---------------Step 14 - Get Pixel ID---------------")
    endpoint = "{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), apiResources.getAdaccount,
                                   payload.getAdaccountID(), apiResources.getPixelIDs)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}
    log.info(f"URL is set to: " + context.url)


@when(u'getPixel getAPI is executed')
def step_impl(context):
    context.getPixel_response = requests.get(context.url,
                                             headers=context.Authorization)
    context.getPixel_response_json = context.getPixel_response.json()


@when(u'the error response from getPixel is false')
def step_impl(context):
    assert context.getPixel_response_json['error'] == False
    log.info("{}{}".format("Login error status: ", context.getPixel_response_json['error']))


@then(u'store the pixel id if accessible is true')
def step_impl(context):
    values = []
    for result in context.getPixel_response_json['data']:
        if not result['error'] and result['accessible']:
            values.append(result['value']['pixel_id'])
    payload.savePixelID(values)
    log.info("{}{}".format("Pixel ids are: ", payload.getPixelID()))


# ----------------------Step15---------------------

@given(u'the client id, ad account id, experiment setup id and the postCreative endpoint')
def step_impl(context):
    log.info("\n\n---------------Step 15 - Post the creative---------------")
    endpoint = "{}{}{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), apiResources.getAdaccount,
                                       payload.getAdaccountID(), apiResources.experimentSetup,
                                       payload.getExperimentSetupID(), apiResources.getCreative)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}
    log.info("Post the creative: " + str(apiResources.getCreative))


@when(u'postCreative postAPI is executed for Leadgen')
def step_impl(context):
    context.postCreative_response = requests.post(context.url,
                                                  headers=context.Authorization,
                                                  json=payload.getPostCreativeBodyForLeadgen())
    context.postCreative_response_json = context.postCreative_response.json()
    log.info("Post the creative: " + str(apiResources.getCreative))


@when(u'postCreative postAPI is executed for Traffic')
def step_impl(context):
    context.postCreative_response = requests.post(context.url,
                                                  headers=context.Authorization,
                                                  json=payload.getPostCreativeBodyForTraffic())
    context.postCreative_response_json = context.postCreative_response.json()


@when(u'the error response from postCreative is false')
def step_impl(context):
    assert context.postCreative_response_json['error'] == False
    log.info("{}{}".format("Login error status: ", context.postCreative_response_json['error']))


@then(u'save the creative ID')
def step_impl(context):
    id = context.postCreative_response_json['data']['id']
    payload.saveCreativeID(id)
    log.info("The creative ID is: " + str(payload.getCreativeID()))


# ----------------------Step16---------------------

@then(u'store the json response from getCreative')
def step_impl(context):
    log.info("\n\n---------------Step 16 - Get the creative---------------")
    payload.saveCreatives(context.getCreative_response_json)


# ----------------------Step17---------------------


@given(u'the experiment setup id and the storyname endpoint')
def step_impl(context):
    log.info("\n\n---------------Step 17 - Get storyname---------------")
    endpoint = "{}{}{}".format(apiResources.getExpSetup, payload.getExperimentSetupID(), apiResources.getStoryName)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}
    log.info(f"URL is set to: " + context.url)


@when(u'getStoryName getAPI is executed')
def step_impl(context):
    context.getStoryName_response = requests.get(context.url,
                                                 headers=context.Authorization)
    context.getStoryName_response_json = context.getStoryName_response.json()


@when(u'the error response from getStoryName is false')
def step_impl(context):
    context.getStoryName_response_json['error'] == False
    log.info("{}{}".format("Login error status: ", context.getStoryName_response_json['error']))


@then(u'save the story id')
def step_impl(context):
    payload.saveStoryID(context.getStoryName_response_json['data']['story_id'])
    log.info("Story ID is: " + payload.getStoryID())


# ----------------------Step18---------------------


@given(u'client id, ad account id, experiment setup id and publish endpoint')
def step_impl(context):
    log.info("\n\n---------------Step 18 - Publish request---------------")
    endpoint = "{}{}{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), apiResources.getAdaccount,
                                       payload.getAdaccountID(), apiResources.experimentSetup,
                                       payload.getExperimentSetupID(), apiResources.publish)
    context.url = getConfig()['API']['endpoint'] + endpoint
    context.Authorization = {'Authorization': payload.getToken()}
    log.info(f"URL is set to: " + context.url)


@when(u'publish postAPI is executed for Leadgen')
def step_impl(context):
    context.publish_response = requests.post(context.url,
                                             headers=context.Authorization,
                                             json=payload.getPublishBodyLeadgen())
    context.publish_response_json = context.publish_response.json()


@when(u'publish postAPI is executed for Traffic')
def step_impl(context):
    context.publish_response = requests.post(context.url,
                                             headers=context.Authorization,
                                             json=payload.getPublishBodyTraffic())
    context.publish_response_json = context.publish_response.json()


@when(u'the error response from publish is false and status is requested')
def step_impl(context):
    assert context.publish_response_json['error'] == False
    assert context.publish_response_json['data']['status'] == 'requested'
    log.info("{}{}".format("Login error status: ", context.publish_response_json['error']))
    log.info("Status of the API request is: " + context.publish_response_json['data']['status'])


@then(u'save the publish request id')
def step_impl(context):
    ID = context.publish_response_json['data']['publish_request_id']


# ----------------------Step19---------------------


@given(u'experiment setup id and the endpoint')
def step_impl(context):
    log.info("\n\n---------------Step 19 - AdsPipeline---------------")
    context.url = getConfig()['API']['adspipeline'] + apiResources.publishStatus
    log.info(f"URL is set to: " + context.url)


@when(u'getAPI is executed')
def step_impl(context):
    context.status = requests.get(context.url)
    context.status_json = context.status.json()


@when(u'error status is 200')
def step_impl(context):
    assert context.status_json['statusCode'] == 200
    log.info("{}{}".format("The status code is: ", context.status_json['statusCode']))


@then(u'verify the status is SUCCESS')
def step_impl(context):
    statusCode = context.status_json['statusCode']
    assert statusCode == 200
    for result in context.status_json['data']['tasks']:
        if result['storyId'] == payload.getStoryID():
            break
    assert result['status'] == "PENDING"
    log.info("The experiment setup is created successfully on Aiqurie dashboard and "
             "has been pushed to Upload pipeline")
