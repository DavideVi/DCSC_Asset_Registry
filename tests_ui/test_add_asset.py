# Framework
from framework.driver import Driver
from framework.test_blocked_exception import TestBlockedException
from framework.logger import Logger

# Pages
from pages.menu import MenuBar
from pages.add_asset import AddAssetPage

ENDPOINT = "http://52.56.141.168/"

# Actual test journey
try:
    driver = Driver()

    # We go to the homepage
    driver.load_url(ENDPOINT)

    # We click on the 'Add asset button'
    MenuBar.click_add_asset(driver)

    # We complete the form
    AddAssetPage.complete_form(driver, "asset_form.valid_asset.json")

    # We submit the form
    AddAssetPage.submit_form(driver)

    # We should end up on the asset page

    driver.close()

except TestBlockedException:
    Logger.log_blocked("Test has been blocked. Cannot continue")
