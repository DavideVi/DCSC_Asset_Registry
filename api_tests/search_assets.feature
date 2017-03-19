Feature: As a user
  I want to search for assets
  So that I can find assets to use

  Background: some assets must have been added
    Given assets and their tags are present in the database

  Scenario: Multiple exact tags
    Given a set of tags that match the all the tags of a target asset
    When we search for tags
    Then the target asset should be the first result

  Scenario: Partial match
    Given a set of tags that match an asset more than all the others
    When we search for tags
    Then the target asset should be the first result

  Scenario: No match
    Given a set of tags that does not match any of the tags of a target asset
    When we search for tags
    Then the target asset should not be in the search results
