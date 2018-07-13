from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_see_a_quote(self):
        # Elise has heard about a cool new online quote generation app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention quote generation
        self.assertIn('Quote Generation', self.browser.title)
        self.fail('Finish the test!')

        # A quote is shown to her straight away

        # When she refreshes the page, the page now shows another quote

        # Satisfied, she goes back to sleep


if __name__ == '__main__':
    unittest.main()
