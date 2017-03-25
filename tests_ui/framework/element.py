from logger import Logger

class Element():

    def __init__(self, element, name):
        self.element = element
        self.name = name

    def click(self):
        try:
            Logger.log_info("Clicking on '" + self.name + "'")
            self.element.click()
        except Exception:
            Logger.log_fail("Element '" + self.name + "'could not be clicked")

    def send_keys(self, keys):
        try:
            Logger.log_info("Sending keys '" + str(keys) + "' to '" + self.name + "'")
            self.element.send_keys(keys)
        except Exception:
            Logger.log_fail("Could not send '" + str(keys) + "' to element '" + self.name + "'")

    def clear(self):
        self.element.clear()
