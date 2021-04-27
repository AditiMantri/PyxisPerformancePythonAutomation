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
    json_body = {"data":{"campaign":{"name":"LeadGenAPItesting","status":"PAUSED","objective":"Lead Generation","buying_type":"AUCTION","bid_strategy":"Lowest Cost","daily_budget":80,"campaign_budget":"DAILY_BUDGET"},"ads_groups":[{"ad":{"status":"ACTIVE"},"adset":{"status":"ACTIVE","billing_event":"IMPRESSIONS","promoted_object":"LEAD_GENERATION","adset_time_start":"2021-04-27T20:16:59+05:30","attribution_spec":[{"event_type":"CLICK_THROUGH","window_days":1}],"optimization_goal":"LEAD_GENERATION"},"ad_type":"image","creative":{"object_type":"SHARE","Creative Type":"Link Page Post Ad","call_to_action_type":"LEARN_MORE"},"targeting":{"targeting_optimization":"none","brand_safety_content_filter_levels":["FACEBOOK_STANDARD","AN_STANDARD"]},"story_spec":{"page_id":{"page_id":"107973334116438"}},"geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home","recent"]},"excluded_geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home"]}}],"name":"LeadGenAPItesting","extras":{"ads_groups$geo_locations":[],"ads_groups$excluded_geo_locations":[],"ads_groups$targeting$flexible_spec":[],"ads_groups$targeting$excluded_flexible_spec":[]}}}
    return json_body


# Store the experiment setup id after creation
def saveExperimentSetupID(id):
    payload.ID = id


# Get the experiment setup ID
def getExperimentSetupID():
    return payload.ID


# Save the response
def saveGetExperimentSetupResponse(response):
    payload.response = response

# Get the response
def getGetExperimentSetupResponse():
    return payload.response

#update exp setup
def updateLeadGenBody():
    updatedJSON = {"data":{"campaign":{"name":"LeadGenAPItesting","status":"PAUSED","objective":"Lead Generation","buying_type":"AUCTION","bid_strategy":"Lowest Cost","daily_budget":80,"campaign_budget":"DAILY_BUDGET"},"ads_groups":[{"ad":{"status":"ACTIVE"},"adset":{"name":"LeadGenAPItesting","status":"ACTIVE","billing_event":"IMPRESSIONS","promoted_object":"LEAD_GENERATION","adset_time_start":"2021-04-27T20:16:59+05:30","attribution_spec":[{"event_type":"CLICK_THROUGH","window_days":1}],"optimization_goal":"LEAD_GENERATION"},"ad_type":"image","creative":{"object_type":"SHARE","Creative Type":"Link Page Post Ad","call_to_action_type":"LEARN_MORE"},"targeting":{"age_max":33,"age_min":22,"custom_audiences":[{"id":"23847574287240410","name":"Lookalike (IN, 1% to 5%) - Ranit's testing audience","subtype":"LOOKALIKE"},{"id":"23847574322950410","name":"Special Ad Audience (IN, 2%) - Ranit's testing audience","subtype":"REGULATED_CATEGORIES_AUDIENCE"}],"targeting_optimization":"none","excluded_custom_audiences":[{"id":"23847574323680410","name":"Special Ad Audience (IN, 4% to 7%) - Ranit's testing audience","subtype":"REGULATED_CATEGORIES_AUDIENCE"},{"id":"23847574286990410","name":"Lookalike (IN, 1%) - Ranit's testing audience","subtype":"LOOKALIKE"}],"brand_safety_content_filter_levels":["FACEBOOK_STANDARD","AN_STANDARD"]},"story_spec":{"page_id":{"page_id":"245069182739198"}},"geo_locations":{"countries":[],"cities":[{"country":"IN","name":"Varanasi","region":"Uttar Pradesh","key":"1046744"}],"regions":[{"name":"Karnataka","country":"IN","key":"1738"}],"zips":[],"country_groups":[],"location_types":["home","recent"]},"excluded_geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home"]}}],"name":"LeadGenAPItesting","extras":{"ads_groups$geo_locations":[{"key":"1046744","name":"Varanasi","type":"city","country_code":"IN","country_name":"India","region":"Uttar Pradesh","region_id":1754,"supports_region":'true',"supports_city":'true',"responseType":"location","text":"Varanasi, Uttar Pradesh, India city"},{"key":"1738","name":"Karnataka","type":"region","country_code":"IN","country_name":"India","supports_region":'true',"supports_city":'true',"responseType":"location","text":"Karnataka, India region"}],"ads_groups$excluded_geo_locations":[],"ads_groups$targeting$flexible_spec":[],"ads_groups$targeting$excluded_flexible_spec":[]}}}
    return updatedJSON


# Store getCreativeFiles
def saveCreativeFiles(creativeFiles):
    payload.creativeFiles = creativeFiles


# Get creative files
def getCreativeFiles():
    return payload.creativeFiles


# Store getCreativeTemplate
def saveCreativeTemplate(creativeTemplate):
    payload.creativeTemplate = creativeTemplate

# Get getCreativeTemplate
def getCreativeTemplate():
    return payload.creativeTemplate

# Save the pixel IDS
def savePixelID(values):
    payload.pixelID = values


# Get the list of pixel IDS
def getPixelID():
    return payload.pixelID


# Post creative body
def getPostCreativeBody():
    json_body = {"type":"single image","name":"cr_bmp","files":[{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1617808700111_img-ui-cdgsx.bmp","name":"1617808700111_img-ui-cdgsx.bmp","type":"image/bmp","file_type":"image/bmp","carouselIndex":0}],"form_data":{"lead_gen_form_id":"254429285840340","adType":"single image","creativeName":"cr_bmp","primaryText":"12","displayUrl":"","utmBuilderForDisplayUrl":[],"includedGeoLocations":[],"tracking_specs":{"pixel_id":"706589963501348"},"viewTags":"","cta":"LEARN_MORE","carousel":[{"file":"1617808700111_img-ui-cdgsx.bmp","headline":"123","description":"","websiteUrl":"www.pyxisocial.com","utmBuilderForWebsiteUrl":[],"deepLink":""}]},"creative_json":{"lead_gen_form_id":"254429285840340","adType":"single image","creativeName":"cr_bmp","primaryText":"12","displayUrl":"","utmBuilderForDisplayUrl":[],"includedGeoLocations":{"location_types":["home","recent"],"cities":[],"countries":[],"regions":[],"zips":[],"country_groups":[]},"tracking_specs":{"pixel_id":"706589963501348"},"viewTags":"","cta":"LEARN_MORE","carousel":[{"file":"1617808700111_img-ui-cdgsx.bmp","headline":"123","description":"","websiteUrl":"www.pyxisocial.com","utmBuilderForWebsiteUrl":[],"deepLink":""}]},"approver_email":"","cc_emails":"","approval_status":"draft","comments":"","preview_url":""}
    return json_body

# Save the creative ID
def saveCreativeID(id):
    payload.creativeID = id

# Retrieve the creative ID
def getCreativeID():
    return payload.creativeID

# Save all the creatives
def saveCreatives(creatives):
    payload.creatives = creatives

# Retrive all the creatives
def getCreatives():
    return payload.creatives

# Save Story ID
def saveStoryID(storyID):
    payload.storyID = storyID

# Get storyID
def getStoryID():
    return payload.storyID

# publish
def getPublishBody():
    return {"creative_ids":[1046],"story_id":"AQ-E:M:T:-TEST-A-BRD--0421-    1069","json":[{"campaign":{"name":"aipsm_TEST_FBIN_O:LN_Base:Multi_*AQ-E:M:T:-TEST-A-BRD--0421-    1069*_DEFAULT_Apr21_LeadGenAPItesting_1069","status":"PAUSED","objective":"Lead Generation","buying_type":"AUCTION","bid_strategy":"Lowest Cost","daily_budget":80,"campaign_budget":"DAILY_BUDGET"},"ads_groups":[{"ad":{"name":"aipsm_TEST_FBIN_O:LN_Base:Multi_22to33_ALL_MP_##AQ-FBIN-TEST-SI-270421-476|cr_bmp##__DEFAULT_27Apr21_1069","status":"ACTIVE","tracking_specs":{"fb_pixel":"706589963501348"}},"adset":{"name":"aipsm_TEST_FBIN_O:LN_Base:Multi_22to33_ALL_MP__DEFAULT_27Apr21_LeadGenAPItesting_1069","status":"ACTIVE","billing_event":"IMPRESSIONS","promoted_object":"LEAD_GENERATION","adset_time_start":"2021-04-27T20:16:59+05:30","attribution_spec":[{"event_type":"CLICK_THROUGH","window_days":1}],"optimization_goal":"LEAD_GENERATION"},"ad_type":"image","creative":{"creative_type":"Link Page Post Ad","object_type":"SHARE"},"targeting":{"age_max":33,"age_min":22,"custom_audiences":[{"id":"23847574287240410","name":"Lookalike (IN, 1% to 5%) - Ranit's testing audience","subtype":"LOOKALIKE"},{"id":"23847574322950410","name":"Special Ad Audience (IN, 2%) - Ranit's testing audience","subtype":"REGULATED_CATEGORIES_AUDIENCE"}],"targeting_optimization":"none","excluded_custom_audiences":[{"id":"23847574323680410","name":"Special Ad Audience (IN, 4% to 7%) - Ranit's testing audience","subtype":"REGULATED_CATEGORIES_AUDIENCE"},{"id":"23847574286990410","name":"Lookalike (IN, 1%) - Ranit's testing audience","subtype":"LOOKALIKE"}],"brand_safety_content_filter_levels":["FACEBOOK_STANDARD","AN_STANDARD"]},"story_spec":{"page_id":"245069182739198"},"geo_locations":{"countries":[],"cities":[{"country":"IN","name":"Varanasi","region":"Uttar Pradesh","key":"1046744"}],"regions":[{"name":"Karnataka","country":"IN","key":"1738"}],"zips":[],"country_groups":[],"location_types":["home","recent"]},"excluded_geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home"]},"photo_data_spec":{"call_to_action":{"type":"LEARN_MORE","value":{"lead_gen_form_id":"254429285840340"}},"image_name":"1617808700111_img-ui-cdgsx.bmp","link":"https://fb.me/","message":"123","name":"12"}}]}],"creative_s3_url":"https://s3.console.aws.amazon.com/s3/buckets/fb-adsuploading-files-bucket/dev-upload-form/client-122/creative/","campaignDetails":{"1046":[{"name":"aipsm_TEST_FBIN_O:LN_Base:Multi_*AQ-E:M:T:-TEST-A-BRD--0421-    1069*_DEFAULT_Apr21_LeadGenAPItesting_1069","adsets":[{"adset_name":"aipsm_TEST_FBIN_O:LN_Base:Multi_22to33_ALL_MP__DEFAULT_27Apr21_LeadGenAPItesting_1069","ads":[{"ad_name":"aipsm_TEST_FBIN_O:LN_Base:Multi_22to33_ALL_MP_##AQ-FBIN-TEST-SI-270421-476|cr_bmp##__DEFAULT_27Apr21_1069"}]}]}]}}

# Save publish request ID
def setPublishRequestID(publishID):
    payload.publishID = publishID


# Get publish request ID
def getPublishRequestID():
    return  payload.publishID
