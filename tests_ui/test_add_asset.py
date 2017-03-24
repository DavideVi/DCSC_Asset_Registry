from framework.driver import Driver

from page.menu import MenuBar

ENDPOINT = "http://52.56.141.168/"


driver = Driver()
driver.load_url(ENDPOINT)
# elm = driver.get_element("test")

MenuBar.click_add_asset(driver)
