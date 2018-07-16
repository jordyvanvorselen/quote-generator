from django.test import TestCase
from bs4 import BeautifulSoup
from .views import home_page
from django.http import request


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class QuoteModelTest(TestCase):

    def get_quote_from_response(self, response):
        return BeautifulSoup(response.content, "html.parser").find(id='Quote').string

    def test_home_page_view_should_return_different_quote_each_refresh(self):
        first_quote = self.get_quote_from_response(home_page(request))
        second_quote = self.get_quote_from_response(home_page(request))
        self.assertNotEqual(first_quote, second_quote)

    def test_quote_on_home_page_should_change_upon_refresh(self):
        first_quote = self.get_quote_from_response(self.client.get('/'))
        second_quote = self.get_quote_from_response(self.client.get('/'))
        self.assertNotEqual(first_quote, second_quote)
