from selenium.webdriver.common.by import By

from .base_page import BasePage


class Page9Locators:
    LINK = (By.CSS_SELECTOR, r"[href='\/scrollbars']")
    BUTTON = (By.CSS_SELECTOR, "#hidingButton")


class Page9(BasePage):
    def go_to_page(self):
        link = self.find_element(Page9Locators.LINK)
        link.click()

    def scroll_to_button(self):
        button = self.find_element(Page9Locators.BUTTON)
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", button)

    def click_the_button(self):
        self.click_element(Page9Locators.BUTTON)
