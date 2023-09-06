# Created by ktknu at 9/2/2023
Feature: # Enter feature name here
  # Enter feature description here


  Scenario: Verify Best Sellers UI
    Given Open Amazon BestSellers page
    Then Verify 5 links display

  Scenario: Verify Best Sellers menu items opens correctly
    Given Open Amazon BestSellers page
    Then User can click through menu links
