import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions

from element import Element
from logger import Logger
from test_blocked_exception import TestBlockedException

class Driver():

    def __init__(self):
        Logger.log_info("Initialising driver")
        self.driver = webdriver.Chrome('/Users/davide/chromedriver')

    def load_url(self, url):
        Logger.log_info("Loading URL: " + url)
        self.driver.get(url)

    def get_element(self, element, blocker=False):
        try:
            return Element(self.driver.find_element_by_id(element), element)
        except NoSuchElementException:
            if blocker:
                Logger.log_blocked("Could not find element: #" + element)
                raise TestBlockedException("Important element not found: #" + element)
            else:
                Logger.log_fail("Cloud not find element: #" + element)

    def close(self):
        self.driver.close()

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_element(self, element_id):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID, element_id)))

    def wait(self, seconds):
        Logger.log_info("Waiting for " + str(seconds) + " seconds")
        time.sleep(seconds)
        # Logger.log_info("Waiting for " + str(seconds) + " seconds")
        # self.driver.implicitly_wait(seconds * 10)
