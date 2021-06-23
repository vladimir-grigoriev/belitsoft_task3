import unittest

from pages.page8 import Page8
from .config import driver as d


class TestPage8(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = d

    def tearDown(self) -> None:
        self.driver.quit()

    def test_button_text_changes_after_pressing_the_button(self):
        """Ensure entering text into an edit field have effect"""

        self.page = Page8(self.driver)
        self.page.go_to_site()
        self.page.go_to_page()
        data_to_fill_the_input = ["hello", "0", "world"]
        for data in data_to_fill_the_input:
            self.page.fill_the_input_field(data)
            self.page.press_the_button()
            button_value = self.page.get_the_button_text()
            self.assertEqual(data, button_value)
