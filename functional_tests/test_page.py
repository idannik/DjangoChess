import time

from functional_tests.base import FunctionalTest


class PageTest(FunctionalTest):
    def test_a(self):
        self.browser.get(self.live_server_url)
        text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Chess', text)


