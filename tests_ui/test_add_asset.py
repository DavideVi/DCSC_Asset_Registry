import unittest

from selenium import webdriver

# Pages
from pages.menu import MenuBar
from pages.add_asset_page import AddAssetPage
from pages.asset_page import AssetPage

ENDPOINT = "http://52.56.141.168/"

class TestAddAsset(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS('/Users/davide/phantomjs-2.1.1-macosx/bin/phantomjs')
        self.driver.get(ENDPOINT + "add")

    def test_valid_asset(self):
        AddAssetPage.complete_form(self.driver, "asset_form.valid_asset.json")
        AddAssetPage.submit_form(self.driver)

        assert "/asset/" in self.driver.current_url

    def test_all_fields_missing(self):
        pass

    def test_mandatory_fields_empty(self):
        AddAssetPage.complete_form(self.driver, "asset_form.missing_mandatory.json")
        AddAssetPage.submit_form(self.driver)

        # Submision should not be successful
        assert "/add" in self.driver.current_url


    def test_only_mandatory_fields(self):
        pass

    def test_invalid_formatting(self):
        pass

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
