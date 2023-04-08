import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestValidInput(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_valid_input(self):
        self.browser.get('https://demo.guru99.com/test/newtours/register.php')

        # Step 1: Enter valid data in the form fields
        self.browser.find_element(By.NAME, 'firstName').send_keys('John')
        self.browser.find_element(By.NAME, 'lastName').send_keys('Doe')
        self.browser.find_element(By.NAME, 'phone').send_keys('123-456-7890')
        self.browser.find_element(By.NAME, 'userName').send_keys('john.doe@example.com')
        self.browser.find_element(By.NAME, 'address1').send_keys('123 Main St')
        self.browser.find_element(By.NAME, 'city').send_keys('New York')
        self.browser.find_element(By.NAME, 'state').send_keys('NY')
        self.browser.find_element(By.NAME, 'postalCode').send_keys('10001')
        country_select = Select(self.browser.find_element(By.NAME, 'country'))
        country_select.select_by_visible_text('UNITED STATES')
        self.browser.find_element(By.NAME, 'email').send_keys('JohnDoe2023')
        self.browser.find_element(By.NAME, 'password').send_keys('P@ssw0rd123')
        self.browser.find_element(By.NAME, 'confirmPassword').send_keys('P@ssw0rd123')

        # Step 2: Click the submit button
        self.browser.find_element(By.NAME, 'submit').click()

        # Step 3: Verify that the account has been created successfully
        expected_url = 'https://demo.guru99.com/test/newtours/register_sucess.php'
        WebDriverWait(self.browser, 10).until(EC.url_to_be(expected_url))
        self.assertEqual(self.browser.current_url, expected_url)

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)