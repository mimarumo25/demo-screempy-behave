from screenpy import Actor
from screenpy_selenium import BrowseTheWeb
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ChooseFromList:

    def __init__(self, actor, element, search):
        self.actor = actor
        self.element = element
        self.search = search

    def choose_from_list(self):
        # item2 = self.actor.find_element(By.XPATH, self.element)
        browser = self.actor.ability_to(BrowseTheWeb).browser
        item2 = browser.find_element(By.XPATH, self.element)
        # item = WebElement.find_element(element)
        options = item2.find_elements(By.TAG_NAME, "li")
        for option in options:
            if option.text == self.search:
                option.click()
                break  # Exit the loop once the option is found
