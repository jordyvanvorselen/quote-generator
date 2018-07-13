from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--headless")
        self.browser = webdriver.Chrome(chrome_options=chrome_options)

    def tearDown(self):
        self.browser.quit()

    def test_can_see_a_quote(self):
        # Elise has heard about a cool new online quote generation app. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention quote generation
        self.assertIn('Quote Generation', self.browser.title)

        # A quote is shown to her straight away
        quote_text = self.browser.find_element_by_id('Quote').text
        self.assertNotEqual(quote_text, '')
        self.fail('Finish the test!')

        # When she refreshes the page, the page now shows another quote

        # Satisfied, she goes back to sleep
