from selenium.webdriver.common.by import By

from .base_page import BasePage


class Page6Locators:
    LINK = (By.CSS_SELECTOR, r"[href='\/clientdelay']")
    BUTTON = (By.CSS_SELECTOR, "button#ajaxButton")
    AJAX_DATA = (By.XPATH, "//div[@id='content']/p[@class='bg-success']")


class Page6(BasePage):
    def go_to_page(self):
        link = self.find_element(Page6Locators.LINK)
        link.click()

    def press_the_button(self):
        self.click_element(Page6Locators.BUTTON)

    def get_the_data_from_ajax(self):
        client_data = self.find_element(Page6Locators.AJAX_DATA).text
        return client_data
