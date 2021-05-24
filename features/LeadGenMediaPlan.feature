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
        |TestClient|


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
      |Test Account|


    @leadGenMediaPlan
    Scenario: Step 5 - Get the status of past data
      Given the token, adaccount id and getStatus endpoint
      When Status GetAPI is executed
      And the error response from status is false
      Then verify that the sync_status is DONE
      And last_30d_available and first_30d_available are both true