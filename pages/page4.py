"""
Module to describe the Load Delay page of http://uitestingplayground.com/
"""

from selenium.webdriver.common.by import By

from .base_page import BasePage


class Page4Locators:
    """Class for Load Delay page locators"""

    LINK = (
        By.XPATH,
        r"""/html//section[@id='overview']
        /div[@class='container']//a[@href='/loaddelay']""",
    )
    BUTTON = (By.XPATH, r"/html//section//button[@class='btn btn-primary']")


class Page4(BasePage):
    """Class describing the Load Delay page"""

    def go_to_page(self):
        """Clicking the page link"""

        self.click_element(Page4Locators.LINK)
        # link.click()

    def press_the_button(self):
        """Finding and pressing definite button"""

        self.click_element(Page4Locators.BUTTON)
        # button.click()
