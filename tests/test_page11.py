import unittest

from pages.page11 import Page11
from .config import driver as d


class TestPage11(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = d

    def tearDown(self) -> None:
        self.driver.quit()

    def test_field_with_definite_value_is_reachable(self):
        """ finds an element with 'Welcome...' text"""

        self.page = Page11(self.driver)
        self.page.go_to_site()
        self.page.go_to_page()
        text = self.page.get_field_value()
        self.assertAlmostEqual(text, "Welcome UserName!")
