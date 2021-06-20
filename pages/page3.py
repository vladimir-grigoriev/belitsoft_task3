"""
Module to describe the Hidden Layers page of http://uitestingplayground.com/
"""

from selenium.webdriver.common.by import By

from .base_page import BasePage


class Page3Locators:
    """Class for Hidden Layers page locators"""

    LINK = (By.CSS_SELECTOR, r"[href='\/hiddenlayers']")
    BUTTON = (By.XPATH, "/html//button[@id='greenButton']")


class Page3(BasePage):
    """Class describing the Class Attribute page"""

    def go_to_page(self):
        """Clicking the page link"""

        link = self.find_element(Page3Locators.LINK)
        link.click()

    def press_green_button(self):
        """Finding and pressing definite green button"""

        self.click_element(Page3Locators.BUTTON)
