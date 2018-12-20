import time

from functional_tests.base import FunctionalTest


class PageTest(FunctionalTest):
    def test_title(self):
        self.browser.get(self.live_server_url)
        text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Chess', text)

        list = self.browser.find_element_by_tag_name('ul')
        rows = list.find_elements_by_tag_name('li')
        self.assertIn('Learn the basics!', [row.text for row in rows])

        print(repr(list))

