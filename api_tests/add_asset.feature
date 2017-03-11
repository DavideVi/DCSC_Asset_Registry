Feature: Add an asset
  In order to have assets
  As a user
  I want to be able to add an asset

  Scenario: Default scenario
    Given we have valid information regarding the asset
    When we request to add an asset
    Then the request should succeed
