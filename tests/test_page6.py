import unittest

from pages.page6 import Page6
from .config import driver as d


class TestPage6(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = d

    def tearDown(self) -> None:
        self.driver.quit()

    def test_user_can_see_the_delayed_data(self):
        """Check elements appeared after client-side time consuming
        JavaScript calculations"""

        self.page = Page6(self.driver)
        self.page.go_to_site()
        self.page.go_to_page()
        self.page.press_the_button()
        client_data = self.page.get_the_data_from_ajax()
        self.assertEqual(client_data, "Data calculated on the client side.")
