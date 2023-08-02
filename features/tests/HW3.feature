# Created by ktknu at 8/1/2023
Feature: #Test Amazon features

  Scenario: HW problem 2 - verify that logged out user sees Sign In when clicking on Returns and Orders.
    Given Open new Amazon page
    When Click Returns & Orders
    Then Verify user is brought to Sign In page


  Scenario: HW problem 3 - verify that 'Your Amazon Cart is empty' message shows when clicking the cart.
     Given Open new Amazon page
     When Click on cart icon
     Then Verify 'Your Amazon Cart is empty' message displays


  Scenario: Creative HW problem - verify that a user can add an item to the cart
     Given Open new Amazon page
     Then Search for an item
     When Add item to cart
     Then Verify the item displays in the cart