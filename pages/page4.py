from selenium.webdriver.common.by import By

from .base_page import BasePage


class Page4Locators:
    LINK = (
        By.XPATH,
        r"/html//section[@id='overview']/div[@class='container']//a[@href='/loaddelay']",
    )
    BUTTON = (By.XPATH, r"/html//section//button[@class='btn btn-primary']")


class Page4(BasePage):
    def go_to_page(self):
        link = self.find_element(Page4Locators.LINK)
        link.click()

    def press_the_button(self):
        button = self.find_element(Page4Locators.BUTTON)
        button.click()
