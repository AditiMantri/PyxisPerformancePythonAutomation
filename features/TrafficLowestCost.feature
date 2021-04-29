 Feature: Lead Generation end to end API with lowest cost


   @smoke @traffic
   Scenario Outline: Step 8 - Post experiment setup campaign details
      Given the token, client account id, ad account id and createExperimentSetup endpoint
      When the json body is sent with <CampaignName>, <DailyBudget>, <AdsetStartTime> for Traffic
      And create ExperimentSetup postAPI is executed
      Then verify if the error response is false
      And status of the experiment setup is Created
      Then capture the Experiment Setup id
        Examples:
          |CampaignName|DailyBudget|AdsetStartTime           |
          |Traffic     |100        |2021-06-27T20:16:59+05:30|