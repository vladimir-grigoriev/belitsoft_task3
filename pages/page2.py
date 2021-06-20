import time

from selenium.webdriver.common.by import By

from .base_page import BasePage


class Page2Locators:
    LINK = (By.CSS_SELECTOR, r"[href='\/classattr']")
    BUTTON = (
        By.XPATH,
        r"//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]",
    )


class Page2(BasePage):
    def go_to_page(self):
        link = self.find_element(Page2Locators.LINK)
        link.click()

    def press_primary_button(self):
        button = self.find_element(Page2Locators.BUTTON)
        button.click()

    def read_the_alert_text(self):
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        return alert, alert_text

    def close_the_alert_window(self, alert):
        alert.accept()
