import unittest

from selenium import webdriver

from pages.page2 import Page2
from .config import capabilities, link, driver_chrome


class TestPage2(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Remote(
        #     command_executor=link,
        #     desired_capabilities=capabilities)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_user_can_see_alert_window(self):
        """Check that class attribute based XPath is well formed"""

        self.page = Page2(self.driver)
        self.page.go_to_site()
        self.page.go_to_page()
        self.page.press_primary_button()
        alert, alertion_text = self.page.read_the_alert_text()
        self.assertEqual(
            alertion_text, "Primary button pressed", "message didn't matches"
        )
        self.page.close_the_alert_window(alert)
