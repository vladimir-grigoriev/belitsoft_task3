from selenium.webdriver.common.by import By

from .base_page import BasePage


class Page8Locators:
    LINK = (By.CSS_SELECTOR, r"[href='\/textinput']")
    BUTTON = (By.CSS_SELECTOR, "#updatingButton")
    INPUT = (By.CSS_SELECTOR, "#newButtonName")


class Page8(BasePage):
    def go_to_page(self):
        link = self.find_element(Page8Locators.LINK)
        link.click()

    def fill_the_input_field(self, text):
        self.send_keys(Page8Locators.INPUT, text)

    def press_the_button(self):
        self.click_element(Page8Locators.BUTTON)

    def get_the_button_text(self):
        return self.find_element(Page8Locators.BUTTON).text
