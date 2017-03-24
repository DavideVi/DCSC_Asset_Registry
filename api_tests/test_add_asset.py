from helper import make_request, assert_eq, assert_neq, out_header, get_key

ENDPOINT = "http://52.56.141.168/api"
ASSET_ADD = ENDPOINT + "/asset/add"

'''
Feature: Add an asset
  In order to have assets
  As a user
  I want to be able to add an asset
'''

# ==============================================================================

out_header("All fields valid")

# Given we have valid information regarding an asset
# When we request to add an asset
response = make_request(ASSET_ADD, "POST_asset_add.valid_payload.0.json")

if response is not None:
    # Then the request should succeed
    assert_eq(response.status_code, 200, "Response code is 200")
    # and return asset ID
    assert_neq(get_key(response,"asset_id"), None, "Asset ID is returned")
    # and the asset should appear in the database
    assert_eq(True, False, "Asset should appear in database (Not Implemented)")

# ==============================================================================

out_header("Only mandatory fields")

for i in range(0, 3):
    # Given we have only the necessary asset information
    # When we request to add an asset
    response = make_request(ASSET_ADD, "POST_asset_add.mandatory_fields." + str(i) + ".json")

    if response is not None:
        # Then the request should succeed
        assert_eq(response.status_code, 200, "Response code is 200")
        # and return asset ID
        assert_neq(get_key(response,"asset_id"), None, "Asset ID is returned")
        # and the asset should appear in the database
        assert_eq(True, False, "Asset should appear in database (Not Implemented)")

# ==============================================================================

out_header("Missing data")

for i in range(0, 6):
    # Given we have asset information that is missing mandatory data
    # When we request to add an asset
    response = make_request(ASSET_ADD, "POST_asset_add.missing_mandatory." + str(i) + ".json")

    if response is not None:
        # Then the request should return Bad Request
        assert_eq(response.status_code, 400, "Response code is 400")
