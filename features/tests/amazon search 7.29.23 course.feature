# Created by ktknu at 7/29/2023
Feature: Test for Amazon search

  Scenario: Verify that a user can search for a table
    Given Open Amazon page
    When Search for table
    Then Verify search result is correct