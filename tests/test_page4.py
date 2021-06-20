import unittest

from selenium import webdriver

from pages.page4 import Page4


class TestPage4(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_can_see_the_page_after_long_delay(self):
        self.page = Page4(self.driver)
        self.page.go_to_site()
        self.page.go_to_page()
        self.assertEqual(self.driver.title, "Load Delays")
        self.page.press_the_button()
