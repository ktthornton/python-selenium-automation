# Created by ktknu at 8/14/2023
Feature: HW5 scenarios

  Scenario: Make a test case with a loop
    Given Open Amazon product B07W45LYY8 page
    Then Verify user can click through colors


 Scenario: Verify search results have a product name and image
    Given Open new Amazon page
    When Search for coffee
    Then Verify results have a product name and image