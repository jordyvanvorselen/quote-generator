from django.test import TestCase
from bs4 import BeautifulSoup
from .views import home_page
from django.http import request


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class QuoteModelTest(TestCase):

    def all_items_in_list_are_equal(self, list):
        return all(x == list[0] for x in list)

    def test_home_page_view_should_return_different_quote_each_refresh(self):
        first_quote = BeautifulSoup(
            home_page(request).content, "html.parser").find(id='Quote').string
        second_quote = BeautifulSoup(
            home_page(request).content, "html.parser").find(id='Quote').string
        self.assertNotEqual(first_quote, second_quote)

    def test_quote_on_home_page_should_change_upon_refresh(self):
        first_quote_soup = BeautifulSoup(
            self.client.get('/').content, "html.parser")
        first_quote = first_quote_soup.find(id='Quote').string
        second_quote_soup = BeautifulSoup(
            self.client.get('/').content, "html.parser")
        second_quote = second_quote_soup.find(id='Quote').string
        self.assertNotEqual(first_quote, second_quote)
