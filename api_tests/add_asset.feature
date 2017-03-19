Feature: Add an asset
  In order to have assets
  As a user
  I want to be able to add an asset

  Scenario: Valid request
    Given we have valid information regarding an asset
    When we request to add an asset
    Then the request should succeed

  Scenario: Missing data
    Given we have asset information that is missing mandatory data
    When we request to add an asset
    Then the request should return Bad Request
