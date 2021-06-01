import json
import random
import time
import threading
from asyncio import wait

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
    log.info("\n\n---------------Login---------------")
    try:
        context.url = getConfig()['API']['endpoint'] + apiResources.login
        context.payload = loginPayload(login, password)
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the Login postAPI is executed')
def step_impl(context):
    try:
        context.loginResponse = requests.post(context.url,
                                              json=context.payload)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the user should be logged in successfully')
def step_impl(context):
    try:
        context.response_json = context.loginResponse.json()
        log.debug("{}{}".format("Login response: ", context.response_json))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'I should receive a valid HTTP response code {status_code:d}')  # d to read it as a decimal
def step_impl(context, status_code):
    try:
        assert context.loginResponse.status_code == status_code
        log.debug(f"Login status: " + str(context.loginResponse.status_code))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'validate error is False')
def step_impl(context):
    try:
        assert context.response_json['error'] == False
        log.debug("{}{}".format("Login error status: ", context.response_json['error']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'extract token and save it')
def step_impl(context):
    try:
        context.token = context.response_json['data']['key']
        payload.setToken(context.token)
        log.debug("Token: " + payload.getToken() + "\n\n")
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step2---------------------

@given('the Authorization')
def step_impl(context):
    log.info("---------------Get clients associated with the logged in user---------------")
    try:
        context.url = getConfig()['API']['endpoint'] + apiResources.clients
        context.Authorization = {'Authorization': payload.getToken()}
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the Clients GetAPI is executed')
def step_impl(context):
    try:
        context.clientResponse = requests.get(context.url,
                                              headers=context.Authorization)
        context.response_json = context.clientResponse.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'error should be false')
def step_impl(context):
    try:
        assert context.response_json['error'] == False
        log.debug("{}{}".format("Login error status: ", context.response_json['error']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'extract the GetAPI response and store it')
def step_impl(context):
    try:
        payload.setClientData(context.response_json)
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'verify if the {ClientName} is linked to the logged in user')
def step_impl(context, ClientName):
    try:
        for result in context.response_json['data']['clients']:
            if ClientName in (result['name']):
                log.debug("Client " + ClientName + " is linked to the logged in user")
                break
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'store the client ID {ClientName}')
def step_impl(context, ClientName):
    try:
        for result in context.response_json['data']['clients']:
            if (result['name']) == ClientName:
                payload.setClientID(result['id'])
                log.debug("{}{}".format("Client Name is: ", result['name']))
                log.debug("{}{}".format("Client ID is: ", payload.getClientID()) + "\n\n")
                break
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step3.0---------------------


@given(u'the token, client id and adaccounts endpoint')
def step_impl(context):
    log.info("---------------Get adaccounts data with logged in user---------------")
    try:
        endpoint = "{}{}{}".format(apiResources.clients, payload.getClientID(), apiResources.adaccounts)
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'adaccount GetAPI is executed')
def step_impl(context):
    try:
        context.adaccounts_response = requests.get(context.url,
                                                   headers=context.Authorization)
        context.adaccounts_response_json = context.adaccounts_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from adaccount is false')
def step_impl(context):
    try:
        assert context.adaccounts_response_json['error'] == False
        log.debug("{}{}".format("Login error status: ", context.adaccounts_response_json['error']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'store the adaccounts response')
def step_impl(context):
    try:
        payload.saveAdaccountsList(context.adaccounts_response_json['data'])
        log.debug("{}{}".format(payload.getAdaccountsList(), "\n\n"))
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step3.1---------------------


@given(u'the token, client id and mpadaccounts endpoint')
def step_impl(context):
    log.info("---------------Get mpadaccounts data with logged in user---------------")
    try:
        endpoint = "{}{}{}".format(apiResources.clients, payload.getClientID(), apiResources.mpadaccounts)
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'mpadaccount GetAPI is executed')
def step_impl(context):
    try:
        context.mpadaccounts_response = requests.get(context.url,
                                                     headers=context.Authorization)
        context.mpadaccounts_response_json = context.mpadaccounts_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from mpadaccount is false')
def step_impl(context):
    try:
        assert context.mpadaccounts_response_json['error'] == False
        log.debug("{}{}".format("Login error status: ", context.mpadaccounts_response_json['error']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then('store the id if adaccount name is {adaccountName}')
def step_impl(context, adaccountName):
    try:
        for result in context.mpadaccounts_response_json['data']['adaccounts']:
            if result['name'] == adaccountName:
                payload.setAdaccountID(result['id'])
                log.debug("{}{}".format("Ad account name", result['name']))
                log.debug("{}{}".format("Ad account ID: ", payload.getAdaccountID()) + "\n\n")
                break
    except Exception as e:
        log.exception(str(e))
        raise e


@then('store the id of {adaccountName} if adaccount name is present in the adaccount list')
def step_impl(context, adaccountName):
    try:
        for result in context.mpadaccounts_response_json['data']['adaccounts']:
            if result['name'] == adaccountName:
                payload.setAdaccountID(result['id'])
                log.debug("{}{}".format("Ad account name", result['name']))
                log.debug("{}{}{}".format("Ad account ID: ", payload.getAdaccountID(), "\n\n"))
                break
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step4---------------------


@given(u'the token and getCampaignSetupFormConfig endpoint')
def step_impl(context):
    log.info("---------------Get Campaign Setup Form Config---------------")
    try:
        context.url = getConfig()['API']['endpoint'] + apiResources.getCampaignSetupFormConfig
        context.Authorization = {'Authorization': payload.getToken()}
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'getCampaignSetupFormConfig GetAPI is executed')
def step_impl(context):
    try:
        context.getCampaignSetupFormConfig_response = requests.get(context.url,
                                                                   headers=context.Authorization)
        context.getCampaignSetupFormConfig_response_json = context.getCampaignSetupFormConfig_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from getCampaignSetupFormConfig is false')
def step_impl(context):
    try:
        assert context.getCampaignSetupFormConfig_response_json['error'] == False
        log.debug("{}{}".format("Login error status: ",
                                context.getCampaignSetupFormConfig_response_json['error']) + "\n\n")
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'save the config file')
def step_impl(context):
    try:
        payload.saveConfig(context.getCampaignSetupFormConfig_response_json)
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step5.0---------------------


@given(u'the token, adaccount id and getStatus endpoint')
def step_impl(context):
    log.info("---------------Get Status---------------")
    try:
        endpoint = "{}{}{}{}".format(apiResources.api, apiResources.getAdaccount, payload.getAdaccountID(),
                                     apiResources.getStatus)
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'Status GetAPI is executed')
def step_impl(context):
    try:
        context.status_response = requests.get(context.url,
                                               headers=context.Authorization)
        context.status_response_json = context.status_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from status is false')
def step_impl(context):
    try:
        assert context.status_response_json['error'] == False
        log.debug("{}{}".format("Status error status: ", context.status_response_json['error']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'verify that the sync_status is DONE')
def step_impl(context):
    try:
        if context.status_response_json['data']['status']['sync_status'] == 'DONE':
            log.debug("Sync is completed from the backend")
        else:
            log.debug("The sync is in progress, cannot proceed further!")
            assert context.status_response_json['data']['status']['sync_status'] == 'DONE'
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'last_30d_available and first_30d_available are both true')
def step_impl(context):
    try:
        if context.status_response_json['data']['status']['first_30d_available']:
            log.debug(
                "{}{}".format("last 30d - ", context.status_response_json['data']['status']['first_30d_available']))
            if context.status_response_json['data']['status']['last_30d_available']:
                log.debug(
                    "{}{}".format("first 30d - ", context.status_response_json['data']['status']['last_30d_available']))
                log.debug("Past data is available \n\n")
        else:
            log.debug("Past data is not available \n\n")
            assert context.status_response_json['data']['status']['first_30d_available'] == True
            assert context.status_response_json['data']['status']['last_30d_available'] == True
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step5.1---------------------


@given(u'the token, client id, adaccount id and pages endpoint')
def step_impl(context):
    log.info("---------------Get pages---------------")
    try:
        endpoint = "{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), apiResources.getAdaccount,
                                       payload.getAdaccountID(), apiResources.pages)
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'Pages GetAPI is executed')
def step_impl(context):
    try:
        context.pages_response = requests.get(context.url,
                                              headers=context.Authorization)
        context.pages_response_json = context.pages_response.json()
        payload.setPagejson(context.pages_response_json)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from getPages is false')
def step_impl(context):
    try:
        assert context.pages_response_json['error'] == False
        log.debug("{}{}".format("Login error status: ", context.pages_response_json['error']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'capture page ids when accessible is true')
def step_impl(context):
    try:
        values = []
        for result in context.pages_response_json['data']:
            if not result['error'] and result['accessible'] == True:
                values.append(result['value']['page_id'])
        log.debug("{}{}".format('The page ids are ', values) + "\n\n")
        payload.setPages(values)
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step6.0---------------------


@given(u'the adaccount id, date preset, objective, optimization goal and getMetricData endpoint')
def step_impl(context):
    log.info("---------------Get Metric data---------------")
    try:
        endpoint = "{}{}{}{}{}".format(apiResources.api, apiResources.getAdaccount, payload.getAdaccountID()
                                       , "/", apiResources.metric)
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        context.header = {
            "date_preset": "last_60d",
            "objective": "CONVERSIONS",
            "event": "fb_primary_actions_offsite_conversion_fb_pixel_complete_registration"
        }
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'Metric getAPI is executed')
def step_impl(context):
    try:
        context.metric_response = requests.get(context.url,
                                               headers=context.Authorization,
                                               params=context.header)
        context.metric_response_json = context.metric_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from Metric is false')
def step_impl(context):
    try:
        assert context.metric_response_json['error'] == False
        log.debug("{}{}".format("Login error status: ", context.metric_response_json['error']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'store the metrics data')
def step_impl(context):
    try:
        payload.saveMetricData(context.metric_response_json['data'])
        log.debug("{}{}{}".format("Metric data is : ", payload.getMetricData(), "\n\n"))
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step6.1---------------------


@given(u'the token, client id, adaccount id and adaccounts endpoint')
def step_impl(context):
    log.info("---------------Get Instagram account---------------")
    try:
        endpoint = "{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), '/adaccount/',
                                       payload.getAdaccountID(), apiResources.instagram)
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'instagram account GetAPI is executed')
def step_impl(context):
    try:
        context.instagram_response = requests.get(context.url,
                                                  headers=context.Authorization)
        context.instagram_response_json = context.instagram_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from Instagram accounts is false')
def step_impl(context):
    try:
        assert context.instagram_response_json['error'] == False
        log.debug("{}{}".format("Login error status: ", context.instagram_response_json['error']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'capture adaccount ids when accessible is true')
def step_impl(context):
    try:
        values = []
        for result in context.instagram_response_json['data']:
            if not result['error'] and result['accessible'] == True:
                values.append(result['value'])
        log.debug("{}{}".format("The instagram account ids are ", values) + "\n\n")
        payload.setInstagramAccounts(values)
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step7.0---------------------


@given(u'the adaccount id, date preset, objective and getCampaignIDs endpoint')
def step_impl(context):
    log.info("---------------Get Campaign IDs data---------------")
    try:
        endpoint = "{}{}{}{}".format(apiResources.api, apiResources.getAdaccount, payload.getAdaccountID()
                                     , "/")
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        context.header = {
            "date_preset": "last_60d",
            "objective": "CONVERSIONS"
        }
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'getCampaignIDs getAPI is executed')
def step_impl(context):
    try:
        context.campaignID_response = requests.get(context.url,
                                                   headers=context.Authorization,
                                                   params=context.header
                                                   )
        context.campaignID_response_json = context.campaignID_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from the getCampaignIDs is false')
def step_impl(context):
    try:
        assert context.campaignID_response_json['error'] == False
        log.debug("{}{}".format("Login error status: ", context.campaignID_response_json['error']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'store all the campaign ids')
def step_impl(context):
    try:
        values = []
        for result in context.campaignID_response_json['data']['breakdown']:
            values.append(result['campaign_id'])
        payload.saveCampaignIDs(values)
        log.debug("{}{}{}".format("Campaign Ids - ", payload.getCampaignIDs(), "\n\n"))
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step7.1---------------------


@given(u'the token, client id, adaccount id and CustomAudience endpoint')
def step_impl(context):
    log.info("---------------Get Custom Audience---------------")
    try:
        endpoint = "{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), '/adaccount/',
                                       payload.getAdaccountID(),
                                       apiResources.customAudience)
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'CustomAudience GetAPI is executed')
def step_impl(context):
    try:
        context.customAudience_response = requests.get(context.url,
                                                       headers=context.Authorization)
        context.customAudience_response_json = context.customAudience_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from CustomAudience is false')
def step_impl(context):
    try:
        assert context.customAudience_response_json['error'] == False
        log.debug("{}{}".format("Login error status: ", context.customAudience_response_json['error']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'capture custom audience id')
def step_impl(context):
    try:
        values = []
        for result in context.customAudience_response_json['data']:
            values.append(result['value']['id'])
        payload.setAudienceID(values)
        log.debug("{}{}".format("Audience ID is: ", payload.getAudienceID()) + "\n\n")
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step8.1---------------------


@given(u'the adaccount id, date preset, age breakdown, campaign IDs and the AgeBreakdown endpoint')
def step_impl(context):
    log.info("---------------Get Age breakdown data---------------")
    try:
        endpoint = "{}{}{}{}".format(apiResources.api, apiResources.getAdaccount, payload.getAdaccountID()
                                     , apiResources.breakdown)
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        context.header = {
            "date_preset": "last_60d",
            "breakdown": "age",
            "campaign_ids": payload.getCampaignIDs()
        }
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the AgeBreakdown getAPI is executed')
def step_impl(context):
    try:
        context.age_response = requests.get(context.url,
                                            headers=context.Authorization,
                                            params=context.header)
        context.age_response_json = context.age_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from the getAgeBreakdown is false')
def step_impl(context):
    try:
        assert context.age_response_json['error'] == False
        log.debug("{}{}".format("Login error status: ", context.age_response_json['error']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'verify that the initial data from getAgeBreakdown is blank')
def step_impl(context):
    try:
        if context.age_response_json['data']['breakdown'] == []:
            log.debug("Age breakdown API successfully executed \n\n")
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step8.2---------------------


@given(u'the token, client account id, ad account id and createExperimentSetup endpoint')
def step_impl(context):
    log.info("---------------Post experiment setup campaign details---------------")
    try:
        endpoint = "{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), '/adaccount/',
                                       payload.getAdaccountID(),
                                       apiResources.createExpSetup)
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the json body is sent with {CampaignName}, {DailyBudget}, {AdsetStartTime} for Leadgen')
def step_impl(context, CampaignName, DailyBudget, AdsetStartTime):
    try:
        page = payload.getPages()
        randomint = random.randint(1, len(page))
        val = page[randomint - 1]
        context.leadgen_body = payload.setLeadGenBody(CampaignName, DailyBudget, AdsetStartTime, val)
        pagejson = getPagejson()
        for result in pagejson['data']:
            if result['value']['page_id'] == val:
                pageName = result['label']
                break
        log.debug("The data that is sent to post API are, Campaign Name = " + CampaignName + ", Daily Budget = " +
                  str(DailyBudget) + ", Ad set Start Time = " + AdsetStartTime + " Page id = " + str(val) +
                  " and Page name is = " + pageName)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the json body is sent with {CampaignName}, {DailyBudget}, {AdsetStartTime} for Traffic')
def step_impl(context, CampaignName, DailyBudget, AdsetStartTime):
    try:
        page = payload.getPages()
        randomint = random.randint(1, len(page))
        val = page[randomint - 1]
        context.traffic_json_body = payload.setTrafficBody(CampaignName, DailyBudget, AdsetStartTime, val)
        pagejson = getPagejson()
        for result in pagejson['data']:
            if result['value']['page_id'] == val:
                pageName = result['label']
                break
        log.debug("The data that is sent to post API are, Campaign Name = " + CampaignName + ", Daily Budget = " +
                  str(DailyBudget) + ", Ad set Start Time = " + AdsetStartTime + " Page id = " + str(val) +
                  " and Page name is = " + pageName)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the json body is sent with {CampaignName}, {DailyBudget}, {AdsetStartTime} for Conversion')
def step_impl(context, CampaignName, DailyBudget, AdsetStartTime):
    try:
        page = payload.getPages()
        randomint = random.randint(1, len(page))
        val = page[randomint - 1]
        context.conversion_json_body = payload.setConversionBody(CampaignName, DailyBudget, AdsetStartTime, val)
        pagejson = getPagejson()
        for result in pagejson['data']:
            if result['value']['page_id'] == val:
                pageName = result['label']
                break
        log.debug("The data that is sent to post API are, Campaign Name = " + CampaignName + ", Daily Budget = " +
                  str(DailyBudget) + ", Ad set Start Time = " + AdsetStartTime + " Page id = " + str(val) +
                  " and Page name is = " + pageName)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the json body is sent with {CampaignName}, {DailyBudget}, {AdsetStartTime} for AppInstall')
def step_impl(context, CampaignName, DailyBudget, AdsetStartTime):
    try:
        page = payload.getPages()
        randomint = random.randint(1, len(page))
        val = page[randomint - 1]
        context.AppInstall_json_body = payload.setAppInstallBody(CampaignName, DailyBudget, AdsetStartTime, val)
        pagejson = getPagejson()
        for result in pagejson['data']:
            if result['value']['page_id'] == val:
                pageName = result['label']
                break
        log.debug("The data that is sent to post API are, Campaign Name = " + CampaignName + ", Daily Budget = " +
                  str(DailyBudget) + ", Ad set Start Time = " + AdsetStartTime + " Page id = " + str(val) +
                  " and Page name is = " + pageName)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'create ExperimentSetup postAPI is executed for Leadgen')
def step_impl(context):
    try:
        context.experiment_setup = requests.post(url=context.url,
                                                 headers=context.Authorization,
                                                 json=context.leadgen_body)
        context.experiment_setup_json = context.experiment_setup.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'create ExperimentSetup postAPI is executed for Conversion')
def step_impl(context):
    try:
        context.experiment_setup = requests.post(url=context.url,
                                                 headers=context.Authorization,
                                                 json=context.conversion_json_body)
        context.experiment_setup_json = context.experiment_setup.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'create ExperimentSetup postAPI is executed for Traffic')
def step_impl(context):
    context.experiment_setup = requests.post(url=context.url,
                                             headers=context.Authorization,
                                             json=context.traffic_json_body)
    context.experiment_setup_json = context.experiment_setup.json()


@when(u'create ExperimentSetup postAPI is executed for Appinstall')
def step_impl(context):
    try:
        context.experiment_setup = requests.post(url=context.url,
                                                 headers=context.Authorization,
                                                 json=context.AppInstall_json_body)
        context.experiment_setup_json = context.experiment_setup.json()
        log.info(context.experiment_setup_json)
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'verify if the error response is false')
def step_impl(context):
    try:
        assert context.experiment_setup_json['error'] == False
        log.debug("{}{}".format("Login error status: ", context.experiment_setup_json['error']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'status of the experiment setup is Created')
def step_impl(context):
    try:
        assert context.experiment_setup_json['data']['status'] == 'Created'
        log.debug("{}{}".format("Status of Experiment setup: ", context.experiment_setup_json['data']['status']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'capture the Experiment Setup id')
def step_impl(context):
    try:
        payload.saveExperimentSetupID(context.experiment_setup_json['data']['id'])
        log.debug("Experiment setup id is: " + str(payload.getExperimentSetupID()) + "\n\n")
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step9.1---------------------


@given(u'the adaccount id, date preset, Gender breakdown, campaign IDs and the GenderBreakdown endpoint')
def step_impl(context):
    log.info("---------------Get Gender breakdown data---------------")
    try:
        endpoint = "{}{}{}{}".format(apiResources.api, apiResources.getAdaccount, payload.getAdaccountID()
                                     , apiResources.breakdown)
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        context.header = {
            "date_preset": "last_60d",
            "breakdown": "gender",
            "campaign_ids": payload.getCampaignIDs()
        }
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the GenderBreakdown getAPI is executed')
def step_impl(context):
    try:
        context.gender_response = requests.get(context.url,
                                               headers=context.Authorization,
                                               params=context.header)
        context.gender_response_json = context.gender_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from the getGenderBreakdown is false')
def step_impl(context):
    try:
        assert context.gender_response_json['error'] == False
        log.debug("{}{}".format("Login error status: ", context.gender_response_json['error']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'verify that the initial data from getGenderBreakdown is blank')
def step_impl(context):
    try:
        if context.gender_response_json['data']['breakdown'] == []:
            log.debug("Gender breakdown API successfully executed \n\n")
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step9.2---------------------


@given(u'the token, experiment setup ID and the getExperimentSetup endpoint')
def step_impl(context):
    log.info("---------------Get experiment setup---------------")
    try:
        endpoint = "{}{}{}".format(apiResources.getExpSetup, payload.getExperimentSetupID(), '/')
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'getExperimentSetup getAPI is executed')
def step_impl(context):
    try:
        context.getExperimentSetup_response = requests.get(context.url,
                                                           headers=context.Authorization)
        context.getExperimentSetup_response_json = context.getExperimentSetup_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from getExperimentSetup is false')
def step_impl(context):
    try:
        assert context.getExperimentSetup_response_json['error'] == False
        log.debug("{}{}".format("Login error status: ", context.getExperimentSetup_response_json['error'])
                  + "\n\n")
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'save the getExperimentSetup response')
def step_impl(context):
    try:
        payload.saveGetExperimentSetupResponse(context.getExperimentSetup_response_json)
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step10.1---------------------


@given(u'the adaccount id, date preset, PublisherPlatform breakdown, campaign IDs and the PublisherPlatform endpoint')
def step_impl(context):
    log.info("---------------Get PublisherPlatform data---------------")
    try:
        endpoint = "{}{}{}{}".format(apiResources.api, apiResources.getAdaccount, payload.getAdaccountID()
                                     , apiResources.breakdown)
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        context.header = {
            "date_preset": "last_60d",
            "breakdown": "publisher_platform",
            "campaign_ids": payload.getCampaignIDs()
        }
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the PublisherPlatform getAPI is executed')
def step_impl(context):
    try:
        context.PublisherPlatform_response = requests.get(context.url,
                                                          headers=context.Authorization,
                                                          params=context.header)
        context.PublisherPlatform_response_json = context.PublisherPlatform_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from the getPublisherPlatform is false')
def step_impl(context):
    try:
        assert context.PublisherPlatform_response_json['error'] == False
        log.debug(
            "{}{}".format("getPublisherPlatform error status: ", context.PublisherPlatform_response_json['error']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'verify that the initial data from getPublisherPlatform is blank')
def step_impl(context):
    try:
        if context.PublisherPlatform_response_json['data']['breakdown'] == []:
            log.debug("PublisherPlatform breakdown API successfully executed \n\n")
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step10.2---------------------

@given(u'the token,experiment setup ID and the updateExperimentSetup endpoint')
def step_impl(context):
    log.info("---------------Update experiment setup---------------")
    try:
        endpoint = "{}{}{}".format(apiResources.getExpSetup, payload.getExperimentSetupID(), '/')
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'updateExperimentSetup putAPI is executed with maxAge={maxAge} and minAge={minAge} for Leadgen')
def step_impl(context, maxAge, minAge):
    try:
        context.updateExperimentSetup_response = requests.put(context.url,
                                                              headers=context.Authorization,
                                                              json=payload.updateLeadGenBody(maxAge, minAge))
        context.updateExperimentSetup_response_json = context.updateExperimentSetup_response.json()
        log.debug("Update the experiment setup with the following details: Min age = "
                  + str(minAge) + "and Max age = " + str(maxAge))
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'updateExperimentSetup putAPI is executed with maxAge={maxAge} and minAge={minAge} for Traffic')
def step_impl(context, maxAge, minAge):
    try:
        context.updateExperimentSetup_response = requests.put(context.url,
                                                              headers=context.Authorization,
                                                              json=payload.updateTraffic(maxAge, minAge))
        context.updateExperimentSetup_response_json = context.updateExperimentSetup_response.json()
        log.debug("Update the experiment setup with the following details: Min age = "
                  + str(minAge) + "and Max age = " + str(maxAge))
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'updateExperimentSetup putAPI is executed with maxAge={maxAge} and minAge={minAge} for Conversion')
def step_impl(context, maxAge, minAge):
    try:
        context.updateExperimentSetup_response = requests.put(context.url,
                                                              headers=context.Authorization,
                                                              json=payload.updateConversionBody(maxAge, minAge))
        context.updateExperimentSetup_response_json = context.updateExperimentSetup_response.json()
        log.debug("Update the experiment setup with the following details: Min age = "
                  + str(minAge) + "and Max age = " + str(maxAge))
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'updateExperimentSetup putAPI is executed with maxAge={maxAge} and minAge={minAge} for Appinstall')
def step_impl(context, maxAge, minAge):
    try:
        context.updateExperimentSetup_response = requests.put(context.url,
                                                              headers=context.Authorization,
                                                              json=payload.updateAppInstallBody(maxAge, minAge))
        context.updateExperimentSetup_response_json = context.updateExperimentSetup_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from updateExperimentSetup is false')
def step_impl(context):
    try:
        assert context.updateExperimentSetup_response_json['error'] == False
        log.debug("{}{}".format("Login error status: ", context.updateExperimentSetup_response_json['error']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'verify the status of the experiment setup is Updated')
def step_impl(context):
    try:
        assert context.updateExperimentSetup_response_json['data']['status'] == 'Updated'
        log.debug("The status of the updated experiment setup is : "
                  + context.updateExperimentSetup_response_json['data']['status'] + "\n\n")
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step11.1---------------------


@given(u'the adaccount id, date preset, DevicePlatform breakdown, campaign IDs and the DevicePlatform endpoint')
def step_impl(context):
    log.info("---------------Get DevicePlatform data---------------")
    try:
        endpoint = "{}{}{}{}".format(apiResources.api, apiResources.getAdaccount, payload.getAdaccountID()
                                     , apiResources.breakdown)
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        context.header = {
            "date_preset": "last_60d",
            "breakdown": "device_platform",
            "campaign_ids": payload.getCampaignIDs()
        }
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the DevicePlatform getAPI is executed')
def step_impl(context):
    try:
        context.DevicePlatform_response = requests.get(context.url,
                                                       headers=context.Authorization,
                                                       params=context.header)
        context.DevicePlatform_response_json = context.DevicePlatform_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from the getDevicePlatform is false')
def step_impl(context):
    try:
        assert context.DevicePlatform_response_json['error'] == False
        log.debug("{}{}".format("Login error status: ", context.DevicePlatform_response_json['error']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'verify that the initial data from getDevicePlatform is blank')
def step_impl(context):
    try:
        if context.DevicePlatform_response_json['data']['breakdown'] == []:
            log.debug("DevicePlatform breakdown API successfully executed \n\n")
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step11.2---------------------

@given(u'the client id, ad account id, experiment setup id and the getCreative endpoint')
def step_impl(context):
    log.info("---------------Get creative---------------")
    try:
        endpoint = "{}{}{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), apiResources.getAdaccount,
                                           payload.getAdaccountID(), apiResources.experimentSetup,
                                           payload.getExperimentSetupID(), apiResources.getCreative)
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'getCreative getAPI is executed')
def step_impl(context):
    try:
        context.getCreative_response = requests.get(context.url,
                                                    headers=context.Authorization)
        context.getCreative_response_json = context.getCreative_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from getCreative is false')
def step_impl(context):
    try:
        assert context.getCreative_response_json['error'] == False
        log.debug("{}{}".format("Login error status: ", context.getCreative_response_json['error']) + "\n\n")
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'verify that the data body is empty')
def step_impl(context):
    try:
        assert context.getCreative_response_json['data'] == {'data': []}
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step12.1---------------------


@given(u'the adaccount id, date preset, Region breakdown, campaign IDs and the Region endpoint')
def step_impl(context):
    log.info("---------------Get Region data---------------")
    try:
        endpoint = "{}{}{}{}".format(apiResources.api, apiResources.getAdaccount, payload.getAdaccountID()
                                     , apiResources.breakdown)
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        context.header = {
            "date_preset": "last_60d",
            "breakdown": "region",
            "campaign_ids": payload.getCampaignIDs()
        }
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the Region getAPI is executed')
def step_impl(context):
    try:
        context.region_response = requests.get(context.url,
                                               headers=context.Authorization,
                                               params=context.header)
        context.region_response_json = context.region_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from the getRegion is false')
def step_impl(context):
    try:
        assert context.region_response_json['error'] == False
        log.debug("{}{}".format("Login error status: ", context.region_response_json['error']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'verify that the initial data from getRegion is blank')
def step_impl(context):
    try:
        if context.region_response_json['data']['breakdown'] == []:
            log.debug("Region breakdown API successfully executed \n\n")
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step12.2---------------------

@given(u'the client id and the getCreativeFiles endpoint')
def step_impl(context):
    log.info("---------------Get creative files---------------")
    try:
        endpoint = "{}{}{}".format(apiResources.clients, payload.getClientID(), apiResources.getCreativeFiles)
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'getCreativeFiles getAPI is executed')
def step_impl(context):
    try:
        context.getCreativeFiles_response = requests.get(context.url,
                                                         headers=context.Authorization)
        context.getCreativeFiles_response_json = context.getCreativeFiles_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from getCreativeFiles is false')
def step_impl(context):
    try:
        assert context.getCreativeFiles_response_json['error'] == False
        log.debug("{}{}".format("Login error status: ", context.getCreativeFiles_response_json['error'])
                  + "\n\n")
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'store the response that we get from getCreativeFiles')
def step_impl(context):
    try:
        payload.saveCreativeFiles(context.getCreativeFiles_response)
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step13.1---------------------

@given(u'the adaccount id, json and media plan end point')
def step_impl(context):
    log.info("---------------Generate Media Plan---------------")
    try:
        endpoint = "{}{}{}{}".format(apiResources.api, apiResources.getAdaccount, payload.getAdaccountID()
                                     , apiResources.generateMediaPlan)
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.payload = generateMediaPlanPayload()
        context.Authorization = {'Authorization': payload.getToken()}
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the generateMediaPlan postAPI is executed')
def step_impl(context):
    try:
        context.generateMediaPlan_response = requests.post(context.url,
                                                           headers=context.Authorization,
                                                           json=context.payload)
        context.generateMediaPlan_response_json = context.generateMediaPlan_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from the postgenerateMediaPlan is false')
def step_impl(context):
    try:
        assert context.generateMediaPlan_response_json['error'] == False
        log.debug("{}{}".format("Login error status: ", context.generateMediaPlan_response_json['error']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'verify that success is true')
def step_impl(context):
    try:
        if context.generateMediaPlan_response_json['data']['success'] == True:
            log.debug(context.generateMediaPlan_response_json)
            log.debug("Media plan created successfully \n\n")
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step13.2---------------------


@given(u'the client id and the getCreativeTemplate endpoint')
def step_impl(context):
    log.info("---------------Get creative template files---------------")
    try:
        endpoint = "{}{}{}".format(apiResources.clients, payload.getClientID(),
                                   apiResources.getCreativeTemplates)
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'getCreativeTemplate getAPI is executed')
def step_impl(context):
    try:
        context.getCreativeTemplate_response = requests.get(context.url,
                                                            headers=context.Authorization)
        context.getCreativeTemplate_response_json = context.getCreativeTemplate_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from getCreativeTemplate is false')
def step_impl(context):
    try:
        assert context.getCreativeTemplate_response_json['error'] == False
        log.debug("{}{}".format("Login error status: ", context.getCreativeTemplate_response_json['error'])
                  + "\n\n")
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'store the response that we get from getCreativeTemplate')
def step_impl(context):
    try:
        payload.saveCreativeTemplate(context.getCreativeTemplate_response_json)
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step14.1---------------------

@given(u'the client id, objective and get media plan endpoint')
def step_impl(context):
    log.info("---------------Get Media plan data---------------")
    try:
        endpoint = "{}{}{}{}".format(apiResources.clients, payload.getClientID(), apiResources.getMediaPlan,
                                     "objective=CONVERSIONS")
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the getMediaPlan getAPI is executed')
def step_impl(context):
    try:
        context.getMediaPlan_response = requests.get(context.url,
                                                     headers=context.Authorization)
        log.debug(context.getMediaPlan_response)
        context.getMediaPlan_response_json = context.getMediaPlan_response.json()
        log.debug(context.getMediaPlan_response_json)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from the getMediaPlan is false')
def step_impl(context):
    try:
        assert context.getMediaPlan_response_json['error'] == False
        log.debug("{}{}".format("Get Media Plan status: ", context.getMediaPlan_response_json['error']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'compare the media plan created date, other details and save the media plan id')
def step_impl(context):
    id_list = []
    for result in context.getMediaPlan_response_json['data']:
        id_list.append(result['id'])
    payload.setMediaPlanList(id_list)
    log.debug("{}{}".format("Media plans ids available are", payload.getMediaPlanList()))
    payload.setMediaPlanID(max(id_list))
    log.debug("{}{}{}".format("The media plan id is: ", payload.getMediaPlanID(), "\n\n"))


# ----------------------Step14.2---------------------


@given(u'the client id and the getPixel endpoint')
def step_impl(context):
    log.info("---------------Get Pixel ID---------------")
    try:
        endpoint = "{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), apiResources.getAdaccount,
                                       payload.getAdaccountID(), apiResources.getPixelIDs)
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'getPixel getAPI is executed')
def step_impl(context):
    try:
        context.getPixel_response = requests.get(context.url,
                                                 headers=context.Authorization)
        context.getPixel_response_json = context.getPixel_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from getPixel is false')
def step_impl(context):
    try:
        assert context.getPixel_response_json['error'] == False
        log.debug("{}{}".format("Login error status: ", context.getPixel_response_json['error']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'store the pixel id if accessible is true')
def step_impl(context):
    try:
        values = []
        for result in context.getPixel_response_json['data']:
            if not result['error'] and result['accessible']:
                values.append(result['value']['pixel_id'])
        payload.savePixelID(values)
        log.debug("{}{}".format("Pixel ids are: ", payload.getPixelID()) + "\n\n")
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step15.1---------------------


@given(u'the media plan ID and the media plan endpoint')
def step_impl(context):
    log.info("---------------Get Media plan details---------------")
    try:
        endpoint = "{}{}{}{}".format(apiResources.clients, payload.getClientID()
                                     , apiResources.fetchMediaPlan, payload.getMediaPlanID())
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the fetchMediaPlan getAPI is executed')
def step_impl(context):
    try:
        context.MediaPlan_response = requests.get(context.url,
                                                  headers=context.Authorization)
        context.MediaPlan_response_json = context.MediaPlan_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from the fetchMediaPlan is false')
def step_impl(context):
    try:
        assert context.MediaPlan_response_json['error'] == False
        log.debug("{}{}".format("Media plan fetch status: ", context.MediaPlan_response_json['error']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'get the details of the media plan created')
def step_impl(context):
    try:
        payload.setMediaPlanDetails(context.MediaPlan_response_json)
        log.debug("{}{}".format("Media plan details - ", payload.getMediaPlanDetails()))
    except Exception as e:
        log.exception(str(e))
        raise e

# ----------------------Step15.2---------------------


@given(u'the client id, ad account id, experiment setup id and the postCreative endpoint')
def step_impl(context):
    log.info("---------------Post the creative---------------")
    try:
        endpoint = "{}{}{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), apiResources.getAdaccount,
                                           payload.getAdaccountID(), apiResources.experimentSetup,
                                           payload.getExperimentSetupID(), apiResources.getCreative)
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        log.debug("Post the creative: " + str(apiResources.getCreative))
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'postCreative postAPI is executed for Leadgen of {Type}')
def step_impl(context, Type):
    setCreativeType(Type)
    try:
        context.postCreative_response = requests.post(context.url,
                                                      headers=context.Authorization,
                                                      json=payload.getPostCreativeBodyForLeadgen(Type))
        context.postCreative_response_json = context.postCreative_response.json()
        log.debug("Post the creative: " + str(apiResources.getCreative))
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'postCreative postAPI is executed for Traffic of {Type}')
def step_impl(context, Type):
    setCreativeType(Type)
    try:
        context.postCreative_response = requests.post(context.url,
                                                      headers=context.Authorization,
                                                      json=payload.getPostCreativeBodyForTraffic(Type))
        context.postCreative_response_json = context.postCreative_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'postCreative postAPI is executed for Conversion')
def step_impl(context):
    try:
        context.postCreative_response = requests.post(context.url,
                                                      headers=context.Authorization,
                                                      json=payload.getPostCreativeBodyForConversion())
        context.postCreative_response_json = context.postCreative_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'postCreative postAPI is executed for AppInstall')
def step_impl(context):
    try:
        context.postCreative_response = requests.post(context.url,
                                                      headers=context.Authorization,
                                                      json=payload.getPostCreativeBodyForAppinstall())
        context.postCreative_response_json = context.postCreative_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from postCreative is false')
def step_impl(context):
    try:
        assert context.postCreative_response_json['error'] == False
        log.debug("{}{}".format("Login error status: ", context.postCreative_response_json['error']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'save the creative ID')
def step_impl(context):
    try:
        id = context.postCreative_response_json['data']['id']
        payload.saveCreativeID(id)
        log.debug("The creative ID is: " + str(payload.getCreativeID()) + "\n\n")
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step16---------------------

@then(u'store the json response from getCreative')
def step_impl(context):
    log.info("---------------Get the creative---------------\n\n")
    try:
        payload.saveCreatives(context.getCreative_response_json)
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step17---------------------


@given(u'the experiment setup id and the storyname endpoint')
def step_impl(context):
    log.info("---------------Get storyname---------------")
    try:
        endpoint = "{}{}{}".format(apiResources.getExpSetup, payload.getExperimentSetupID(), apiResources.getStoryName)
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'getStoryName getAPI is executed')
def step_impl(context):
    try:
        context.getStoryName_response = requests.get(context.url,
                                                     headers=context.Authorization)
        context.getStoryName_response_json = context.getStoryName_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from getStoryName is false')
def step_impl(context):
    try:
        context.getStoryName_response_json['error'] == False
        log.debug("{}{}".format("Login error status: ", context.getStoryName_response_json['error']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'save the story id')
def step_impl(context):
    try:
        payload.saveStoryID(context.getStoryName_response_json['data']['story_id'])
        log.debug("Story ID is: " + payload.getStoryID() + "\n\n")
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step18---------------------


@given(u'client id, ad account id, experiment setup id and publish endpoint')
def step_impl(context):
    log.info("---------------Publish request---------------")
    try:
        endpoint = "{}{}{}{}{}{}{}".format(apiResources.getids, payload.getClientID(), apiResources.getAdaccount,
                                           payload.getAdaccountID(), apiResources.experimentSetup,
                                           payload.getExperimentSetupID(), apiResources.publish)
        context.url = getConfig()['API']['endpoint'] + endpoint
        context.Authorization = {'Authorization': payload.getToken()}
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'publish postAPI is executed for Leadgen')
def step_impl(context):
    try:
        context.publish_response = requests.post(context.url,
                                                 headers=context.Authorization,
                                                 json=payload.getPublishBodyLeadgen(getCreativeType()))
        context.publish_response_json = context.publish_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'publish postAPI is executed for Traffic')
def step_impl(context):
    try:
        context.publish_response = requests.post(context.url,
                                                 headers=context.Authorization,
                                                 json=payload.getPublishBodyTraffic(getCreativeType()))
        context.publish_response_json = context.publish_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'publish postAPI is executed for Conversion')
def step_impl(context):
    try:
        context.publish_response = requests.post(context.url,
                                                 headers=context.Authorization,
                                                 json=payload.getPublishBodyConversion())
        context.publish_response_json = context.publish_response.json()
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'publish postAPI is executed for AppInstall')
def step_impl(context):
    try:
        context.publish_response = requests.post(context.url,
                                                 headers=context.Authorization,
                                                 json=payload.getPublishBodyAppInstall())
        context.publish_response_json = context.publish_response.json()
        log.info(context.publish_response_json)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'the error response from publish is false and status is requested')
def step_impl(context):
    try:
        print(context.publish_response_json)
        assert context.publish_response_json['error'] == False
        assert context.publish_response_json['data']['status'] == 'requested'
        log.debug("{}{}".format("Login error status: ", context.publish_response_json['error']))
        log.debug("Status of the API request is: " + context.publish_response_json['data']['status'] + "\n\n")
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'save the publish request id')
def step_impl(context):
    try:
        ID = context.publish_response_json['data']['publish_request_id']
    except Exception as e:
        log.exception(str(e))
        raise e


# ----------------------Step19---------------------


@given(u'experiment setup id and the endpoint')
def step_impl(context):
    log.info("---------------AdsPipeline---------------")
    try:
        context.url = getConfig()['API']['adspipeline'] + apiResources.publishStatus
        log.debug(f"URL is set to: " + context.url)
    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'getAPI is executed')
def step_impl(context):
    try:
        context.status = requests.get(context.url)
        context.status_json = context.status.json()
        for result in context.status_json['data']['tasks']:
            if result['storyId'] == payload.getStoryID():
                break
        context.statusValue = result['status']
        while context.statusValue == "PENDING" or context.statusValue == "PROCESSING":
            time.sleep(30)
            context.status = requests.get(context.url)
            context.status_json = context.status.json()
            for result in context.status_json['data']['tasks']:
                if result['storyId'] == payload.getStoryID():
                    break
            context.statusValue = result['status']
            if context.statusValue == "SUCCESS" or context.statusValue == "FAILED":
                break

    except Exception as e:
        log.exception(str(e))
        raise e


@when(u'error status is 200')
def step_impl(context):
    try:
        assert context.status_json['statusCode'] == 200
        log.debug("{}{}".format("The status code is: ", context.status_json['statusCode']))
    except Exception as e:
        log.exception(str(e))
        raise e


@then(u'verify the status is SUCCESS')
def step_impl(context):
    try:
        statusCode = context.status_json['statusCode']
        assert statusCode == 200
        if context.statusValue == "SUCCESS":
            log.info("Status: " + context.statusValue)
            log.info("The experiment setup successfully published to FB \n")
        else:
            log.info("Status: " + context.statusValue)
            assert context.statusValue == "SUCCESS"
            log.info("FAILURE IN ADS PIPELINE - please check adspipeline for more information \n")
    except Exception as e:
        log.exception(str(e))
        raise e
