import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://uitestingplayground.com"

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def click_element(self, locator):
        time.sleep(0.5)
        return (
            WebDriverWait(self.driver, 20)
            .until(EC.element_to_be_clickable(locator), message="Nope")
            .click()
        )

    def send_keys(self, locator, text, timeout=20):
        time.sleep(0.5)
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def find_element(self, locator, timeout=20):
        time.sleep(0.5)
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )
