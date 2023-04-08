import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class TestInvalidEmail(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_invalid_email(self):
        self.browser.get('https://demo.guru99.com/test/newtours/register.php')

        # Fill out the form fields with valid data except for the email field
        self.browser.find_element(By.NAME, 'firstName').send_keys('John')
        self.browser.find_element(By.NAME, 'lastName').send_keys('Doe')
        self.browser.find_element(By.NAME, 'phone').send_keys('123-456-7890')
        self.browser.find_element(By.NAME, 'userName').send_keys('invalid_email')
        self.browser.find_element(By.NAME, 'address1').send_keys('123 Main St')
        self.browser.find_element(By.NAME, 'city').send_keys('New York')
        self.browser.find_element(By.NAME, 'state').send_keys('NY')
        self.browser.find_element(By.NAME, 'postalCode').send_keys('10001')

        # Select a country from the dropdown
        country_select = Select(self.browser.find_element(By.NAME, 'country'))
        country_select.select_by_visible_text('UNITED STATES')

        # Enter username and password
        self.browser.find_element(By.NAME, 'email').send_keys('JohnDoe2023')
        self.browser.find_element(By.NAME, 'password').send_keys('P@ssw0rd123')
        self.browser.find_element(By.NAME, 'confirmPassword').send_keys('P@ssw0rd123')

        # Click the submit button
        self.browser.find_element(By.NAME, 'submit').click()

        # Check if the browser is redirected to the success page
        # This is a defect in the website and is covered in Defect 002
        success_url = 'https://demo.guru99.com/test/newtours/register_sucess.php'
        self.assertEqual(self.browser.current_url, success_url, "The browser is not redirected to the success page.")

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)