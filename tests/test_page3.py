import unittest

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException

from pages.page3 import Page3


class TestPage3(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Remote(
        #     command_executor=link,
        #     desired_capabilities=capabilities)

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
