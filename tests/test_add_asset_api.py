import unittest, requests, os, json

from data_provider import DataProvider


ENDPOINT = "http://52.56.141.168/api/asset/add"


class TestAddAssetAPI(unittest.TestCase):

    '''
    Valid asset information should obviously be accepted
    '''
    def test_valid_fields(self):
        payload = DataProvider.get_payload("POST_asset_add.valid_payload.0.json")
        response = requests.post(ENDPOINT, data=payload)

        # assert response.status_code is 200
        self.assertEqual(200, response.status_code)
        try:
            self.assertNotEqual(None, response.json()["asset_id"])
        except KeyError:
            self.fail("Asset ID not returned")

    '''
    Submission should succeed if skip the optional fields
    '''
    def test_mandatory_fields(self):
        for i in range(0, 3):
            payload = DataProvider.get_payload("POST_asset_add.mandatory_fields." + str(i) + ".json")
            response = requests.post(ENDPOINT, data=payload)

            self.assertEqual(200, response.status_code)
            try:
                self.assertNotEqual(None, response.json()["asset_id"])
            except KeyError:
                self.fail("Asset ID not returned")

    '''
    Submission should fail if any of the mandatory fields are missing
    '''
    def test_missing_data(self):
        for i in range(0, 6):
            payload = DataProvider.get_payload("POST_asset_add.missing_mandatory." + str(i) + ".json")
            response = requests.post(ENDPOINT, data=payload)

            self.assertEqual(400, response.status_code)
            try:
                asset_id = response.json()["asset_id"]
            except KeyError:
                pass

    '''
    Ensuring that strings, integers and lists are what they are supposed to be
    '''
    def test_invalid_formatting(self):
        for i in range(0, 5):
            payload = DataProvider.get_payload("POST_asset_add.invalid_format." + str(i) + ".json")
            response = requests.post(ENDPOINT, data=payload)

            self.assertEqual(400, response.status_code)
            try:
                asset_id = response.json()["asset_id"]
            except KeyError:
                pass

if __name__ == '__main__':
    unittest.main()
