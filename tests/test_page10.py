import unittest

from selenium import webdriver

from pages.page10 import Page10
from .config import capabilities, link


class TestPage10(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Remote(
        #     command_executor=link,
        #     desired_capabilities=capabilities)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_google_cpu_from_table_matches_cpu_from_reference_field(self):
        """Matching chrome CPU values from dynamic table"""

        self.page = Page10(self.driver)
        self.page.go_to_site()
        self.page.go_to_page()
        chrome_cpu = self.page.getting_chrome_cpu_from_table()
        reference_chrome_cpu = self.page.get_cpu_value()
        self.assertIn(chrome_cpu, reference_chrome_cpu)
