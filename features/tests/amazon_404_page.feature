# Created by ktknu at 9/2/2023
Feature: Tests for 404 page
  # Enter feature description here

  Scenario: verify 404 page
    Given Open Amazon product B87NF5WGQ11111111 page
    And Store original window
    When Click dog image
    And Switch to new window
    Then Verify blog is opened
    And Close blog
    And Return to original window