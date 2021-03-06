import unittest

from pages.page5 import Page5
from .config import driver as d


class TestPage5(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = d

    def tearDown(self) -> None:
        self.driver.quit()

    def test_user_can_see_the_data_afte_ajax_request(self):
        """Check the elements appeared on a page after loading
        data with AJAX request"""

        self.page = Page5(self.driver)
        self.page.go_to_site()
        self.page.go_to_page()
        self.page.press_the_button()
        ajax_data = self.page.get_the_data_from_ajax()
        self.assertEqual(ajax_data, "Data loaded with AJAX get request.")
