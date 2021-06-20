import unittest

from selenium import webdriver

from pages.page7 import Page7


class TestPage7(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_button_changes_color_to_green_after_clicking(self):
        self.page = Page7(self.driver)
        self.page.go_to_site()
        self.page.go_to_page()
        self.page.press_the_button()
        button_color_attribute = self.page.get_the_button_attribute()
        self.assertEqual(button_color_attribute, "#218838")
