"""This is the module with parent base page class"""

import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """base class to be inherited."""

    def __init__(self, driver) -> None:
        """Constructor method"""

        self.driver = driver
        self.base_url = "http://uitestingplayground.com"

    def go_to_site(self):
        """Common method to open definite link in browser"""

        return self.driver.get(self.base_url)

    def click_element(self, locator):
        """Common method to find and click definite element in browser"""

        time.sleep(0.5)
        return (
            WebDriverWait(self.driver, 20)
            .until(EC.element_to_be_clickable(locator), message="Nope")
            .click()
        )

    def send_keys(self, locator, text, timeout=20):
        """Common method to find and send keys to an element in browser"""

        time.sleep(0.5)
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def find_element(self, locator, timeout=20):
        """Common method to find an element in browser"""

        time.sleep(0.5)
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_elements(self, locator, timeout=20):
        time.sleep(0.5)
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )
