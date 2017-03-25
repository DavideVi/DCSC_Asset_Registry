from data_provider import DataProvider

class AddAssetPage():

    @staticmethod
    def complete_form(driver, data_file):

        AddAssetPage.clear_form(driver)

        data = DataProvider.get_data(data_file)

        driver.find_element_by_id("asset-name").send_keys(data["asset-name"])
        driver.find_element_by_id("asset-purpose").send_keys(data["asset-purpose"])
        driver.find_element_by_id("author-ids").send_keys(data["author-ids"])
        driver.find_element_by_id("technologies").send_keys(data["technologies"])
        driver.find_element_by_id("scm-link").send_keys(data["scm-link"])
        driver.find_element_by_id("wiki-link").send_keys(data["wiki-link"])

    @staticmethod
    def set_text_fields(driver, value):
        driver.find_element_by_id("asset-name").clear()
        driver.find_element_by_id("asset-name").send_keys(value)
        driver.find_element_by_id("asset-purpose").clear()
        driver.find_element_by_id("asset-purpose").send_keys(value)

    @staticmethod
    def set_list_fields(driver, value):
        driver.find_element_by_id("author-ids").clear()
        driver.find_element_by_id("author-ids").send_keys(value)
        driver.find_element_by_id("technologies").clear()
        driver.find_element_by_id("technologies").send_keys(value)

    @staticmethod
    def set_url_fields(driver, value):
        driver.find_element_by_id("scm-link").clear()
        driver.find_element_by_id("scm-link").send_keys(value)
        driver.find_element_by_id("wiki-link").clear()
        driver.find_element_by_id("wiki-link").send_keys(value)

    @staticmethod
    def submit_form(driver):
        driver.find_element_by_id("btn-submit").click()

    @staticmethod
    def clear_form(driver):
        driver.find_element_by_id("asset-name").clear()
        driver.find_element_by_id("asset-purpose").clear()
        driver.find_element_by_id("author-ids").clear()
        driver.find_element_by_id("technologies").clear()
        driver.find_element_by_id("scm-link").clear()
        driver.find_element_by_id("wiki-link").clear()

    @staticmethod
    def get_validation_message(driver):
        return driver.find_element_by_id("validation-message").text

    @staticmethod
    def is_validation_message_displayed(driver):
        return driver.find_element_by_id("validation-message").is_displayed()
