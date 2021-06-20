import unittest

from selenium import webdriver

from pages.page5 import Page5


class TestPage5(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_user_can_see_the_data_afte_ajax_request(self):
        self.page = Page5(self.driver)
        self.page.go_to_site()
        self.page.go_to_page()
        self.page.press_the_button()
        ajax_data = self.page.get_the_data_from_ajax()
        self.assertEqual(ajax_data, "Data loaded with AJAX get request.")
