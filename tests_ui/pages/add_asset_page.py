from framework.data_provider import DataProvider

class AddAssetPage():

    @staticmethod
    def complete_form(driver, data_file):

        AddAssetPage.clear_form(driver)

        data = DataProvider.get_data(data_file)

        driver.get_element("asset-name").send_keys(data["asset-name"])
        driver.get_element("asset-purpose").send_keys(data["asset-purpose"])
        driver.get_element("author-ids").send_keys(data["author-ids"])
        driver.get_element("technologies").send_keys(data["technologies"])
        driver.get_element("scm-link").send_keys(data["scm-link"])
        driver.get_element("wiki-link").send_keys(data["wiki-link"])

    @staticmethod
    def submit_form(driver):

        driver.get_element("btn-submit").click()

    @staticmethod
    def clear_form(driver):
        driver.get_element("asset-name").clear()
        driver.get_element("asset-purpose").clear()
        driver.get_element("author-ids").clear()
        driver.get_element("technologies").clear()
        driver.get_element("scm-link").clear()
        driver.get_element("wiki-link").clear()
