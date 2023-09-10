# Created by ktknu at 8/5/2023
Feature: Test for Main page UI
  # Enter feature description here

  Scenario: Verify that footer has correct amount of links
    Given Open Amazon page
    Then Verify footer has 36 links


  Scenario: Verify that footer has many links
    Given Open Amazon page
    Then Verify many links are shown in the footer


  Scenario: Verify that 'Your Amazon Cart is empty' message shows when clicking the cart.
     Given Open Amazon page
     When Click on cart icon
     Then Verify empty cart message displays: Your Amazon Cart is empty



  Scenario: Verify Customer Service UI
    Given Open Amazon Customer Service page
    Then Verify UI elements


  Scenario: Verify language hover option
    Given Open Amazon page
    When Hover over language options
    Then Verify Spanish option present