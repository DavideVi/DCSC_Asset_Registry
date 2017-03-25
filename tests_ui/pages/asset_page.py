from framework.test_blocked_exception import TestBlockedException
from framework.logger import Logger

class AssetPage():

    @staticmethod
    def wait_until_load(driver):
        counter = 0
        while "/asset/" not in driver.get_current_url() and counter < 10:
            driver.wait(1)
            counter += 1

        if "/asset/" not in driver.get_current_url() and counter >= 10:
            Logger.log_blocked("Page load failed, URL still is: " + driver.get_current_url())
            raise TestBlockedException("Page has not been loaded: " + driver.get_current_url())
