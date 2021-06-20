import unittest

from selenium import webdriver

from pages.page9 import Page9


class TestPage8(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_user_can_see_scrolled_button(self):
        """Ensure scrolling an element into view is possible"""

        self.page = Page9(self.driver)
        self.page.go_to_site()
        self.page.go_to_page()
        self.page.scroll_to_button()
        self.page.click_the_button()
