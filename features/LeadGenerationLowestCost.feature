# Author : Aditi Mantri

  Feature: Lead Generation end to end API with lowest cost


    @smoke @leadgen @traffic
    Scenario Outline: Step 1 - Login
      Given the URL and the login credentials <login> and <password>
      When the Login postAPI is executed
      And the user should be logged in successfully
      Then I should receive a valid HTTP response code 200
      And validate error is False
      Then extract token and save it
        Examples:
          |login            |password|
          |test@aiquire.com |123456  |
 #         |aditi.mantri@pyxispm.com|123456|


    @smoke @leadgen @traffic
    Scenario Outline: Step 2 - Get clients associated with the logged in user
      Given the Authorization
      When the Clients GetAPI is executed
      And error should be false
      Then store the client ID <ClientName>
        Examples:
          | ClientName |
          |TestClient  |


    @smoke @leadgen @traffic
    Scenario Outline: Step 3 - Get mpadaccounts data with logged in user
      Given the token, client id and mpadaccounts endpoint
      When mpadaccount GetAPI is executed
      And the error response from mpadaccount is false
      Then store the id if adaccount name is <adaccountName>
      Examples:
        |adaccountName|
        |Test Account|


    @smoke @leadgen @traffic
    Scenario: Step 4 - Get Campaign Setup Form Config
      Given the token and getCampaignSetupFormConfig endpoint
      When getCampaignSetupFormConfig GetAPI is executed
      And the error response from getCampaignSetupFormConfig is false
      Then save the config file


    @smoke @leadgen @traffic
    Scenario: Step 5 - Get pages
      Given the token, client id, adaccount id and pages endpoint
      When Pages GetAPI is executed
      And the error response from getPages is false
      Then capture page ids when accessible is true


    @smoke @leadgen @traffic
    Scenario: Step 6 - Get Adaccounts
      Given the token, client id, adaccount id and adaccounts endpoint
      When adaccount GetAPI is executed
      And the error response from getAdaccounts is false
      Then capture adaccount ids when accessible is true


    @smoke @leadgen @traffic
    Scenario: Step 7 - Get Custom Audience
      Given the token, client id, adaccount id and CustomAudience endpoint
      When CustomAudience GetAPI is executed
      And the error response from CustomAudience is false
      Then capture custom audience id


    @smoke @leadgen
    Scenario Outline: Step 8 - Post experiment setup campaign details
      Given the token, client account id, ad account id and createExperimentSetup endpoint
      When the json body is sent with <CampaignName>, <DailyBudget>, <AdsetStartTime> for Leadgen
      And create ExperimentSetup postAPI is executed
      Then verify if the error response is false
      And status of the experiment setup is Created
      Then capture the Experiment Setup id
        Examples:
          |CampaignName|DailyBudget|AdsetStartTime           |
          |Demo        |100        |2021-07-27T20:16:59+05:30|


    @smoke @leadgen
    Scenario: Step 9 - Get experiment setup
      Given the token, experiment setup ID and the getExperimentSetup endpoint
      When getExperimentSetup getAPI is executed
      And the error response from getExperimentSetup is false
      Then save the getExperimentSetup response


    @smoke @leadgen
    Scenario Outline: Step 10 - Update experiment setup
      Given the token,experiment setup ID and the updateExperimentSetup endpoint
      When updateExperimentSetup putAPI is executed with maxAge=<maxAge> and minAge=<minAge>
      And the error response from updateExperimentSetup is false
      Then verify the status of the experiment setup is Updated
        Examples:
          |maxAge|minAge|
          |44    |33    |


    @smoke @leadgen
    Scenario: Step 11 - Get creative
      Given the client id, ad account id, experiment setup id and the getCreative endpoint
      When getCreative getAPI is executed
      And the error response from getCreative is false
      Then verify that the data body is empty


    @smoke @leadgen
    Scenario: Step 12 - Get creative files
      Given the client id and the getCreativeFiles endpoint
      When getCreativeFiles getAPI is executed
      And the error response from getCreativeFiles is false
      Then store the response that we get from getCreativeFiles


    @smoke @leadgen
    Scenario: Step 13 - Get creative template files
      Given the client id and the getCreativeTemplate endpoint
      When getCreativeTemplate getAPI is executed
      And the error response from getCreativeTemplate is false
      Then store the response that we get from getCreativeTemplate


    @smoke @leadgen
    Scenario: Step 14 - Get Pixel ID
      Given the client id and the getPixel endpoint
      When getPixel getAPI is executed
      And the error response from getPixel is false
      Then store the pixel id if accessible is true


    @smoke @leadgen
    Scenario: Step 15 - Post the creative
      Given the client id, ad account id, experiment setup id and the postCreative endpoint
      When postCreative postAPI is executed
      And the error response from postCreative is false
      Then save the creative ID


    @smoke @leadgen
    Scenario: Step 16 - Get the creative
      Given the client id, ad account id, experiment setup id and the getCreative endpoint
      When getCreative getAPI is executed
      And the error response from getCreative is false
      Then store the json response from getCreative


    @smoke @leadgen
    Scenario: Step 17 - Get storyname
      Given the experiment setup id and the storyname endpoint
      When getStoryName getAPI is executed
      And the error response from getStoryName is false
      Then save the story id


    @smoke @leadgen
    Scenario: Step 18 - Publish request
      Given client id, ad account id, experiment setup id and publish endpoint
      When publish postAPI is executed
      And the error response from publish is false and status is requested
      Then save the publish request id


    @smoke @leadgen
    Scenario: Step 19 - Verify the status of the task on middleware
      Given experiment setup id and the endpoint
      When getAPI is executed
      And error status is 200
      Then verify the status is SUCCESS