from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from element import Element
from logger import Logger
from test_blocked_exception import TestBlockedException

class Driver():

    def __init__(self):
        self.driver = webdriver.Chrome('/Users/davide/chromedriver')

    def load_url(self, url):
        self.driver.get(url)

    def get_element(self, element, blocker=False):
        try:
            return Element(self.driver.find_element_by_id(element))
        except NoSuchElementException:
            if blocker:
                Logger.log_blocked("Could not find element: #" + element)
                raise TestBlockedException("Important element not found: #" + element)
            else:
                Logger.log_fail("Cloud not find element: #" + element)

    def close():
        self.driver.close()
