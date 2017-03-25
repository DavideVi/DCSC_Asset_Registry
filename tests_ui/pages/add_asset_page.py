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
