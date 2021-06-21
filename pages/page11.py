from selenium.webdriver.common.by import By

from .base_page import BasePage


class Page11Locators:

    LINK = (By.CSS_SELECTOR, r"[href='\/verifytext']")
    FIELD = (By.XPATH, "//span[normalize-space(.)='Welcome UserName!']")


class Page11(BasePage):

    def go_to_page(self):

        link = self.find_element(Page11Locators.LINK)
        link.click()

    def get_field_value(self):
        field = self.find_element(Page11Locators.FIELD)
        return field.text
