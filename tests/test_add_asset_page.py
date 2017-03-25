import unittest, os

from selenium import webdriver
from data_provider import DataProvider

# Pages
from pages.menu import MenuBar
from pages.add_asset_page import AddAssetPage
from pages.asset_page import AssetPage

AR_ENDPOINT = os.environ['AR_ENDPOINT']
ENDPOINT = AR_ENDPOINT + "/add"

class TestAddAssetPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.get(ENDPOINT)

    '''
    Valid asset information should obviously be accepted
    '''
    def test_valid_asset(self):
        AddAssetPage.complete_form(self.driver, "asset_form.valid_asset.0.json")
        AddAssetPage.submit_form(self.driver)

        # Submision should be successful
        assert "/asset/" in self.driver.current_url

    '''
    Submission should succeed if skip the optional fields
    '''
    def test_only_mandatory_fields(self):
        AddAssetPage.complete_form(self.driver, "asset_form.mandatory_fields_only.0.json")
        AddAssetPage.submit_form(self.driver)

        # Submision should be successful
        assert "/asset/" in self.driver.current_url

    '''
    Submission should fail if any of the mandatory fields are missing
    '''
    def test_mandatory_fields_empty(self):

        for i in range(0,5):

            AddAssetPage.complete_form(self.driver, "asset_form.missing_mandatory." + str(i) + ".json")
            AddAssetPage.submit_form(self.driver)

            # Submision should not be successful
            assert "/add" in self.driver.current_url
            # Validation alert should be visible
            assert AddAssetPage.is_validation_message_displayed(self.driver)
            # Validation message should state that fields are empty
            assert "Field is empty" in AddAssetPage.get_validation_message(self.driver)

    '''
    Some values that make no sense/break the system should not be allowed
    '''
    def test_invalid_formatting(self):

        invalid_values = DataProvider.get_data("generic.invalid_values.json")

        for value in invalid_values["text-fields"]:
            AddAssetPage.complete_form(self.driver, "asset_form.valid_asset.0.json")
            AddAssetPage.set_text_fields(self.driver, value)

            # Submision should not be successful
            assert "/add" in self.driver.current_url
            # Validation alert should be visible
            assert AddAssetPage.is_validation_message_displayed(self.driver)

        for value in invalid_values["non-http-urls"]:
            AddAssetPage.complete_form(self.driver, "asset_form.valid_asset.0.json")
            AddAssetPage.set_url_fields(self.driver, value)

            # Submision should not be successful
            assert "/add" in self.driver.current_url
            # Validation alert should be visible
            assert AddAssetPage.is_validation_message_displayed(self.driver)

        for value in invalid_values["lists"]:
            AddAssetPage.complete_form(self.driver, "asset_form.valid_asset.0.json")
            AddAssetPage.set_list_fields(self.driver, value)

            # Submision should not be successful
            assert "/add" in self.driver.current_url
            # Validation alert should be visible
            assert AddAssetPage.is_validation_message_displayed(self.driver)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
