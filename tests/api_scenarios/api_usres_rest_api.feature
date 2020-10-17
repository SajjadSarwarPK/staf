# Created by user at 10/17/2020
Feature: Verify users list endpoint
  As a SDET
  I want to verify the users endpoint
  So that it is working as expected

  Scenario: get_all_users
    When user hit the "Get_All_Users" configuration to access api
    Then user should get an OK response
    And user should see "Miss Abhaidev"