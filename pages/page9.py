"""
Module to describe the Scrollbars page of http://uitestingplayground.com/
"""

from selenium.webdriver.common.by import By

from .base_page import BasePage


class Page9Locators:
    """Class for Scrollbars page locators"""

    LINK = (By.CSS_SELECTOR, r"[href='\/scrollbars']")
    BUTTON = (By.CSS_SELECTOR, "#hidingButton")


class Page9(BasePage):
    """Class describing the Scrollbars page"""

    def go_to_page(self):
        """Clicking the page link"""

        link = self.find_element(Page9Locators.LINK)
        link.click()

    def scroll_to_button(self):
        """Executing JavaScript code to scroll to button"""

        button = self.find_element(Page9Locators.BUTTON)
        self.driver.execute_script(
            "return arguments[0].scrollIntoView(true);", button
        )

    def click_the_button(self):
        """Pressing founded button"""

        self.click_element(Page9Locators.BUTTON)
