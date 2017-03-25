# Framework
from framework.driver import Driver
from framework.test_blocked_exception import TestBlockedException
from framework.logger import Logger

# Pages
from pages.menu import MenuBar
from pages.add_asset_page import AddAssetPage
from pages.asset_page import AssetPage

ENDPOINT = "http://52.56.141.168/"

def run_test_case(test_case):
    Logger.log_head(test_case)
    try:
        # New driver
        driver = Driver()
        driver.load_url(ENDPOINT + "add")
        test_case(driver)

    except TestBlockedException:
        Logger.log_blocked("Test has been blocked. Cannot continue")

    finally:
        driver.close()

def tc_valid_asset(driver):
    AddAssetPage.complete_form(driver, "asset_form.valid_asset.json")
    AddAssetPage.submit_form(driver)

def tc_all_fields_missing(driver):
    pass

def tc_mandatory_fields_empty(driver):
    AddAssetPage.complete_form(driver, "asset_form.missing_mandatory.json")
    AddAssetPage.submit_form(driver)
    pass

def tc_only_mandatory_fields(driver):
    pass

def tc_invalid_formatting(driver):
    pass

run_test_case(tc_valid_asset)
run_test_case(tc_mandatory_fields_empty)
