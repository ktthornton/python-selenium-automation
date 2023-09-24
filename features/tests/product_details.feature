# Created by ktknu at 8/28/2023
Feature: Tests for product page
  # Enter feature description here

  Scenario: User can select colors
    Given Open Amazon product B07W45LYY8 page
    Then Verify user can click through colors

  @smoke
  Scenario: User can view New Arrivals
    Given Open Amazon product B074TBCSC8 page
    When Hover over New Arrivals menu item
    Then Verify New Arrivals menu is present