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