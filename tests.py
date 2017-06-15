from selenium import webdriver
import unittest


class TestHomepage(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:5000/')
        self.assertEqual(self.browser.title, 'AirAnywhere')

    def test_new_search(self):
        self.browser.get('http://localhost:5000/')

        inputElement = self.browser.find_element_by_id('origin-airport-field')
        inputElement.send_keys('San Francisco International Airport (SFO)')
        inputElement.submit()

        outputElement = self.browser.find_element_by_id('results-div')
        print outputElement


if __name__ == "__main__":
    unittest.main()


# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
# from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0

# # Create a new instance of the Firefox driver
# driver = webdriver.Firefox()

# # go to the google home page
# driver.get("http://www.google.com")

# # the page is ajaxy so the title is originally this:
# print driver.title

# # find the element that's name attribute is q (the google search box)
# inputElement = driver.find_element_by_name("q")

# # type in the search
# inputElement.send_keys("cheese!")

# # submit the form (although google automatically searches now without submitting)
# inputElement.submit()

# try:
#     # we have to wait for the page to refresh, the last thing that seems to be updated is the title
#     WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))

#     # You should see "cheese! - Google Search"
#     print driver.title

# finally:
#     driver.quit()
