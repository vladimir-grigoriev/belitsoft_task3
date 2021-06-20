import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

from .base_page import BasePage


class Page7Locators:
    LINK = (By.CSS_SELECTOR, r"[href='\/click']")
    BUTTON = (By.XPATH, "/html//button[@id='badButton']")


class Page7(BasePage):
    def go_to_page(self):
        link = self.find_element(Page7Locators.LINK)
        link.click()

    def press_the_button(self):
        self.click_element(Page7Locators.BUTTON)

    def get_the_button_attribute(self):
        time.sleep(1)
        button_attribute = self.find_element(
            Page7Locators.BUTTON
        ).value_of_css_property("background-color")
        return Color.from_string(button_attribute).hex
