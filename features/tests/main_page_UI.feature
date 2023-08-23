# Created by ktknu at 8/5/2023
Feature: Test for Main page UI
  # Enter feature description here

  Scenario: Verify that footer has correct amount of links
    Given Open Amazon page
    Then Verify footer has 36 links


  Scenario: Verify that footer has many links
    Given Open Amazon page
    Then Verify many links are shown in the footer


  Scenario: HW problem 2 - verify that logged out user sees Sign In when clicking on Returns and Orders.
    Given Open Amazon page
    When Click Returns & Orders
    Then Verify user is brought to Sign In page


  Scenario: HW problem 3 - verify that 'Your Amazon Cart is empty' message shows when clicking the cart.
     Given Open Amazon page
     When Click on cart icon
     Then Verify 'Your Amazon Cart is empty' message displays


  Scenario: Creative HW problem - verify that a user can add an item to the cart
     Given Open Amazon page
     Then Search for an item
     When Add item to cart
     Then Verify the item displays in the cart


  Scenario: HW problem 1 - Verify Best Sellers UI
    Given Open Amazon BestSellers page
    Then Verify 5 links display


  Scenario: HW problem 3 - Verify Customer Service UI
    Given Open Amazon Customer Service page
    Then Verify UI elements
