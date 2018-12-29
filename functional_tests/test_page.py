import time

from functional_tests.base import FunctionalTest


class PageTest(FunctionalTest):
    def test_title(self):
        self.browser.get(self.live_server_url)
        text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Chess', text)

    def test_beginner_chess(self):
        self.browser.get(self.live_server_url)
        title_list = self.browser.find_element_by_tag_name('ul')
        learn_the_basics = title_list.find_elements_by_tag_name('li')[0]

        self.assertEqual('Learn the basics!', learn_the_basics.text)
        learn_the_basics.click()
        chess_board = self.browser.find_element_by_id('board')
        self.assertIsNotNone(chess_board)




