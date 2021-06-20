"""
Module to describe the Text Input page of http://uitestingplayground.com/
"""

from selenium.webdriver.common.by import By

from .base_page import BasePage


class Page8Locators:
    """Class for Text Input page locators"""

    LINK = (By.CSS_SELECTOR, r"[href='\/textinput']")
    BUTTON = (By.CSS_SELECTOR, "#updatingButton")
    INPUT = (By.CSS_SELECTOR, "#newButtonName")


class Page8(BasePage):
    """Class describing the Click page"""

    def go_to_page(self):
        """Clicking the page link"""

        link = self.find_element(Page8Locators.LINK)
        link.click()

    def fill_the_input_field(self, text):
        """Finding and filling input field with selected text"""

        self.send_keys(Page8Locators.INPUT, text)

    def press_the_button(self):
        """Finding and pressing the button"""

        self.click_element(Page8Locators.BUTTON)

    def get_the_button_text(self):
        """Getting the pressed button text"""

        return self.find_element(Page8Locators.BUTTON).text
