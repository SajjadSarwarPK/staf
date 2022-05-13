Feature: Verify users list endpoint
  As a SDET
  I want to verify the users endpoint
  So that it is working as expected

  @api
  Scenario: api_sample_scenario_api
    When user hit the following url to perform get operation
      | url                                |
      | https://reqres.in/api/users?page=2 |
    Then user should get an OK response
    And I should see the following information
      | keyword |
      | George  |
      | Howell  |
      | email   |


  Scenario: ui_based_test_scenarios_ui
    When user hit the following url to load in the ui
      | url                |
      | https://google.com |
    Then user should see the following keywords on the page
      | keyword    |
      | Google     |
      | offered in |
    And close the browser