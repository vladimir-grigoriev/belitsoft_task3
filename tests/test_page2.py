import unittest

from selenium import webdriver

from pages.page2 import Page2


class TestPage2(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_user_can_see_alert_window(self):
        self.page = Page2(self.driver)
        self.page.go_to_site()
        self.page.go_to_page()
        self.page.press_primary_button()
        alert, alertion_text = self.page.read_the_alert_text()
        self.assertEqual(
            alertion_text, "Primary button pressed", "message didn't matches"
        )
        self.page.close_the_alert_window(alert)
