from django.test import TestCase
from quotes.models import Quote


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class QuoteModelTest(TestCase):

    def test_save_and_retrieve_quotes(self):
        first_quote = Quote()
        first_quote.text = 'This is a very good quote'
        first_quote.save()

        second_quote = Quote()
        second_quote.text = 'This is also a very good quote...'
        second_quote.save()

        saved_items = Quote.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'This is a very good quote')
        self.assertEqual(second_saved_item.text,
                         'This is also a very good quote...')
