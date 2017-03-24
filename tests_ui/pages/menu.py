
class MenuBar():

    @staticmethod
    def click_logo(driver):
        #logo
        pass

    @staticmethod
    def click_homepage(driver):
        #homepage-menu-btn
        pass

    @staticmethod
    def click_browse(driver):
        #browse-menu-btn
        pass

    @staticmethod
    def click_feedback(driver):
        # driver.get_element("feedback-btn")
        pass

    @staticmethod
    def click_add_asset(driver):
        elm = driver.get_element("add-asset-btn")
        elm.click()
