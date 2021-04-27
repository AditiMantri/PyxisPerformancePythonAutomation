import payload
#
# #global variable
# token = "Key value comes here"
# clientID = 0
# adaccountID = 0

# Login and password that gets passed to login to aiquire dashboard
def loginPayload(login, password):
    body = {
        "email" : login,
        "password" : password
    }
    return body


# Unique Token that is set when the user logs in for the first time
def setToken(token):
    payload.token = token


# Get the token value
def getToken():
    return "Token "+token


# Set the client id where the experiment setup is to be set up
def setClientID(clientID):
    payload.clientID = clientID


# Get the client id value
def getClientID():
    return payload.clientID


# Set the account id where the experiment setup is to be set
def setAdaccountID(adaccountnID):
    payload.adaccountID = adaccountnID


# Get the account id
def getAdaccountID():
    return payload.adaccountID;


# Get the config
def saveConfig(config):
    payload.config = config


# Get the config json
def getConfig():
    return payload.config


# Set the page ids for a particular client and ad account
def setPages(page_ids):
    payload.page_ids = page_ids


# Get the page id list
def getPages():
    return payload.page_ids


# Set the Instagram account ids that are accessible
def setInstagramAccounts(insta_ids):
    payload.insta_ids = insta_ids


# Return the Instagram account ids
def getInstagramAccounts():
    return payload.insta_ids


# Set the list of audience ids
def setAudienceID(audienceID):
    payload.audienceID = audienceID


# Get the list of audience
def getAudienceID():
    return payload.audienceID


# Get JSON body to create experiment setup
def setLeadGenBody():
    json_body = {"data":{"campaign":{"name":"LeadGenAPItesting","status":"PAUSED","objective":"Lead Generation","buying_type":"AUCTION","bid_strategy":"Lowest Cost","daily_budget":100,"campaign_budget":"DAILY_BUDGET"},"ads_groups":[{"ad":{"status":"ACTIVE"},"adset":{"status":"ACTIVE","billing_event":"IMPRESSIONS","adset_time_start":"2021-04-10T13:30:17+05:30","attribution_spec":[{"event_type":"CLICK_THROUGH","window_days":1}]},"ad_type":"image","creative":{"object_type":"SHARE","Creative Type":"Link Page Post Ad","call_to_action_type":"LEARN_MORE"},"targeting":{"targeting_optimization":"none","brand_safety_content_filter_levels":["FACEBOOK_STANDARD","AN_STANDARD"]},"story_spec":{"page_id":{"page_id":"107973334116438"}},"geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home","recent"]},"excluded_geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home"]}}],"name":"LeadGenAPItesting","extras":{"ads_groups$geo_locations":[],"ads_groups$excluded_geo_locations":[],"ads_groups$targeting$flexible_spec":[],"ads_groups$targeting$excluded_flexible_spec":[]}}}
    return json_body


# Store the experiment setup id after creation
def saveExperimentSetupID(id):
    payload.ID = id


# Get the experiment setup ID
def getExperimentSetupID():
    return payload.ID