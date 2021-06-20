"""
Module to describe the Click page of http://uitestingplayground.com/
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

from .base_page import BasePage


class Page7Locators:
    """Class for Click page locators"""

    LINK = (By.CSS_SELECTOR, r"[href='\/click']")
    BUTTON = (By.XPATH, "/html//button[@id='badButton']")


class Page7(BasePage):
    """Class describing the Click page"""

    def go_to_page(self):
        """Clicking the page link"""

        link = self.find_element(Page7Locators.LINK)
        link.click()

    def press_the_button(self):
        """Finding and pressing definite button"""

        self.click_element(Page7Locators.BUTTON)

    def get_the_button_attribute(self):
        """Getting button attribute and transform it into hex"""

        button_attribute = self.find_element(
            Page7Locators.BUTTON
        ).value_of_css_property("background-color")

        return Color.from_string(button_attribute).hex
