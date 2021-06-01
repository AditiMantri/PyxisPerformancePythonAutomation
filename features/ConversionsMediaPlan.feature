Feature: LeadGen end to end API for Media Plan

  @leadGenMediaPlan
  Scenario Outline: Step1 - Login
    Given the URL and the login credentials <login> and <password>
      When the Login postAPI is executed
      And the user should be logged in successfully
      Then I should receive a valid HTTP response code 200
      And validate error is False
      Then extract token and save it
      Examples:
          |login            |password|
          |test@aiquire.com |123456  |


  @leadGenMediaPlan
  Scenario Outline: Step 2 - Get client, client ID, Story name and story id under each client
    Given the Authorization
    When the Clients GetAPI is executed
    And error should be false
    Then extract the GetAPI response and store it
    And verify if the <ClientName> is linked to the logged in user
    Then store the client ID <ClientName>
      Examples:
        |ClientName|
        |Brandtrack|


    @leadGenMediaPlan
    Scenario: Step 3 - Get adaccounts data with logged in user
    Given the token, client id and adaccounts endpoint
    When adaccount GetAPI is executed
    And the error response from adaccount is false
    Then store the adaccounts response


    @leadGenMediaPlan
    Scenario Outline: Step 4 - Get mpadaccounts data with logged in user
    Given the token, client id and mpadaccounts endpoint
    When mpadaccount GetAPI is executed
    And the error response from mpadaccount is false
    Then store the id of <adaccountName> if adaccount name is present in the adaccount list
    Examples:
      |adaccountName|
      |DBS AIQ - OC BM2|


    @leadGenMediaPlan
    Scenario: Step 5 - Get the status of past data
      Given the token, adaccount id and getStatus endpoint
      When Status GetAPI is executed
      And the error response from status is false
      Then verify that the sync_status is DONE
      And last_30d_available and first_30d_available are both true


    @leadGenMediaPlan
    Scenario: Step 6 - Get Metric data
      Given the adaccount id, date preset, objective, optimization goal and getMetricData endpoint
      When Metric getAPI is executed
      And the error response from Metric is false
      Then store the metrics data


    @leadGenMediaPlan
    Scenario: Step 7 : Get Campaign IDs
      Given the adaccount id, date preset, objective and getCampaignIDs endpoint
      When getCampaignIDs getAPI is executed
      And the error response from the getCampaignIDs is false
      Then store all the campaign ids


    @leadGenMediaPlan
    Scenario: Step 8 : Get Age breakdown
      Given the adaccount id, date preset, age breakdown, campaign IDs and the AgeBreakdown endpoint
      When the AgeBreakdown getAPI is executed
      And the error response from the getAgeBreakdown is false
      Then verify that the initial data from getAgeBreakdown is blank


    @leadGenMediaPlan
    Scenario: Step 9 : Get Gender breakdown
      Given the adaccount id, date preset, Gender breakdown, campaign IDs and the GenderBreakdown endpoint
      When the GenderBreakdown getAPI is executed
      And the error response from the getGenderBreakdown is false
      Then verify that the initial data from getGenderBreakdown is blank


    @leadGenMediaPlan
    Scenario: Step 10 : Get Publisher Platform breakdown
      Given the adaccount id, date preset, PublisherPlatform breakdown, campaign IDs and the PublisherPlatform endpoint
      When the PublisherPlatform getAPI is executed
      And the error response from the getPublisherPlatform is false
      Then verify that the initial data from getPublisherPlatform is blank


    @leadGenMediaPlan
    Scenario: Step 11 : Get Device Platform breakdown
      Given the adaccount id, date preset, DevicePlatform breakdown, campaign IDs and the DevicePlatform endpoint
      When the DevicePlatform getAPI is executed
      And the error response from the getDevicePlatform is false
      Then verify that the initial data from getDevicePlatform is blank


    @leadGenMediaPlan
    Scenario: Step 12 : Get Region breakdown
      Given the adaccount id, date preset, Region breakdown, campaign IDs and the Region endpoint
      When the Region getAPI is executed
      And the error response from the getRegion is false
      Then verify that the initial data from getRegion is blank


    @leadGenMediaPlan
    Scenario: Step 13 : Generate Media plan
      Given the adaccount id, json and media plan end point
      When the generateMediaPlan postAPI is executed
      And the error response from the postgenerateMediaPlan is false
      Then verify that success is true


#    @leadGenMediaPlan
#    Scenario: Step 14 : Get Media Plan ID
#      Given the client id, objective and get media plan endpoint
#      When the getMediaPlan getAPI is executed
#      And the error response from the getMediaPlan is false
#      Then compare the media plan created date, other details and save the media plan id
#
#
#    @leadGenMediaPlan
#    Scenario: Step 15 : Fetch Media Plan Details
#      Given the media plan ID and the media plan endpoint
#      When the fetchMediaPlan getAPI is executed
#      And the error response from the fetchMediaPlan is false
#      Then get the details of the media plan created

