"""
Module to describe the Class Attribute page of http://uitestingplayground.com/
"""

from selenium.webdriver.common.by import By

from .base_page import BasePage


class Page2Locators:
    """Class for Class Attribute page locators"""

    LINK = (By.CSS_SELECTOR, r"[href='\/classattr']")
    BUTTON = (
        By.XPATH,
        r"""//button[contains(concat(
            ' ', normalize-space(@class), ' '), ' btn-primary ')]""",
    )


class Page2(BasePage):
    """Class describing the Class Attribute page"""

    def go_to_page(self):
        """Clicking the page link"""

        link = self.find_element(Page2Locators.LINK)
        link.click()

    def press_primary_button(self):
        """Finding and pressing selected button"""

        button = self.find_element(Page2Locators.BUTTON)
        button.click()

    def read_the_alert_text(self):
        """Reading the alert window text"""

        alert = self.driver.switch_to.alert
        alert_text = alert.text
        return alert, alert_text

    def close_the_alert_window(self, alert):
        """Closing the alert window"""

        alert.accept()
