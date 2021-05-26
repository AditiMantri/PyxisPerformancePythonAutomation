import payload
import xlrd

# -------------------------------- COMMON METHODS --------------------------------

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
    return "Token "+ payload.token


# Set the client id where the experiment setup is to be set up
def setClientID(clientID):
    payload.clientID = clientID


# Get the client id value
def getClientID():
    return payload.clientID


# Set the account id where the experiment setup is to be set
def setAdaccountID(adaccountID):
    payload.adaccountID = adaccountID


# Get the account id
def getAdaccountID():
    return payload.adaccountID;


# Get the config
def saveConfig(config):
    payload.config = config


# Get the config json
def getConfig():
    return payload.config

def setPagejson(page):
    payload.page_json = page

def getPagejson():
    return payload.page_json

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



# Store the experiment setup id after creation
def saveExperimentSetupID(id):
    payload.id = id


# Get the experiment setup ID
def getExperimentSetupID():
    return payload.id


# Save the response
def saveGetExperimentSetupResponse(response):
    payload.response = response

# Get the response
def getGetExperimentSetupResponse():
    return payload.response


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


# Save the creative ID
def saveCreativeID(creativeID):
    payload.creativeID = creativeID

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


# -------------------------------- TRAFFIC --------------------------------

# Traffic body
def setTrafficBody(CampaignName, DailyBudget, AdsetStartTime, page):
    payload.setCampaignName(CampaignName)
    payload.setDailyBudget(DailyBudget)
    payload.setAdsetStartTime(AdsetStartTime)
    payload.setPage(page)
    json_body = {"data":{"campaign":{"name":CampaignName,"status":"PAUSED","objective":"Traffic","buying_type":"AUCTION","bid_strategy":"Lowest Cost","daily_budget":DailyBudget,"campaign_budget":"DAILY_BUDGET"},"ads_groups":[{"ad":{"status":"ACTIVE"},"adset":{"status":"ACTIVE","billing_event":"IMPRESSIONS","adset_time_start":AdsetStartTime,"attribution_spec":[{"event_type":"CLICK_THROUGH","window_days":1}],"destination_type":"Website","optimization_goal":"LANDING_PAGE_VIEWS"},"ad_type":"image","creative":{"object_type":"SHARE","Creative Type":"Link Page Post Ad","instagram_actor_id":"2685713601466369","call_to_action_type":"LEARN_MORE"},"targeting":{"targeting_optimization":"none","brand_safety_content_filter_levels":["FACEBOOK_STANDARD","AN_STANDARD"]},"story_spec":{"page_id":{"page_id":page},"instagram_actor_id":"2685713601466369"},"geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home","recent"]},"excluded_geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home"]}}],"name":CampaignName,"extras":{"ads_groups$geo_locations":[],"ads_groups$excluded_geo_locations":[],"ads_groups$targeting$flexible_spec":[],"ads_groups$targeting$excluded_flexible_spec":[]}}}
    # loc = ("Utilities/data.xls")
    # wb = xlrd.open_workbook(loc)
    # sheet = wb.sheet_by_index(0)
    # json_body = sheet.cell_value(1, 2)
    return json_body


# update traffic
def updateTraffic(age_max,age_min):
    name = payload.getCampaignName()
    DailyBudget = payload.getDailyBudget()
    AdsetStartTime = payload.getAdsetStartTime()
    page = payload.getPage()
    payload.setAgeMax(age_max)
    payload.setAgeMin(age_min)
    updatedJSON = {"data":{"campaign":{"name":name,"status":"PAUSED","objective":"Traffic","buying_type":"AUCTION","bid_strategy":"Lowest Cost","daily_budget":DailyBudget,"campaign_budget":"DAILY_BUDGET"},"ads_groups":[{"ad":{"status":"ACTIVE"},"adset":{"name":name,"status":"ACTIVE","billing_event":"IMPRESSIONS","adset_time_start":AdsetStartTime,"attribution_spec":[{"event_type":"CLICK_THROUGH","window_days":1}],"destination_type":"Website","optimization_goal":"LANDING_PAGE_VIEWS"},"ad_type":"image","creative":{"object_type":"SHARE","Creative Type":"Link Page Post Ad","call_to_action_type":"LEARN_MORE"},"targeting":{"age_max":age_max,"age_min":age_min,"genders":"2","user_os":"All","placements":"Manual_Placements","device_platforms":["mobile","desktop"],"facebook_positions":["feed"],"publisher_platforms":["facebook"],"targeting_expansion":["expansion_all"],"targeting_optimization":"none","brand_safety_content_filter_levels":["FACEBOOK_STANDARD","AN_STANDARD"]},"story_spec":{"page_id":{"page_id":page}},"geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":["android_free_store"],"location_types":["home","recent"]},"excluded_geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home"]}}],"name":name,"extras":{"ads_groups$geo_locations":[{"key":"android_free_store","name":"Free Android store countries","type":"country_group","country_codes":["AF","AL","DZ","AS","AD","AO","AI","AQ","AG","AR","AM","AW","AU","AT","AZ","BH","BD","BB","BY","BE","BZ","BJ","BM","BT","BO","BA","BW","BR","IO","VG","BN","BG","BF","BI","KH","CM","MZ","MM","NA","NR","NP","NL","FJ","NC","NZ","NI","NE","NG","NU","NF","FI","NO","OM","PK","PW","PS","PA","PG","PY","PE","PH","PN","PL","PT","PR","QA","RE","RO","RU","RW","KN","LC","MF","PM","VC","WS","SM","ST","SA","SN","RS","SC","SL","SG","SX","SK","SI","SB","SO","ZA","GS","KR","SS","ES","LK","BL","SH","SR","SJ","SZ","SE","CH","TW","TJ","TZ","TH","BS","TG","TK","TO","TT","TN","TR","TM","TC","TV","UG","UA","AE","GB","UM","US","VI","UY","UZ","VU","VA","VE","VN","WF","EH","YE","ZM","ZW","FR","GF","PF","TF","GA","GM","GE","DE","GH","GI","GR","GL","GD","GP","GU","GT","GG","GN","GW","GY","HT","HN","HK","HU","IS","IN","ID","IQ","IE","IM","IL","IT","CI","JM","JP","JE","JO","KZ","KE","KI","XK","KW","KG","LA","LV","LB","LS","LR","LY","LI","LT","LU","MO","MK","MG","MW","MY","MV","ML","MT","MP","MH","MQ","MR","MU","YT","MX","MD","MC","MN","ME","MS","MA","CA","CV","KY","CF","TD","CL","CN","CX","CC","CO","KM","CG","CD","CK","CR","HR","CW","CY","CZ","DK","DJ","DM","DO","TL","EC","EG","SV","GQ","ER","EE","ET","FK","FO","FM"],"is_worldwide":'false',"supports_region":'true',"supports_city":'true',"responseType":"location","text":"Free Android store countries country_group"}],"ads_groups$excluded_geo_locations":[],"ads_groups$targeting$flexible_spec":[],"ads_groups$targeting$excluded_flexible_spec":[]}}}
    return updatedJSON


# Post creative body for traffic
def getPostCreativeBodyForTraffic(Type):
    if Type in "Image":
        return {"type":"single image","name":"Single Image for Traffic","files":[{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1617186586554_sda.jpg","name":"1617186586554_sda.jpg","type":"image/jpeg","file_type":"image/jpeg","carouselIndex":0}],"form_data":{"lead_gen_form_id":"254429285840340","adType":"single image","creativeName":"Single Image for Traffic","primaryText":"Traffic test","displayUrl":"www.pyxispm.com","utmBuilderForDisplayUrl":[],"includedGeoLocations":[],"tracking_specs":{"pixel_id":"706589963501348"},"viewTags":[],"cta":"LEARN_MORE","carousel":[{"file":"1617186586554_sda.jpg","headline":"PyxisPM","description":"www.pyxispm.com","websiteUrl":"www.pyxispm.com","deepLink":"","utmBuilderForWebsiteUrl":[]}]},"creative_json":{"lead_gen_form_id":"254429285840340","adType":"single image","creativeName":"Single Image for Traffic","primaryText":"Traffic test","displayUrl":"www.pyxispm.com","utmBuilderForDisplayUrl":[],"includedGeoLocations":{"location_types":["home","recent"],"cities":[],"countries":[],"regions":[],"zips":[],"country_groups":[]},"tracking_specs":{"pixel_id":"706589963501348"},"viewTags":[],"cta":"LEARN_MORE","carousel":[{"file":"1617186586554_sda.jpg","headline":"PyxisPM","description":"www.pyxispm.com","websiteUrl":"www.pyxispm.com","deepLink":"","utmBuilderForWebsiteUrl":[]}]},"approver_email":"","cc_emails":"","approval_status":"draft","comments":"","preview_url":""}
    if Type in "Video":
        return {"type":"single video","name":"Single video","files":[{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1615804150608_Planningaholiday_Compare&saveonFlights&HotelswithPayZapp.HDFCBank,India'sno.1bank_.mp4","name":"1615804150608_Planningaholiday_Compare&saveonFlights&HotelswithPayZapp.HDFCBank,India'sno.1bank_.mp4","type":"video/mp4","file_type":"video/mp4","carouselIndex":0}],"form_data":{"lead_gen_form_id":"","adType":"single video","creativeName":"Single video","primaryText":"prim","displayUrl":"","utmBuilderForDisplayUrl":[],"includedGeoLocations":[],"tracking_specs":{"pixel_id":"706589963501348"},"viewTags":[],"cta":"CONTACT_US","carousel":[{"file":"1615804150608_Planningaholiday_Compare&saveonFlights&HotelswithPayZapp.HDFCBank,India'sno.1bank_.mp4","headline":"head","description":"","websiteUrl":"www.pyxispm.com","deepLink":"","utmBuilderForWebsiteUrl":[]}]},"creative_json":{"lead_gen_form_id":"","adType":"single video","creativeName":"Single video","primaryText":"prim","displayUrl":"","utmBuilderForDisplayUrl":[],"includedGeoLocations":{"location_types":["home","recent"],"cities":[],"countries":[],"regions":[],"zips":[],"country_groups":[]},"tracking_specs":{"pixel_id":"706589963501348"},"viewTags":[],"cta":"CONTACT_US","carousel":[{"file":"1615804150608_Planningaholiday_Compare&saveonFlights&HotelswithPayZapp.HDFCBank,India'sno.1bank_.mp4","headline":"head","description":"","websiteUrl":"www.pyxispm.com","deepLink":"","utmBuilderForWebsiteUrl":[]}]},"approver_email":"","cc_emails":"","approval_status":"draft","comments":"","preview_url":""}
    if Type in "Carousel":
        return {"type":"carousel","name":"Carousel_Mix","files":[{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1615848269338_images.jpg","name":"1615848269338_images.jpg","type":"image/jpeg","file_type":"image/jpeg","carouselIndex":0},{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1615848269699_kirbxcrw69hk1ubqh48g.jpg","name":"1615848269699_kirbxcrw69hk1ubqh48g.jpg","type":"image/jpeg","file_type":"image/jpeg","carouselIndex":1},{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1615848269896_Pyxis_Logo_sic7q2.png","name":"1615848269896_Pyxis_Logo_sic7q2.png","type":"image/png","file_type":"image/png","carouselIndex":2},{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1615848278538_gif3_ebnwi2.gif","name":"1615848278538_gif3_ebnwi2.gif","type":"image/gif","file_type":"image/gif","carouselIndex":3},{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1615848289463_gif4_ubpyjt.gif","name":"1615848289463_gif4_ubpyjt.gif","type":"image/gif","file_type":"image/gif","carouselIndex":4},{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1615848298686_gif8_gpblfh.gif","name":"1615848298686_gif8_gpblfh.gif","type":"image/gif","file_type":"image/gif","carouselIndex":5},{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1615848308684_gif9_kpp03q.gif","name":"1615848308684_gif9_kpp03q.gif","type":"image/gif","file_type":"image/gif","carouselIndex":6},{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1615848338780_1min.mp4","name":"1615848338780_1min.mp4","type":"video/mp4","file_type":"video/mp4","carouselIndex":7},{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1615848360720_2mins-Copy.mp4","name":"1615848360720_2mins-Copy.mp4","type":"video/mp4","file_type":"video/mp4","carouselIndex":8},{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1615848441970_3min.mp4","name":"1615848441970_3min.mp4","type":"video/mp4","file_type":"video/mp4","carouselIndex":9}],"form_data":{"lead_gen_form_id":"","adType":"carousel","creativeName":"Carousel_Mix","primaryText":"Primary text","displayUrl":"www.hdfc.com","utmBuilderForDisplayUrl":[],"includedGeoLocations":[],"tracking_specs":{"pixel_id":"706589963501348"},"viewTags":[],"cta":"LEARN_MORE","carousel":[{"file":"1615848269338_images.jpg","headline":"1","description":"","websiteUrl":"www.pyxispm.com","deepLink":"","utmBuilderForWebsiteUrl":[]},{"file":"1615848269699_kirbxcrw69hk1ubqh48g.jpg","headline":"2","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848269896_Pyxis_Logo_sic7q2.png","headline":"3","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848278538_gif3_ebnwi2.gif","headline":"4","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848289463_gif4_ubpyjt.gif","headline":"5","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848298686_gif8_gpblfh.gif","headline":"6","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848308684_gif9_kpp03q.gif","headline":"7","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848338780_1min.mp4","headline":"8","description":"desc","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848360720_2mins-Copy.mp4","headline":"9","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848441970_3min.mp4","headline":"10","description":"","websiteUrl":"www.pyxsipm.com","utmBuilderForWebsiteUrl":[],"deepLink":""}]},"creative_json":{"lead_gen_form_id":"","adType":"carousel","creativeName":"Carousel_Mix","primaryText":"Primary text","displayUrl":"www.hdfc.com","utmBuilderForDisplayUrl":[],"includedGeoLocations":{"location_types":["home","recent"],"cities":[],"countries":[],"regions":[],"zips":[],"country_groups":[]},"tracking_specs":{"pixel_id":"706589963501348"},"viewTags":[],"cta":"LEARN_MORE","carousel":[{"file":"1615848269338_images.jpg","headline":"1","description":"","websiteUrl":"www.pyxispm.com","deepLink":"","utmBuilderForWebsiteUrl":[]},{"file":"1615848269699_kirbxcrw69hk1ubqh48g.jpg","headline":"2","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848269896_Pyxis_Logo_sic7q2.png","headline":"3","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848278538_gif3_ebnwi2.gif","headline":"4","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848289463_gif4_ubpyjt.gif","headline":"5","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848298686_gif8_gpblfh.gif","headline":"6","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848308684_gif9_kpp03q.gif","headline":"7","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848338780_1min.mp4","headline":"8","description":"desc","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848360720_2mins-Copy.mp4","headline":"9","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848441970_3min.mp4","headline":"10","description":"","websiteUrl":"www.pyxsipm.com","utmBuilderForWebsiteUrl":[],"deepLink":""}]},"approver_email":"","cc_emails":"","approval_status":"draft","comments":"","preview_url":""}


def getPublishBodyTraffic(Type):
    name = payload.getCampaignName()
    expID = str(payload.getExperimentSetupID())
    age_max = payload.getAgeMax()
    age_min = payload.getAgeMin()
    daily_budget = getDailyBudget()
    AdsetStartTime = payload.getAdsetStartTime()
    lead = payload.getPage()

    if Type == "Image":
        return {"creative_ids":[1258],"story_id":payload.getStoryID(),"json":[{"campaign":{"name":"aipsm_TEST_FBIN_O:TC_Base:Multi_*AQ-E:M:T:-TEST-N-BRD--0521-    "+expID+"*_AUTOMATION_"+name+"_"+expID+"","status":"PAUSED","objective":"Traffic","buying_type":"AUCTION","bid_strategy":"Lowest Cost","daily_budget":daily_budget,"campaign_budget":"DAILY_BUDGET"},"ads_groups":[{"ad":{"name":"aipsm_TEST_FBIN_O:TC_Base:Multi_"+age_min+"to"+age_max+"_FEMALE_MP_##AQ-FBIN-TEST-SI-110521-688|SingleImageforTraffic##__AUTOMATION_"+expID+"","status":"ACTIVE","tracking_specs":{"fb_pixel":"706589963501348"}},"adset":{"name":"aipsm_TEST_FBIN_O:TC_Base:Multi_"+age_min+"to"+age_max+"_FEMALE_MP__AUTOMATION_"+name+"_"+expID+"","status":"ACTIVE","billing_event":"IMPRESSIONS","adset_time_start":AdsetStartTime,"attribution_spec":[{"event_type":"CLICK_THROUGH","window_days":1}],"destination_type":"Website","optimization_goal":"LANDING_PAGE_VIEWS"},"ad_type":"image","creative":{"creative_type":"Link Page Post Ad","object_type":"SHARE"},"targeting":{"age_max":age_max,"age_min":age_min,"genders":[2],"user_os":"All","placements":"Manual_Placements","device_platforms":["mobile","desktop"],"facebook_positions":["feed"],"publisher_platforms":["facebook"],"targeting_expansion":["expansion_all"],"targeting_optimization":"none","brand_safety_content_filter_levels":["FACEBOOK_STANDARD","AN_STANDARD"]},"story_spec":{"page_id":"107973334116438"},"geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":["android_free_store"],"location_types":["home","recent"]},"excluded_geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home"]},"photo_data_spec":{"call_to_action":{"type":"LEARN_MORE"},"caption":"www.pyxispm.com","description":"www.pyxispm.com","image_name":"1617186586554_sda.jpg","link":"www.pyxispm.com","message":"PyxisPM","name":"Traffic test"}}]}],"creative_s3_url":"https://s3.console.aws.amazon.com/s3/buckets/fb-adsuploading-files-bucket/dev-upload-form/client-122/creative/","campaignDetails":{"1258":[{"name":"aipsm_TEST_FBIN_O:TC_Base:Multi_*AQ-E:M:T:-TEST-N-BRD--0521-    "+expID+"*_AUTOMATION_"+name+"_"+expID+"","adsets":[{"adset_name":"aipsm_TEST_FBIN_O:TC_Base:Multi_"+age_min+"to"+age_max+"_FEMALE_MP__AUTOMATION_"+name+"_"+expID+"","ads":[{"ad_name":"aipsm_TEST_FBIN_O:TC_Base:Multi_"+age_min+"to"+age_max+"_FEMALE_MP_##AQ-FBIN-TEST-SI-110521-688|SingleImageforTraffic##__AUTOMATION_"+expID+""}]}]}]}}
    if Type == "Video":
        return {"creative_ids":[1105],"story_id":payload.getStoryID(),"json":[{"campaign":{"name":"aipsm_TEST_FBIN_O:TC_Base:Multi_*AQ-E:M:T:-TEST-N-BRD--0421-    "+expID+"*_AUTOMATION_"+name+"_"+expID+"","status":"PAUSED","objective":"Traffic","buying_type":"AUCTION","bid_strategy":"Lowest Cost","daily_budget":daily_budget,"campaign_budget":"DAILY_BUDGET"},"ads_groups":[{"ad":{"name":"aipsm_TEST_FBIN_O:TC_Base:Multi_"+age_min+"to"+age_max+"_FEMALE_MP_##AQ-FBIN-TEST-GV-300421-535|Singlevideo##__AUTOMATION_"+expID+"","status":"ACTIVE","tracking_specs":{"fb_pixel":"706589963501348"}},"adset":{"name":"aipsm_TEST_FBIN_O:TC_Base:Multi_"+age_min+"to"+age_max+"_FEMALE_MP__AUTOMATION_"+name+"_"+expID+"","status":"ACTIVE","billing_event":"IMPRESSIONS","adset_time_start":AdsetStartTime,"attribution_spec":[{"event_type":"CLICK_THROUGH","window_days":1}],"destination_type":"Website","optimization_goal":"LANDING_PAGE_VIEWS"},"ad_type":"video","creative":{"object_type":"VIDEO","creative_type":"Video Page Post Ad","status":"ACTIVE"},"targeting":{"age_max":age_max,"age_min":age_min,"genders":[2],"user_os":"All","placements":"Manual_Placements","device_platforms":["mobile","desktop"],"facebook_positions":["feed"],"publisher_platforms":["facebook"],"targeting_expansion":["expansion_all"],"targeting_optimization":"none","brand_safety_content_filter_levels":["FACEBOOK_STANDARD","AN_STANDARD"]},"story_spec":{"page_id":"107973334116438"},"geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":["android_free_store"],"location_types":["home","recent"]},"excluded_geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home"]},"video_data_spec":{"call_to_action":{"type":"CONTACT_US","value":{"link":"www.pyxispm.com","link_format":"VIDEO_LPP"}},"message":"head","name":"prim","video_name":"1615804150608_Planningaholiday_Compare&saveonFlights&HotelswithPayZapp.HDFCBank,India'sno.1bank_.mp4"}}]}],"creative_s3_url":"https://s3.console.aws.amazon.com/s3/buckets/fb-adsuploading-files-bucket/dev-upload-form/client-122/creative/","campaignDetails":{"1105":[{"name":"aipsm_TEST_FBIN_O:TC_Base:Multi_*AQ-E:M:T:-TEST-N-BRD--0421-    "+expID+"*_AUTOMATION_"+name+"_"+expID+"","adsets":[{"adset_name":"aipsm_TEST_FBIN_O:TC_Base:Multi_33to44_FEMALE_MP__AUTOMATION_"+name+"_"+expID+"","ads":[{"ad_name":"aipsm_TEST_FBIN_O:TC_Base:Multi_33to44_FEMALE_MP_##AQ-FBIN-TEST-GV-300421-535|Singlevideo##__AUTOMATION_"+expID+""}]}]}]}}
    if Type == "Carousel":
        return {"creative_ids":[1260],"story_id":payload.getStoryID(),"json":[{"campaign":{"name":"aipsm_TEST_FBIN_O:TC_Base:Multi_*AQ-E:M:T:-TEST-N-BRD--0521-    "+expID+"*_AUTOMATION_"+name+"_"+expID+"","status":"PAUSED","objective":"Traffic","buying_type":"AUCTION","bid_strategy":"Lowest Cost","daily_budget":daily_budget,"campaign_budget":"DAILY_BUDGET"},"ads_groups":[{"ad":{"name":"aipsm_TEST_FBIN_O:TC_Base:Multi_"+age_min+"to"+age_max+"_FEMALE_MP_##AQ-FBIN-TEST-CR-110521-690|Carousel_Mix##__AUTOMATION_"+expID+"","status":"ACTIVE","tracking_specs":{"fb_pixel":"706589963501348"}},"adset":{"name":"aipsm_TEST_FBIN_O:TC_Base:Multi_"+age_min+"to"+age_max+"_FEMALE_MP__AUTOMATION_"+name+"_"+expID+"","status":"ACTIVE","billing_event":"IMPRESSIONS","adset_time_start":AdsetStartTime,"attribution_spec":[{"event_type":"CLICK_THROUGH","window_days":1}],"destination_type":"Website","optimization_goal":"LANDING_PAGE_VIEWS"},"ad_type":"carousel","creative":{"call_to_action_type":"LEARN_MORE","creative_type":"Link Page Post Ad","title":"Primary text","object_type":"SHARE"},"targeting":{"age_max":age_max,"age_min":age_min,"genders":[2],"user_os":"All","placements":"Manual_Placements","device_platforms":["mobile","desktop"],"facebook_positions":["feed"],"publisher_platforms":["facebook"],"targeting_expansion":["expansion_all"],"targeting_optimization":"none","brand_safety_content_filter_levels":["FACEBOOK_STANDARD","AN_STANDARD"]},"story_spec":{"page_id":"107973334116438"},"geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":["android_free_store"],"location_types":["home","recent"]},"excluded_geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home"]},"link_data":{"call_to_action":{"type":"LEARN_MORE"},"caption":"www.hdfc.com","link":"www.pyxispm.com","message":"1","name":"Primary text","multi_share_end_card":'false',"multi_share_optimized":'false'},"mix_products":[{"call_to_action":{"type":"LEARN_MORE"},"link":"www.pyxispm.com","message":"1","image_name":"1615848269338_images.jpg"},{"call_to_action":{"type":"LEARN_MORE"},"link":"www.pyxispm.com","message":"2","image_name":"1615848269699_kirbxcrw69hk1ubqh48g.jpg"},{"call_to_action":{"type":"LEARN_MORE"},"link":"www.pyxispm.com","message":"3","image_name":"1615848269896_Pyxis_Logo_sic7q2.png"},{"call_to_action":{"type":"LEARN_MORE"},"link":"www.pyxispm.com","message":"4","video_name":"1615848278538_gif3_ebnwi2.gif"},{"call_to_action":{"type":"LEARN_MORE"},"link":"www.pyxispm.com","message":"5","video_name":"1615848289463_gif4_ubpyjt.gif"},{"call_to_action":{"type":"LEARN_MORE"},"link":"www.pyxispm.com","message":"6","video_name":"1615848298686_gif8_gpblfh.gif"},{"call_to_action":{"type":"LEARN_MORE"},"link":"www.pyxispm.com","message":"7","video_name":"1615848308684_gif9_kpp03q.gif"},{"call_to_action":{"type":"LEARN_MORE"},"description":"desc","link":"www.pyxispm.com","message":"8","video_name":"1615848338780_1min.mp4"},{"call_to_action":{"type":"LEARN_MORE"},"link":"www.pyxispm.com","message":"9","video_name":"1615848360720_2mins-Copy.mp4"},{"call_to_action":{"type":"LEARN_MORE"},"link":"www.pyxsipm.com","message":"10","video_name":"1615848441970_3min.mp4"}]}]}],"creative_s3_url":"https://s3.console.aws.amazon.com/s3/buckets/fb-adsuploading-files-bucket/dev-upload-form/client-122/creative/","campaignDetails":{"1260":[{"name":"aipsm_TEST_FBIN_O:TC_Base:Multi_*AQ-E:M:T:-TEST-N-BRD--0521-    "+expID+"*_AUTOMATION_"+name+"_"+expID+"","adsets":[{"adset_name":"aipsm_TEST_FBIN_O:TC_Base:Multi_"+age_min+"to"+age_max+"_FEMALE_MP__AUTOMATION_"+name+"_"+expID+"","ads":[{"ad_name":"aipsm_TEST_FBIN_O:TC_Base:Multi_"+age_min+"to"+age_max+"_FEMALE_MP_##AQ-FBIN-TEST-CR-110521-690|Carousel_Mix##__AUTOMATION_"+expID+""}]}]}]}}


# -------------------------------- LEAD GENERATION --------------------------------

# Get JSON body to create experiment setup
def setLeadGenBody(CampaignName, DailyBudget, AdsetStartTime, page):
    payload.setCampaignName(CampaignName)
    payload.setDailyBudget(DailyBudget)
    payload.setAdsetStartTime(AdsetStartTime)
    payload.setPage(page)
    json_body = {"data":{"campaign":{"name":CampaignName,"status":"PAUSED","objective":"Lead Generation","buying_type":"AUCTION","bid_strategy":"Lowest Cost","daily_budget":DailyBudget,"campaign_budget":"DAILY_BUDGET"},"ads_groups":[{"ad":{"status":"ACTIVE"},"adset":{"status":"ACTIVE","billing_event":"IMPRESSIONS","promoted_object":"LEAD_GENERATION","adset_time_start":AdsetStartTime,"attribution_spec":[{"event_type":"CLICK_THROUGH","window_days":1}],"optimization_goal":"LEAD_GENERATION"},"ad_type":"image","creative":{"object_type":"SHARE","Creative Type":"Link Page Post Ad","call_to_action_type":"LEARN_MORE"},"targeting":{"targeting_optimization":"none","brand_safety_content_filter_levels":["FACEBOOK_STANDARD","AN_STANDARD"]},"story_spec":{"page_id":{"page_id":page}},"geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home","recent"]},"excluded_geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home"]}}],"name":CampaignName,"extras":{"ads_groups$geo_locations":[],"ads_groups$excluded_geo_locations":[],"ads_groups$targeting$flexible_spec":[],"ads_groups$targeting$excluded_flexible_spec":[]}}}
    return json_body


# update exp setup
def updateLeadGenBody(age_max,age_min):
    name = payload.getCampaignName()
    DailyBudget = payload.getDailyBudget()
    AdsetStartTime = payload.getAdsetStartTime()
    page = payload.getPage()
    payload.setAgeMax(age_max)
    payload.setAgeMin(age_min)
    updatedJSON = {"data":{"campaign":{"name":name,"status":"PAUSED","objective":"Lead Generation","buying_type":"AUCTION","bid_strategy":"Lowest Cost","daily_budget":DailyBudget,"campaign_budget":"DAILY_BUDGET"},"ads_groups":[{"ad":{"status":"ACTIVE"},"adset":{"name":name,"status":"ACTIVE","billing_event":"IMPRESSIONS","promoted_object":"LEAD_GENERATION","adset_time_start":AdsetStartTime,"attribution_spec":[{"event_type":"CLICK_THROUGH","window_days":1}],"optimization_goal":"LEAD_GENERATION"},"ad_type":"image","creative":{"object_type":"SHARE","Creative Type":"Link Page Post Ad","call_to_action_type":"LEARN_MORE"},"targeting":{"age_max":age_max,"age_min":age_min,"custom_audiences":[{"id":"23847574287240410","name":"Lookalike (IN, 1% to 5%) - Ranit's testing audience","subtype":"LOOKALIKE"},{"id":"23847574322950410","name":"Special Ad Audience (IN, 2%) - Ranit's testing audience","subtype":"REGULATED_CATEGORIES_AUDIENCE"}],"targeting_optimization":"none","excluded_custom_audiences":[{"id":"23847574323680410","name":"Special Ad Audience (IN, 4% to 7%) - Ranit's testing audience","subtype":"REGULATED_CATEGORIES_AUDIENCE"},{"id":"23847574286990410","name":"Lookalike (IN, 1%) - Ranit's testing audience","subtype":"LOOKALIKE"}],"brand_safety_content_filter_levels":["FACEBOOK_STANDARD","AN_STANDARD"]},"story_spec":{"page_id":{"page_id":page}},"geo_locations":{"countries":[],"cities":[{"country":"IN","name":"Varanasi","region":"Uttar Pradesh","key":"1046744"}],"regions":[{"name":"Karnataka","country":"IN","key":"1738"}],"zips":[],"country_groups":[],"location_types":["home","recent"]},"excluded_geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home"]}}],"name":name,"extras":{"ads_groups$geo_locations":[{"key":"1046744","name":"Varanasi","type":"city","country_code":"IN","country_name":"India","region":"Uttar Pradesh","region_id":1754,"supports_region":'true',"supports_city":'true',"responseType":"location","text":"Varanasi, Uttar Pradesh, India city"},{"key":"1738","name":"Karnataka","type":"region","country_code":"IN","country_name":"India","supports_region":'true',"supports_city":'true',"responseType":"location","text":"Karnataka, India region"}],"ads_groups$excluded_geo_locations":[],"ads_groups$targeting$flexible_spec":[],"ads_groups$targeting$excluded_flexible_spec":[]}}}
    return updatedJSON


# Post creative body for leadgen
def getPostCreativeBodyForLeadgen(Type):
    if Type in "Image":
        return {"type":"single image","name":"cr_bmp","files":[{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1617808700111_img-ui-cdgsx.bmp","name":"1617808700111_img-ui-cdgsx.bmp","type":"image/bmp","file_type":"image/bmp","carouselIndex":0}],"form_data":{"lead_gen_form_id":"254429285840340","adType":"single image","creativeName":"cr_bmp","primaryText":"12","displayUrl":"","utmBuilderForDisplayUrl":[],"includedGeoLocations":[],"tracking_specs":{"pixel_id":"706589963501348"},"viewTags":"","cta":"LEARN_MORE","carousel":[{"file":"1617808700111_img-ui-cdgsx.bmp","headline":"123","description":"","websiteUrl":"www.pyxisocial.com","utmBuilderForWebsiteUrl":[],"deepLink":""}]},"creative_json":{"lead_gen_form_id":"254429285840340","adType":"single image","creativeName":"cr_bmp","primaryText":"12","displayUrl":"","utmBuilderForDisplayUrl":[],"includedGeoLocations":{"location_types":["home","recent"],"cities":[],"countries":[],"regions":[],"zips":[],"country_groups":[]},"tracking_specs":{"pixel_id":"706589963501348"},"viewTags":"","cta":"LEARN_MORE","carousel":[{"file":"1617808700111_img-ui-cdgsx.bmp","headline":"123","description":"","websiteUrl":"www.pyxisocial.com","utmBuilderForWebsiteUrl":[],"deepLink":""}]},"approver_email":"","cc_emails":"","approval_status":"draft","comments":"","preview_url":""}
    if Type in "Video":
        return {"type":"single video","name":"Single video","files":[{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1615804150608_Planningaholiday_Compare&saveonFlights&HotelswithPayZapp.HDFCBank,India'sno.1bank_.mp4","name":"1615804150608_Planningaholiday_Compare&saveonFlights&HotelswithPayZapp.HDFCBank,India'sno.1bank_.mp4","type":"video/mp4","file_type":"video/mp4","carouselIndex":0}],"form_data":{"lead_gen_form_id":"1040305483061660","adType":"single video","creativeName":"Single video","primaryText":"prim","displayUrl":"","utmBuilderForDisplayUrl":[],"includedGeoLocations":[],"tracking_specs":{"pixel_id":"706589963501348"},"viewTags":[],"cta":"SUBSCRIBE","carousel":[{"file":"1615804150608_Planningaholiday_Compare&saveonFlights&HotelswithPayZapp.HDFCBank,India'sno.1bank_.mp4","headline":"head","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""}]},"creative_json":{"lead_gen_form_id":"1040305483061660","adType":"single video","creativeName":"Single video","primaryText":"prim","displayUrl":"","utmBuilderForDisplayUrl":[],"includedGeoLocations":{"location_types":["home","recent"],"cities":[],"countries":[],"regions":[],"zips":[],"country_groups":[]},"tracking_specs":{"pixel_id":"706589963501348"},"viewTags":[],"cta":"SUBSCRIBE","carousel":[{"file":"1615804150608_Planningaholiday_Compare&saveonFlights&HotelswithPayZapp.HDFCBank,India'sno.1bank_.mp4","headline":"head","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""}]},"approver_email":"","cc_emails":"","approval_status":"draft","comments":"","preview_url":""}
    if Type in "Carousel":
        return {"type":"carousel","name":"Carousel_Mix","files":[{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1615848269338_images.jpg","name":"1615848269338_images.jpg","type":"image/jpeg","file_type":"image/jpeg","carouselIndex":0},{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1615848269699_kirbxcrw69hk1ubqh48g.jpg","name":"1615848269699_kirbxcrw69hk1ubqh48g.jpg","type":"image/jpeg","file_type":"image/jpeg","carouselIndex":1},{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1615848269896_Pyxis_Logo_sic7q2.png","name":"1615848269896_Pyxis_Logo_sic7q2.png","type":"image/png","file_type":"image/png","carouselIndex":2},{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1615848278538_gif3_ebnwi2.gif","name":"1615848278538_gif3_ebnwi2.gif","type":"image/gif","file_type":"image/gif","carouselIndex":3},{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1615848289463_gif4_ubpyjt.gif","name":"1615848289463_gif4_ubpyjt.gif","type":"image/gif","file_type":"image/gif","carouselIndex":4},{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1615848298686_gif8_gpblfh.gif","name":"1615848298686_gif8_gpblfh.gif","type":"image/gif","file_type":"image/gif","carouselIndex":5},{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1615848308684_gif9_kpp03q.gif","name":"1615848308684_gif9_kpp03q.gif","type":"image/gif","file_type":"image/gif","carouselIndex":6},{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1615848338780_1min.mp4","name":"1615848338780_1min.mp4","type":"video/mp4","file_type":"video/mp4","carouselIndex":7},{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1615848360720_2mins-Copy.mp4","name":"1615848360720_2mins-Copy.mp4","type":"video/mp4","file_type":"video/mp4","carouselIndex":8},{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1615848441970_3min.mp4","name":"1615848441970_3min.mp4","type":"video/mp4","file_type":"video/mp4","carouselIndex":9}],"form_data":{"lead_gen_form_id":"1040305483061660","adType":"carousel","creativeName":"Carousel_Mix","primaryText":"Primary text","displayUrl":"","utmBuilderForDisplayUrl":[],"includedGeoLocations":[],"tracking_specs":{"pixel_id":"706589963501348"},"viewTags":[],"cta":"LEARN_MORE","carousel":[{"file":"1615848269338_images.jpg","headline":"1","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848269699_kirbxcrw69hk1ubqh48g.jpg","headline":"2","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848269896_Pyxis_Logo_sic7q2.png","headline":"3","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848278538_gif3_ebnwi2.gif","headline":"4","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848289463_gif4_ubpyjt.gif","headline":"5","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848298686_gif8_gpblfh.gif","headline":"6","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848308684_gif9_kpp03q.gif","headline":"7","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848338780_1min.mp4","headline":"8","description":"desc","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848360720_2mins-Copy.mp4","headline":"9","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848441970_3min.mp4","headline":"10","description":"","websiteUrl":"www.pyxsipm.com","utmBuilderForWebsiteUrl":[],"deepLink":""}]},"creative_json":{"lead_gen_form_id":"1040305483061660","adType":"carousel","creativeName":"Carousel_Mix","primaryText":"Primary text","displayUrl":"","utmBuilderForDisplayUrl":[],"includedGeoLocations":{"location_types":["home","recent"],"cities":[],"countries":[],"regions":[],"zips":[],"country_groups":[]},"tracking_specs":{"pixel_id":"706589963501348"},"viewTags":[],"cta":"LEARN_MORE","carousel":[{"file":"1615848269338_images.jpg","headline":"1","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848269699_kirbxcrw69hk1ubqh48g.jpg","headline":"2","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848269896_Pyxis_Logo_sic7q2.png","headline":"3","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848278538_gif3_ebnwi2.gif","headline":"4","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848289463_gif4_ubpyjt.gif","headline":"5","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848298686_gif8_gpblfh.gif","headline":"6","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848308684_gif9_kpp03q.gif","headline":"7","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848338780_1min.mp4","headline":"8","description":"desc","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848360720_2mins-Copy.mp4","headline":"9","description":"","websiteUrl":"www.pyxispm.com","utmBuilderForWebsiteUrl":[],"deepLink":""},{"file":"1615848441970_3min.mp4","headline":"10","description":"","websiteUrl":"www.pyxsipm.com","utmBuilderForWebsiteUrl":[],"deepLink":""}]},"approver_email":"","cc_emails":"","approval_status":"draft","comments":"","preview_url":""}



# publish
def getPublishBodyLeadgen(Type):
    name = payload.getCampaignName()
    expID = str(payload.getExperimentSetupID())
    age_max = payload.getAgeMax()
    age_min = payload.getAgeMin()
    daily_budget = getDailyBudget()
    AdsetStartTime = payload.getAdsetStartTime()
    lead = payload.getPage()

    if Type == "Image":
        return {"creative_ids":[1046],"story_id":payload.getStoryID(),"json":[{"campaign":{"name":"aipsm_TEST_FBIN_O:LN_Base:Multi_*"+payload.getStoryID()+"*_AUTOMATION_"+name+"_"+expID+"","status":"PAUSED","objective":"Lead Generation","buying_type":"AUCTION","bid_strategy":"Lowest Cost","daily_budget":daily_budget,"campaign_budget":"DAILY_BUDGET"},"ads_groups":[{"ad":{"name":"aipsm_TEST_FBIN_O:LN_Base:Multi_"+age_min+"to"+age_max+"_ALL_MP_##AQ-FBIN-TEST-SI-270421-476|cr_bmp##__AUTOMATION_"+expID+"","status":"ACTIVE","tracking_specs":{"fb_pixel":"706589963501348"}},"adset":{"name":"aipsm_TEST_FBIN_O:LN_Base:Multi_"+age_min+"to"+age_max+"_ALL_MP__AUTOMATION_"+name+"_"+expID+"","status":"ACTIVE","billing_event":"IMPRESSIONS","promoted_object":"LEAD_GENERATION","adset_time_start":AdsetStartTime,"attribution_spec":[{"event_type":"CLICK_THROUGH","window_days":1}],"optimization_goal":"LEAD_GENERATION"},"ad_type":"image","creative":{"creative_type":"Link Page Post Ad","object_type":"SHARE"},"targeting":{"age_max":age_max,"age_min":age_min,"custom_audiences":[{"id":"23847574287240410","name":"Lookalike (IN, 1% to 5%) - Ranit's testing audience","subtype":"LOOKALIKE"},{"id":"23847574322950410","name":"Special Ad Audience (IN, 2%) - Ranit's testing audience","subtype":"REGULATED_CATEGORIES_AUDIENCE"}],"targeting_optimization":"none","excluded_custom_audiences":[{"id":"23847574323680410","name":"Special Ad Audience (IN, 4% to 7%) - Ranit's testing audience","subtype":"REGULATED_CATEGORIES_AUDIENCE"},{"id":"23847574286990410","name":"Lookalike (IN, 1%) - Ranit's testing audience","subtype":"LOOKALIKE"}],"brand_safety_content_filter_levels":["FACEBOOK_STANDARD","AN_STANDARD"]},"story_spec":{"page_id":"245069182739198"},"geo_locations":{"countries":[],"cities":[{"country":"IN","name":"Varanasi","region":"Uttar Pradesh","key":"1046744"}],"regions":[{"name":"Karnataka","country":"IN","key":"1738"}],"zips":[],"country_groups":[],"location_types":["home","recent"]},"excluded_geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home"]},"photo_data_spec":{"call_to_action":{"type":"LEARN_MORE","value":{"lead_gen_form_id":"254429285840340"}},"image_name":"1617808700111_img-ui-cdgsx.bmp","link":"https://fb.me/","message":"123","name":"12"}}]}],"creative_s3_url":"https://s3.console.aws.amazon.com/s3/buckets/fb-adsuploading-files-bucket/dev-upload-form/client-122/creative/","campaignDetails":{"1046":[{"name":"aipsm_TEST_FBIN_O:LN_Base:Multi_*"+payload.getStoryID()+"*_AUTOMATION_"+name+"_"+expID+"","adsets":[{"adset_name":"aipsm_TEST_FBIN_O:LN_Base:Multi_"+age_min+"to"+age_max+"_ALL_MP__AUTOMATION_"+name+"_"+expID+"","ads":[{"ad_name":"aipsm_TEST_FBIN_O:LN_Base:Multi_"+age_min+"to"+age_max+"_ALL_MP_##AQ-FBIN-TEST-SI-270421-476|cr_bmp##__AUTOMATION_"+expID+""}]}]}]}}
    if Type == "Video":
        return {"creative_ids":[1244],"story_id":payload.getStoryID(),"json":[{"campaign":{"name":"aipsm_TEST_FBIN_O:LN_Base:Multi_*"+payload.getStoryID()+"*_AUTOMATION_"+name+"_"+expID+"","status":"PAUSED","objective":"Lead Generation","buying_type":"AUCTION","bid_strategy":"Lowest Cost","daily_budget":daily_budget,"campaign_budget":"DAILY_BUDGET"},"ads_groups":[{"ad":{"name":"aipsm_TEST_FBIN_O:LN_Base:Multi_"+age_min+"to"+age_max+"_ALL_MP_##AQ-FBIN-TEST-GV-070521-674|Singlevideo##__AUTOMATION_"+expID+"","status":"ACTIVE","tracking_specs":{"fb_pixel":"706589963501348"}},"adset":{"name":"aipsm_TEST_FBIN_O:LN_Base:Multi_"+age_min+"to"+age_max+"_ALL_MP__AUTOMATION_"+name+"_"+expID+"","status":"ACTIVE","billing_event":"IMPRESSIONS","promoted_object":{"page_id":"105092258056322"},"adset_time_start":AdsetStartTime,"attribution_spec":[{"event_type":"CLICK_THROUGH","window_days":1}],"optimization_goal":"LEAD_GENERATION"},"ad_type":"video","creative":{"object_type":"VIDEO","creative_type":"Video Page Post Ad","status":"ACTIVE"},"targeting":{"age_max":age_max,"age_min":age_min,"custom_audiences":[{"id":"23847574287240410","name":"Lookalike (IN, 1% to 5%) - Ranit's testing audience","subtype":"LOOKALIKE"},{"id":"23847574322950410","name":"Special Ad Audience (IN, 2%) - Ranit's testing audience","subtype":"REGULATED_CATEGORIES_AUDIENCE"}],"targeting_optimization":"none","excluded_custom_audiences":[{"id":"23847574323680410","name":"Special Ad Audience (IN, 4% to 7%) - Ranit's testing audience","subtype":"REGULATED_CATEGORIES_AUDIENCE"},{"id":"23847574286990410","name":"Lookalike (IN, 1%) - Ranit's testing audience","subtype":"LOOKALIKE"}],"brand_safety_content_filter_levels":["FACEBOOK_STANDARD","AN_STANDARD"]},"story_spec":{"page_id":"461441901347474","instagram_actor_id":"2685713601466369"},"geo_locations":{"countries":[],"cities":[{"country":"IN","name":"Varanasi","region":"Uttar Pradesh","key":"1046744"}],"regions":[{"name":"Karnataka","country":"IN","key":"1738"}],"zips":[],"country_groups":[],"location_types":["home","recent"]},"excluded_geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home"]},"video_data_spec":{"call_to_action":{"type":"SUBSCRIBE","value":{"link":"https://fb.me/","link_format":"VIDEO_LPP","lead_gen_form_id":"1040305483061660"}},"message":"head","name":"prim","video_name":"1615804150608_Planningaholiday_Compare&saveonFlights&HotelswithPayZapp.HDFCBank,India'sno.1bank_.mp4"}}]}],"creative_s3_url":"https://s3.console.aws.amazon.com/s3/buckets/fb-adsuploading-files-bucket/dev-upload-form/client-122/creative/","campaignDetails":{"1244":[{"name":"aipsm_TEST_FBIN_O:LN_Base:Multi_*"+getStoryID()+"*_AUTOMATION_"+name+"_"+expID+"","adsets":[{"adset_name":"aipsm_TEST_FBIN_O:LN_Base:Multi_"+age_min+"to"+age_max+"_ALL_MP__AUTOMATION_"+name+"_"+expID+"","ads":[{"ad_name":"aipsm_TEST_FBIN_O:LN_Base:Multi_"+age_min+"to"+age_max+"_ALL_MP_##AQ-FBIN-TEST-GV-070521-674|Singlevideo##__"+name+"_"+expID+""}]}]}]}}
    if Type == "Carousel":
        return {"creative_ids":[1249],"story_id":payload.getStoryID(),"json":[{"campaign":{"name":"aipsm_TEST_FBIN_O:LN_Base:Multi_*"+payload.getStoryID()+"*_AUTOMATION_"+name+"_"+expID+"","status":"PAUSED","objective":"Lead Generation","buying_type":"AUCTION","bid_strategy":"Lowest Cost","daily_budget":daily_budget,"campaign_budget":"DAILY_BUDGET"},"ads_groups":[{"ad":{"name":"aipsm_TEST_FBIN_O:LN_Base:Multi_"+age_min+"to"+age_max+"_ALL_MP_##AQ-FBIN-TEST-CR-070521-679|Carousel_Mix##__AUTOMATION_"+expID+"","status":"ACTIVE","tracking_specs":{"fb_pixel":"706589963501348"}},"adset":{"name":"aipsm_TEST_FBIN_O:LN_Base:Multi_"+age_min+"to"+age_max+"_ALL_MP__AUTOMATION_"+name+"_"+expID+"","status":"ACTIVE","billing_event":"IMPRESSIONS","promoted_object":{"page_id":"105092258056322"},"adset_time_start":AdsetStartTime,"attribution_spec":[{"event_type":"CLICK_THROUGH","window_days":1}],"optimization_goal":"LEAD_GENERATION"},"ad_type":"carousel","creative":{"call_to_action_type":"LEARN_MORE","creative_type":"Link Page Post Ad","title":"Primary text","object_type":"SHARE","instagram_actor_id":"2685713601466369"},"targeting":{"age_max":age_max,"age_min":age_min,"custom_audiences":[{"id":"23847574287240410","name":"Lookalike (IN, 1% to 5%) - Ranit's testing audience","subtype":"LOOKALIKE"},{"id":"23847574322950410","name":"Special Ad Audience (IN, 2%) - Ranit's testing audience","subtype":"REGULATED_CATEGORIES_AUDIENCE"}],"targeting_optimization":"none","excluded_custom_audiences":[{"id":"23847574323680410","name":"Special Ad Audience (IN, 4% to 7%) - Ranit's testing audience","subtype":"REGULATED_CATEGORIES_AUDIENCE"},{"id":"23847574286990410","name":"Lookalike (IN, 1%) - Ranit's testing audience","subtype":"LOOKALIKE"}],"brand_safety_content_filter_levels":["FACEBOOK_STANDARD","AN_STANDARD"]},"story_spec":{"page_id":"461441901347474","instagram_actor_id":"2685713601466369"},"geo_locations":{"countries":[],"cities":[{"country":"IN","name":"Varanasi","region":"Uttar Pradesh","key":"1046744"}],"regions":[{"name":"Karnataka","country":"IN","key":"1738"}],"zips":[],"country_groups":[],"location_types":["home","recent"]},"excluded_geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home"]},"link_data":{"call_to_action":{"type":"LEARN_MORE","value":{"lead_gen_form_id":"1040305483061660"}},"link":"https://fb.me/","message":"1","name":"Primary text","multi_share_end_card":'false',"multi_share_optimized":'false'},"mix_products":[{"call_to_action":{"type":"LEARN_MORE","value":{"lead_gen_form_id":"1040305483061660"}},"link":"https://fb.me/","message":"1","image_name":"1615848269338_images.jpg"},{"call_to_action":{"type":"LEARN_MORE","value":{"lead_gen_form_id":"1040305483061660"}},"link":"https://fb.me/","message":"2","image_name":"1615848269699_kirbxcrw69hk1ubqh48g.jpg"},{"call_to_action":{"type":"LEARN_MORE","value":{"lead_gen_form_id":"1040305483061660"}},"link":"https://fb.me/","message":"3","image_name":"1615848269896_Pyxis_Logo_sic7q2.png"},{"call_to_action":{"type":"LEARN_MORE","value":{"lead_gen_form_id":"1040305483061660"}},"link":"https://fb.me/","message":"4","video_name":"1615848278538_gif3_ebnwi2.gif"},{"call_to_action":{"type":"LEARN_MORE","value":{"lead_gen_form_id":"1040305483061660"}},"link":"https://fb.me/","message":"5","video_name":"1615848289463_gif4_ubpyjt.gif"},{"call_to_action":{"type":"LEARN_MORE","value":{"lead_gen_form_id":"1040305483061660"}},"link":"https://fb.me/","message":"6","video_name":"1615848298686_gif8_gpblfh.gif"},{"call_to_action":{"type":"LEARN_MORE","value":{"lead_gen_form_id":"1040305483061660"}},"link":"https://fb.me/","message":"7","video_name":"1615848308684_gif9_kpp03q.gif"},{"call_to_action":{"type":"LEARN_MORE","value":{"lead_gen_form_id":"1040305483061660"}},"description":"desc","link":"https://fb.me/","message":"8","video_name":"1615848338780_1min.mp4"},{"call_to_action":{"type":"LEARN_MORE","value":{"lead_gen_form_id":"1040305483061660"}},"link":"https://fb.me/","message":"9","video_name":"1615848360720_2mins-Copy.mp4"},{"call_to_action":{"type":"LEARN_MORE","value":{"lead_gen_form_id":"1040305483061660"}},"link":"https://fb.me/","message":"10","video_name":"1615848441970_3min.mp4"}]}]}],"creative_s3_url":"https://s3.console.aws.amazon.com/s3/buckets/fb-adsuploading-files-bucket/dev-upload-form/client-122/creative/","campaignDetails":{"1249":[{"name":"aipsm_TEST_FBIN_O:LN_Base:Multi_*"+payload.getStoryID()+"*_AUTOMATION_"+name+"_"+expID+"","adsets":[{"adset_name":"aipsm_TEST_FBIN_O:LN_Base:Multi_"+age_min+"to"+age_max+"_ALL_MP__AUTOMATION_"+name+"_"+expID+"","ads":[{"ad_name":"aipsm_TEST_FBIN_O:LN_Base:Multi_"+age_min+"to"+age_max+"_ALL_MP_##AQ-FBIN-TEST-CR-070521-679|Carousel_Mix##__AUTOMATION_1315"}]}]}]}}


# -------------------------------- CONVERSION --------------------------------


# Get JSON body to create experiment setup
def setConversionBody(CampaignName, DailyBudget, AdsetStartTime, page):
    payload.setCampaignName(CampaignName)
    payload.setDailyBudget(DailyBudget)
    payload.setAdsetStartTime(AdsetStartTime)
    payload.setPage(page)
    json_body = {"data":{"campaign":{"name":CampaignName,"status":"PAUSED","objective":"Conversions","buying_type":"AUCTION","bid_strategy":"Lowest Cost","daily_budget":DailyBudget,"campaign_budget":"DAILY_BUDGET"},"ads_groups":[{"ad":{"status":"ACTIVE"},"adset":{"status":"ACTIVE","billing_event":"IMPRESSIONS","promoted_object":{"pixel_id":"706589963501348"},"adset_time_start":AdsetStartTime,"attribution_spec":[{"event_type":"CLICK_THROUGH","window_days":7},{"event_type":"VIEW_THROUGH","window_days":1}],"destination_type":"Website","optimization_goal":"OFFSITE_CONVERSIONS"},"ad_type":"image","creative":{"object_type":"SHARE","Creative Type":"Link Page Post Ad","call_to_action_type":"LEARN_MORE"},"targeting":{"targeting_optimization":"none","brand_safety_content_filter_levels":["FACEBOOK_STANDARD","AN_STANDARD"]},"story_spec":{"page_id":{"page_id":page}},"geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home","recent"]},"excluded_geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home"]}}],"name":"convers","extras":{"ads_groups$geo_locations":[],"ads_groups$excluded_geo_locations":[],"ads_groups$targeting$flexible_spec":[],"ads_groups$targeting$excluded_flexible_spec":[]}}}
    return json_body


# update exp setup
def updateConversionBody(age_max,age_min):
    name = payload.getCampaignName()
    DailyBudget = payload.getDailyBudget()
    AdsetStartTime = payload.getAdsetStartTime()
    page = payload.getPage()
    payload.setAgeMax(age_max)
    payload.setAgeMin(age_min)
    updatedJSON = {"data":{"campaign":{"name":name,"status":"PAUSED","objective":"Conversions","buying_type":"AUCTION","bid_strategy":"Lowest Cost","daily_budget":DailyBudget,"campaign_budget":"DAILY_BUDGET"},"ads_groups":[{"ad":{"status":"ACTIVE"},"adset":{"name":"Conversion","status":"ACTIVE","billing_event":"IMPRESSIONS","promoted_object":{"pixel_id":"380740899476965"},"adset_time_start":AdsetStartTime,"attribution_spec":[{"event_type":"CLICK_THROUGH","window_days":1},{"event_type":"VIEW_THROUGH","window_days":1}],"destination_type":"Website","optimization_goal":"OFFSITE_CONVERSIONS","promoted_object_event":{"value":"2488721811438238","custom_event_type":"LEAD","pixel_rule":"{\"and\":[{\"event\":{\"eq\":\"PageView\"}},{\"or\":[{\"URL\":{\"i_contains\":\"confirm\"}}]}]}"}},"ad_type":"image","creative":{"object_type":"SHARE","Creative Type":"Link Page Post Ad","instagram_actor_id":"2685713601466369","call_to_action_type":"LEARN_MORE"},"targeting":{"age_max":age_max,"age_min":age_min,"locales":[{"key":75,"name":"Kannada","responseType":"locale"},{"key":46,"name":"Hindi","responseType":"locale"}],"flexible_spec":[{"behaviors":[{"id":"6013017211983","name":"Owns: Galaxy S III Mini"}]}],"custom_audiences":[{"id":"23847574323660410","name":"Special Ad Audience (IN, 2% to 4%) - Ranit's testing audience","subtype":"REGULATED_CATEGORIES_AUDIENCE"}],"targeting_expansion":["expansion_all"],"excluded_flexible_spec":[{"interests":[{"id":"6003383562925","name":"X2 (film)"}]}],"targeting_optimization":"none","excluded_custom_audiences":[{"id":"23847574322950410","name":"Special Ad Audience (IN, 2%) - Ranit's testing audience","subtype":"REGULATED_CATEGORIES_AUDIENCE"}],"brand_safety_content_filter_levels":["FACEBOOK_STANDARD","AN_STANDARD"]},"story_spec":{"page_id":{"page_id":page},"instagram_actor_id":"2685713601466369"},"geo_locations":{"countries":[],"cities":[{"country":"IN","name":"Ahmedabad","region":"Gujarat","key":"1015741"}],"regions":[],"zips":[],"country_groups":[],"location_types":["home","recent"]},"excluded_geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home"]}}],"name":"Conversion","extras":{"ads_groups$geo_locations":[{"key":"1015741","name":"Ahmedabad","text":"Ahmedabad, Gujarat, India city","type":"city","region":"Gujarat","region_id":1729,"country_code":"IN","country_name":"India","responseType":"location","supports_city":"true","supports_region":"true"}],"ads_groups$excluded_geo_locations":[],"ads_groups$targeting$flexible_spec":[{"id":"6013017211983","name":"Owns: Galaxy S III Mini","path":["Behaviours","Mobile Device User","All Mobile Devices by Brand","Samsung","Owns: Galaxy S III Mini"],"text":"Owns: Galaxy S III Mini : behaviors","type":"behaviors","description":"People who are likely to own a Galaxy S III Mini mobile device","responseType":"interest","audience_size":477453}],"ads_groups$targeting$excluded_flexible_spec":[{"id":"6003383562925","name":"X2 (film)","path":["Interests","Additional interests","X2 (film)"],"text":"X2 (film) : interests","type":"interests","responseType":"interest","audience_size":60470030}]}}}
    return updatedJSON



# Post creative body for traffic
def getPostCreativeBodyForConversion():
    return {"type":"single video","name":"Single video","files":[{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1615804150608_Planningaholiday_Compare&saveonFlights&HotelswithPayZapp.HDFCBank,India'sno.1bank_.mp4","name":"1615804150608_Planningaholiday_Compare&saveonFlights&HotelswithPayZapp.HDFCBank,India'sno.1bank_.mp4","type":"video/mp4","file_type":"video/mp4","carouselIndex":0}],"form_data":{"lead_gen_form_id":"","adType":"single video","creativeName":"Single video","primaryText":"prim","displayUrl":"","utmBuilderForDisplayUrl":[],"includedGeoLocations":[],"tracking_specs":{"pixel_id":"706589963501348"},"viewTags":[],"cta":"CONTACT_US","carousel":[{"file":"1615804150608_Planningaholiday_Compare&saveonFlights&HotelswithPayZapp.HDFCBank,India'sno.1bank_.mp4","headline":"head","description":"","websiteUrl":"www.pyxispm.com","deepLink":"","utmBuilderForWebsiteUrl":[]}]},"creative_json":{"lead_gen_form_id":"","adType":"single video","creativeName":"Single video","primaryText":"prim","displayUrl":"","utmBuilderForDisplayUrl":[],"includedGeoLocations":{"location_types":["home","recent"],"cities":[],"countries":[],"regions":[],"zips":[],"country_groups":[]},"tracking_specs":{"pixel_id":"706589963501348"},"viewTags":[],"cta":"CONTACT_US","carousel":[{"file":"1615804150608_Planningaholiday_Compare&saveonFlights&HotelswithPayZapp.HDFCBank,India'sno.1bank_.mp4","headline":"head","description":"","websiteUrl":"www.pyxispm.com","deepLink":"","utmBuilderForWebsiteUrl":[]}]},"approver_email":"","cc_emails":"","approval_status":"draft","comments":"","preview_url":""}


def getPublishBodyConversion():
    name = payload.getCampaignName()
    expID = str(payload.getExperimentSetupID())
    age_max = payload.getAgeMax()
    age_min = payload.getAgeMin()
    daily_budget = getDailyBudget()
    return {"creative_ids":[1140],"story_id":payload.getStoryID(),"json":[{"campaign":{"name":"aipsm_TEST_FBIN_O:CN_Base:Multi_*AQ-E:M:T:-TEST-C-BRD--0521-    "+expID+"*_AUTOMATION_"+name+"_"+expID+"","status":"PAUSED","objective":"Conversions","buying_type":"AUCTION","bid_strategy":"Lowest Cost","daily_budget":daily_budget,"campaign_budget":"DAILY_BUDGET"},"ads_groups":[{"ad":{"name":"aipsm_TEST_FBIN_O:CN_Base:Multi_33to44_ALL_MP_##AQ-FBIN-TEST-GV-040521-570|Singlevideo##__DEFAULT_04May21_1200","status":"ACTIVE","tracking_specs":{"fb_pixel":"706589963501348"}},"adset":{"name":"aipsm_TEST_FBIN_O:CN_Base:Multi_33to44_ALL_MP__AUTOMATION_"+name+"_"+expID+"","status":"ACTIVE","billing_event":"IMPRESSIONS","promoted_object":{"pixel_id":"380740899476965","value":"420589942262410","custom_event_type":"OTHER","pixel_rule":"{\"and\":[{\"event\":{\"eq\":\"PageView\"}},{\"or\":[{\"URL\":{\"i_contains\":\"tommy\"}}]}]}"},"adset_time_start":AdsetStartTime,"attribution_spec":[{"event_type":"CLICK_THROUGH","window_days":1},{"event_type":"VIEW_THROUGH","window_days":1}],"destination_type":"Website","optimization_goal":"OFFSITE_CONVERSIONS","promoted_object_event":{"value":"420589942262410","custom_event_type":"OTHER","pixel_rule":"{\"and\":[{\"event\":{\"eq\":\"PageView\"}},{\"or\":[{\"URL\":{\"i_contains\":\"tommy\"}}]}]}"}},"ad_type":"video","creative":{"object_type":"VIDEO","creative_type":"Video Page Post Ad","status":"ACTIVE"},"targeting":{"age_max":age_max,"age_min":age_min,"locales":[{"name":"Kannada","key":75,"responseType":"locale"},{"name":"Hindi","key":46,"responseType":"locale"}],"flexible_spec":[{"behaviors":[{"id":"6013017211983","name":"Owns: Galaxy S III Mini"}]}],"custom_audiences":[{"id":"23847574323660410","name":"Special Ad Audience (IN, 2% to 4%) - Ranit's testing audience","subtype":"REGULATED_CATEGORIES_AUDIENCE"}],"targeting_expansion":["expansion_all"],"excluded_flexible_spec":{"interests":[{"id":"6003383562925","name":"X2 (film)"}]},"targeting_optimization":"none","excluded_custom_audiences":[{"id":"23847574322950410","name":"Special Ad Audience (IN, 2%) - Ranit's testing audience","subtype":"REGULATED_CATEGORIES_AUDIENCE"}],"brand_safety_content_filter_levels":["FACEBOOK_STANDARD","AN_STANDARD"]},"story_spec":{"page_id":"107973334116438"},"geo_locations":{"countries":[],"cities":[{"country":"IN","name":"Ahmedabad","region":"Gujarat","key":"1015741"}],"regions":[],"zips":[],"country_groups":[],"location_types":["home","recent"]},"excluded_geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home"]},"video_data_spec":{"call_to_action":{"type":"CONTACT_US","value":{"link":"www.pyxispm.com","link_format":"VIDEO_LPP"}},"message":"head","name":"prim","video_name":"1615804150608_Planningaholiday_Compare&saveonFlights&HotelswithPayZapp.HDFCBank,India'sno.1bank_.mp4"}}]}],"creative_s3_url":"https://s3.console.aws.amazon.com/s3/buckets/fb-adsuploading-files-bucket/dev-upload-form/client-122/creative/","campaignDetails":{"1140":[{"name":"aipsm_TEST_FBIN_O:CN_Base:Multi_*AQ-E:M:T:-TEST-C-BRD--0521-    "+expID+"*_AUTOMATION_"+name+"_"+expID+"","adsets":[{"adset_name":"aipsm_TEST_FBIN_O:CN_Base:Multi_33to44_ALL_MP__AUTOMATION_"+name+"_"+expID+"","ads":[{"ad_name":"aipsm_TEST_FBIN_O:CN_Base:Multi_"+age_min+"to"+age_max+"_ALL_MP_##AQ-FBIN-TEST-GV-040521-570|Singlevideo##__AUTOMATION_"+expID+""}]}]}]}}


# -------------------------------- APP INSTALL --------------------------------

# Get JSON body to create experiment setup
def setAppInstallBody(CampaignName, DailyBudget, AdsetStartTime, page):
    payload.setCampaignName(CampaignName)
    payload.setDailyBudget(DailyBudget)
    payload.setAdsetStartTime(AdsetStartTime)
    payload.setPage(page)
    json_body = {"data":{"campaign":{"name":CampaignName,"status":"PAUSED","objective":"App Installs","buying_type":"AUCTION","bid_strategy":"Lowest Cost","daily_budget":DailyBudget,"campaign_budget":"DAILY_BUDGET"},"ads_groups":[{"ad":{"status":"ACTIVE"},"adset":{"status":"ACTIVE","billing_event":"IMPRESSIONS","promoted_object":{"application_id":"1006500503177359"},"adset_time_start":AdsetStartTime,"optimization_goal":"LINK_CLICKS","destination_type_forAppInstalls":"http://www.facebook.com/instantgames/play/1006500503177359/"},"ad_type":"image","creative":{"object_type":"SHARE","Creative Type":"Link Page Post Ad","call_to_action_type":"LEARN_MORE"},"targeting":{"targeting_optimization":"none","brand_safety_content_filter_levels":["FACEBOOK_STANDARD","AN_STANDARD"]},"story_spec":{"page_id":{"page_id":page}},"geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home","recent"]},"excluded_geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home"]}}],"name":CampaignName,"extras":{"ads_groups$geo_locations":[],"ads_groups$excluded_geo_locations":[],"ads_groups$targeting$flexible_spec":[],"ads_groups$targeting$excluded_flexible_spec":[]}}}
    return json_body



# update exp setup
def updateAppInstallBody(age_max,age_min):
    name = payload.getCampaignName()
    DailyBudget = payload.getDailyBudget()
    AdsetStartTime = payload.getAdsetStartTime()
    page = payload.getPage()
    payload.setAgeMax(age_max)
    payload.setAgeMin(age_min)
    updatedJSON = {"data":{"campaign":{"name":name,"status":"PAUSED","objective":"App Installs","buying_type":"AUCTION","bid_strategy":"Lowest Cost","daily_budget":DailyBudget,"campaign_budget":"DAILY_BUDGET"},"ads_groups":[{"ad":{"status":"ACTIVE"},"adset":{"name":name,"status":"ACTIVE","billing_event":"IMPRESSIONS","promoted_object":{"application_id":"1006500503177359"},"adset_time_start":AdsetStartTime,"optimization_goal":"LINK_CLICKS","destination_type_forAppInstalls":"http://www.facebook.com/instantgames/play/1006500503177359/"},"ad_type":"image","creative":{"object_type":"SHARE","Creative Type":"Link Page Post Ad","call_to_action_type":"LEARN_MORE"},"targeting":{"age_max":age_max,"age_min":age_min,"targeting_optimization":"none","brand_safety_content_filter_levels":["FACEBOOK_STANDARD","AN_STANDARD"]},"story_spec":{"page_id":{"page_id":page}},"geo_locations":{"countries":[],"cities":[{"country":"ID","name":"Bandung","region":"West Java","key":"949797"}],"regions":[],"zips":[],"country_groups":[],"location_types":["home","recent"]},"excluded_geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home"]}}],"name":name,"extras":{"ads_groups$geo_locations":[{"key":"949797","name":"Bandung","type":"city","country_code":"ID","country_name":"Indonesia","region":"West Java","region_id":1685,"supports_region":'true',"supports_city":'true',"responseType":"location","text":"Bandung, West Java, Indonesia city"}],"ads_groups$excluded_geo_locations":[],"ads_groups$targeting$flexible_spec":[],"ads_groups$targeting$excluded_flexible_spec":[]}}}
    return updatedJSON


def getPostCreativeBodyForAppinstall():
        return {"type":"single image","name":"aditi test creative","files":[{"url":"https://fb-adsuploading-files-bucket.s3.ap-south-1.amazonaws.com/dev-upload-form/client-122/creative/1617271274703_Pyxis.png","name":"1617271274703_Pyxis.png","type":"image/png","file_type":"image/png","carouselIndex":0}],"form_data":{"lead_gen_form_id":"254429285840340","adType":"single image","creativeName":"aditi test creative","primaryText":"ads","displayUrl":"","utmBuilderForDisplayUrl":[],"includedGeoLocations":[],"tracking_specs":"","viewTags":"","cta":"LEARN_MORE","carousel":[{"file":"1617271274703_Pyxis.png","headline":"asd","description":"ad","websiteUrl":"https://fb.me/","utmBuilderForWebsiteUrl":[],"deepLink":""}]},"creative_json":{"lead_gen_form_id":"254429285840340","adType":"single image","creativeName":"aditi test creative","primaryText":"ads","displayUrl":"","utmBuilderForDisplayUrl":[],"includedGeoLocations":{"location_types":["home","recent"],"cities":[],"countries":[],"regions":[],"zips":[],"country_groups":[]},"tracking_specs":"","viewTags":"","cta":"LEARN_MORE","carousel":[{"file":"1617271274703_Pyxis.png","headline":"asd","description":"ad","websiteUrl":"https://fb.me/","utmBuilderForWebsiteUrl":[],"deepLink":""}]},"approver_email":"","cc_emails":"","approval_status":"draft","comments":"","preview_url":""}


# publish
def getPublishBodyAppInstall():
    name = payload.getCampaignName()
    expID = str(payload.getExperimentSetupID())
    age_max = payload.getAgeMax()
    age_min = payload.getAgeMin()
    daily_budget = getDailyBudget()
    page = payload.getPage()
    return {"creative_ids":[1159],"story_id":payload.getStoryID(),"json":[{"campaign":{"name":"aipsm_TEST_FBIN_O:AS_Base:Multi_*AQ-E:M:T:-TEST-N-BRD--0521-    "+expID+"*_AUTOMATION_"+name+"_"+expID+"","status":"PAUSED","objective":"App Installs","buying_type":"AUCTION","bid_strategy":"Lowest Cost","daily_budget":DailyBudget,"campaign_budget":"DAILY_BUDGET"},"ads_groups":[{"ad":{"name":"aipsm_TEST_FBIN_O:AS_Base:Multi_"+age_min+"to"+age_max+"_ALL_MP_##AQ-FBIN-TEST-SI-050521-589|adititestcreative##__DEFAULT_05May21_"+expID+"","status":"ACTIVE"},"adset":{"name":"aipsm_TEST_FBIN_O:AS_Base:Multi_"+age_min+"to"+age_max+"_ALL_MP__AUTOMATION_"+name+"_"+expID+"","status":"ACTIVE","billing_event":"IMPRESSIONS","promoted_object":{"application_id":"1006500503177359","object_store_url":"http://www.facebook.com/instantgames/play/1006500503177359/"},"adset_time_start":AdsetStartTime,"optimization_goal":"LINK_CLICKS","destination_type_forAppInstalls":"http://www.facebook.com/instantgames/play/1006500503177359/","attribution_spec":[]},"ad_type":"image","creative":{"creative_type":"Link Page Post Ad","object_type":"SHARE"},"targeting":{"age_max":age_max,"age_min":age_min,"targeting_optimization":"none","brand_safety_content_filter_levels":["FACEBOOK_STANDARD","AN_STANDARD"]},"story_spec":{"page_id":page},"geo_locations":{"countries":[],"cities":[{"country":"ID","name":"Bandung","region":"West Java","key":"949797"}],"regions":[],"zips":[],"country_groups":[],"location_types":["home","recent"]},"excluded_geo_locations":{"countries":[],"cities":[],"regions":[],"zips":[],"country_groups":[],"location_types":["home"]},"photo_data_spec":{"call_to_action":{"type":"LEARN_MORE"},"description":"ad","image_name":"1617271274703_Pyxis.png","link":"http://www.facebook.com/instantgames/play/1006500503177359/","message":"asd","name":"ads"}}]}],"creative_s3_url":"https://s3.console.aws.amazon.com/s3/buckets/fb-adsuploading-files-bucket/dev-upload-form/client-122/creative/","campaignDetails":{"1159":[{"name":"aipsm_TEST_FBIN_O:AS_Base:Multi_*AQ-E:M:T:-TEST-N-BRD--0521-    1223*_AUTOMATION_"+name+"_"+expID+"","adsets":[{"adset_name":"aipsm_TEST_FBIN_O:AS_Base:Multi_22to33_ALL_MP__AUTOMATION_"+name+"_"+expID+"","ads":[{"ad_name":"aipsm_TEST_FBIN_O:AS_Base:Multi_22to33_ALL_MP_##AQ-FBIN-TEST-SI-050521-589|adititestcreative##__DEFAULT_05May21_1223"}]}]}]}}

# -------------------------------- GETTERS AND SETTERS --------------------------------

def setCampaignName(CampaignName):
    payload.CampaignName = CampaignName

def getCampaignName():
    return payload.CampaignName


def setDailyBudget(DailyBudget):
    payload.DailyBudget = DailyBudget

def getDailyBudget():
    return payload.DailyBudget

def setAdsetStartTime(AdsetStartTime):
    payload.AdsetStartTime = AdsetStartTime

def getAdsetStartTime():
    return payload.AdsetStartTime

def setPage(page):
    payload.page = page

def getPage():
    return payload.page

def setAgeMax(age):
    payload.age_max = age

def getAgeMax():
    return payload.age_max

def setAgeMin(age):
    payload.age_min = age

def getAgeMin():
    return payload.age_min

def setCreativeType(type):
    payload.type = type

def getCreativeType():
    return payload.type

# -------------------------------- LEAD GEN MEDIA PLAN --------------------------------

def setClientData(client_json):
    payload.client_json = client_json


def getClientData():
    return payload.client_json


def saveAdaccountsList(adaccounts):
    payload.adaccounts = adaccounts


def getAdaccountsList():
    return payload.adaccounts


def saveMetricData(MetricData):
    payload.MetricData = MetricData

def getMetricData():
    return payload.MetricData

def saveCampaignIDs(Breakdown):
    payload.Breakdown = Breakdown

def getCampaignIDs():
    return payload.Breakdown

