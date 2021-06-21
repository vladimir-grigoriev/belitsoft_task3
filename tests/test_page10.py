import unittest

from selenium import webdriver

from pages.page10 import Page10


class TestPage8(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_user_can_see_scrolled_button(self):
        """Ensure scrolling an element into view is possible"""

        self.page = Page10(self.driver)
        self.page.go_to_site()
        self.page.go_to_page()
        chrome_cpu = self.page.getting_chrome_cpu_from_table()
        reference_chrome_cpu = self.page.get_cpu_value()
        self.assertIn(chrome_cpu, reference_chrome_cpu)
