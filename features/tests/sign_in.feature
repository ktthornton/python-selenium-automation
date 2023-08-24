# Created by ktknu at 8/13/2023
Feature: Sign In page tests

  Scenario: Sign in page can be opened from Sign In popup
    Given Open Amazon page
    When Click on button from Sign In popup
    Then Verify user is brought to Sign In page


  Scenario: Verify that logged out user sees Sign In when clicking on Returns and Orders.
    Given Open Amazon page
    When Click Returns & Orders
    Then Verify user is brought to Sign In page