from selenium.webdriver.common.by import By

from .base_page import BasePage


class Page3Locators:
    LINK = (By.CSS_SELECTOR, r"[href='\/hiddenlayers']")
    BUTTON = (By.XPATH, "/html//button[@id='greenButton']")


class Page3(BasePage):
    def go_to_page(self):
        link = self.find_element(Page3Locators.LINK)
        link.click()

    def press_green_button(self):
        self.click_element(Page3Locators.BUTTON)
