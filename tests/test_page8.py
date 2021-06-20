import unittest

from selenium import webdriver

from pages.page8 import Page8


class TestPage8(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_button_text_changes_after_pressing_the_button(self):
        """Ensure entering text into an edit field have effect"""

        self.page = Page8(self.driver)
        self.page.go_to_site()
        self.page.go_to_page()
        data_to_fill_the_input = ["hello", "0", "world"]
        for d in data_to_fill_the_input:
            self.page.fill_the_input_field(d)
            self.page.press_the_button()
            button_value = self.page.get_the_button_text()
            self.assertEqual(d, button_value)
