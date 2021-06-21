import re

from selenium.webdriver.common.by import By

from .base_page import BasePage


class Page10Locators:

    LINK = (By.CSS_SELECTOR, r"[href='\/dynamictable']")
    ROWS = (By.CSS_SELECTOR, "[role] [role] [role='row']")
    FIELD = (By.XPATH, "/html//section//p[@class='bg-warning']")


class Page10(BasePage):

    def go_to_page(self):

        link = self.find_element(Page10Locators.LINK)
        link.click()

    def getting_chrome_cpu_from_table(self):
        a = self.find_elements(Page10Locators.ROWS)
        for i in a:
            if "Chrome" in i.text:
                regexp = r'[0-9]{1,3}.[0-9]{1,2}%'
                return re.search(regexp, i.text).group(0)

    def get_cpu_value(self):
        field = self.find_element(Page10Locators.FIELD)
        return field.text
