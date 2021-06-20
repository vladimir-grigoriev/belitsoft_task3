"""
Module to describe the AJAX Data page of http://uitestingplayground.com/
"""

from selenium.webdriver.common.by import By

from .base_page import BasePage


class Page5Locators:
    """Class for AJAX Data page locators"""

    LINK = (By.CSS_SELECTOR, r"[href='\/ajax']")
    BUTTON = (By.CSS_SELECTOR, "button#ajaxButton")
    AJAX_DATA = (By.XPATH, "//div[@id='content']/p[@class='bg-success']")


class Page5(BasePage):
    """Class describing the AJAX Data page"""

    def go_to_page(self):
        """Clicking the page link"""

        link = self.find_element(Page5Locators.LINK)
        link.click()

    def press_the_button(self):
        """Finding and pressing definite button"""

        self.click_element(Page5Locators.BUTTON)

    def get_the_data_from_ajax(self):
        """Getting text data from a ajax request"""

        ajax_field = self.find_element(Page5Locators.AJAX_DATA).text
        return ajax_field
