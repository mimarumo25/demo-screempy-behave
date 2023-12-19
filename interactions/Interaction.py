import time

from selenium.webdriver import ActionChains


class Interaction:

    def __init__(self, driver):
        self.driver = driver

    def click_on(self, target):
        element = target.resolve_for(self.driver)
        actions = ActionChains(self.driver)
        actions.click(element).perform()
        time.sleep(1)
