import unittest

from pages.page9 import Page9
from .config import driver as d


class TestPage9(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = d

    def tearDown(self) -> None:
        self.driver.quit()

    def test_user_can_see_scrolled_button(self):
        """Ensure scrolling an element into view is possible"""

        self.page = Page9(self.driver)
        self.page.go_to_site()
        self.page.go_to_page()
        self.page.scroll_to_button()
        self.page.click_the_button()
