# Created by ktknu at 7/29/2023
Feature: Test for Amazon search

  Scenario: Verify that a user can search for a table
    Given Open Amazon page
    When Search for table
    Then Verify search result is "table"


#  Scenario: Verify that a user can search for a cup
#    Given Open Amazon page
#    When Search for cup
#    Then Verify search result is "cup"
#
#
#  Scenario: Verify that a user can search for a dress
#    Given Open Amazon page
#    When Search for dress
#    Then Verify search result is "dress"

  Scenario Outline: Verify that a user can search for a product
    Given Open Amazon page
    When Search for <search_word>
    Then Verify search result is <search_result>
    Examples:
    |search_word    |search_result  |
    |cup            |"cup"          |
    |dress          |"dress"        |
    |coffee         |"coffee"       |



  Scenario: Verify search results have a product name and image
    Given Open Amazon page
    When Search for coffee
    Then Verify results have a product name and image


  Scenario: Verify that a user can add an item to the cart
     Given Open Amazon page
     When Search for coffee
     When Add item to cart
     Then Verify added to cart message displays: Added to Cart
     Then Verify 1 item displays in the cart


  Scenario Outline: User can select and search by department
    Given Open Amazon page
    When Select department by alias <dept_alias>
    And Search for <search_word>
    Then Verify <selected_dept> department is selected
    Examples:
    |dept_alias |search_word  |selected_dept  |
    |stripbooks  |Faust  |books               |
    |audible     |non-fiction |audible        |
    |digital-music  |chris stapleton  |dmusic |
