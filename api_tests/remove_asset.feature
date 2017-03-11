Feature: Remove an asset
  In order to keep the registry clean
  As a user
  I want to be able to delete assets I have added

  Scenario: Default scenario
    Given the user has an asset added to the registry
    When the user deletes the asset
    Then the asset should no longer be in the registry

  Scenario: Deleting someone else's assets as a non-admin
    Given there is an asset in the registry
    And the asset does not belong to the user
    When the user deletes the asset
    Then the asset will still be in the registry
