"""
Module to describe the Client Delay page of http://uitestingplayground.com/
"""

from selenium.webdriver.common.by import By

from .base_page import BasePage


class Page6Locators:
    """Class for Client Side Delay page locators"""

    LINK = (By.CSS_SELECTOR, r"[href='\/clientdelay']")
    BUTTON = (By.CSS_SELECTOR, "button#ajaxButton")
    AJAX_DATA = (By.XPATH, "//div[@id='content']/p[@class='bg-success']")


class Page6(BasePage):
    """Class describing the Client Side Delay page"""

    def go_to_page(self):
        """Clicking the page link"""

        link = self.find_element(Page6Locators.LINK)
        link.click()

    def press_the_button(self):
        """Finding and pressing definite button"""

        self.click_element(Page6Locators.BUTTON)

    def get_the_data_from_ajax(self):
        """Getting text data from a ajax request"""

        client_data = self.find_element(Page6Locators.AJAX_DATA).text
        return client_data
