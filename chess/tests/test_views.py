from django.test import TestCase

# Create your tests here.

class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class ChessPageTest(TestCase):
    def test_uses_list_template(self):
        response = self.client.get(f'/chess/beginner/')
        self.assertTemplateUsed(response, 'chess.html')
