Feature: Listing assets
  In order for users to be aware of the assets in the registry
  As a user
  I want to be able to see all the assets in the registry

  Scenario: Default scenario
    Given there is an asset in the registry
    When the user requests the assets
    Then the assets should be returned to the user
