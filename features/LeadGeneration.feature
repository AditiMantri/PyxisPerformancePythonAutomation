# Author : Aditi Mantri

  Feature: Lead Generation end to end API

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

    Scenario Outline: Step 2 - Get clients associated with the logged in user
      Given the Authorization
      When the Clients GetAPI is executed
      And error should be false
      Then store the client ID <ClientName>
        Examples:
          | ClientName |
          |TestClient  |


    Scenario Outline: Step 3 - Get mpadaccounts data with logged in user
      Given the token, client id and mpadaccounts endpoint
      When mpadaccount GetAPI is executed
      And the error response from mpadaccount is false
      Then store the id if adaccount name is <adaccountName>
      Examples:
        |adaccountName|
        |Test Account|


    Scenario: Step 4 - Get Campaign Setup Form Config
      Given the token and getCampaignSetupFormConfig endpoint
      When getCampaignSetupFormConfig GetAPI is executed
      And the error response from getCampaignSetupFormConfig is false
      Then save the config file


    Scenario: Step 5 - Get pages
      Given the token, client id, adaccount id and pages endpoint
      When Pages GetAPI is executed
      And the error response from getPages is false
      Then capture page ids when accessible is true


    Scenario: Step 6 - Get Adaccounts
      Given the token, client id, adaccount id and adaccounts endpoint
      When adaccount GetAPI is executed
      And the error response from getAdaccounts is false
      Then capture adaccount ids when accessible is true


    Scenario: Step 7 : Get Custom Audience
      Given the token, client id, adaccount id and CustomAudience endpoint
      When CustomAudience GetAPI is executed
      And the error response from CustomAudience is false
      Then capture custom audience id


    Scenario: Step 8 : Post experiment setup campaign details
      Given the token, client account id, ad account id and createExperimentSetup endpoint
      When the json body is sent
      And createExperimentSetup postAPI is executed
      Then verify if the error response is false
      And status of the experiment setup is Created
      Then capture the Experiment Setup id
