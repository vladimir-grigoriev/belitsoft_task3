import unittest

from selenium.common.exceptions import ElementClickInterceptedException

from pages.page3 import Page3
from .config import driver as d


class TestPage3(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = d

    def tearDown(self) -> None:
        self.driver.quit()

    def test_user_cant_press_green_button_again(self):
        """Verify that your test does not interact with elements invisible
        because of z-order"""

        self.page = Page3(self.driver)
        self.page.go_to_site()
        self.page.go_to_page()
        self.page.press_green_button()
        self.assertRaises(
            ElementClickInterceptedException, self.page.press_green_button
        )
