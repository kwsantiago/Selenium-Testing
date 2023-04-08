import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class TestPasswordMismatch(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_password_mismatch(self):
        self.browser.get('https://demo.guru99.com/test/newtours/register.php')

        # Fill out the form fields with valid data
        self.browser.find_element(By.NAME, 'firstName').send_keys('John')
        self.browser.find_element(By.NAME, 'lastName').send_keys('Doe')
        self.browser.find_element(By.NAME, 'phone').send_keys('123-456-7890')
        self.browser.find_element(By.NAME, 'userName').send_keys('john.doe@example.com')
        self.browser.find_element(By.NAME, 'address1').send_keys('123 Main St')
        self.browser.find_element(By.NAME, 'city').send_keys('New York')
        self.browser.find_element(By.NAME, 'state').send_keys('NY')
        self.browser.find_element(By.NAME, 'postalCode').send_keys('10001')
        country_select = Select(self.browser.find_element(By.NAME, 'country'))
        country_select.select_by_visible_text('ALBANIA')
        self.browser.find_element(By.NAME, 'email').send_keys('JohnDoe2023')
        self.browser.find_element(By.NAME, 'password').send_keys('P@ssw0rd123')
        self.browser.find_element(By.NAME, 'confirmPassword').send_keys('P@ssw0rd456')

        # Click the submit button
        self.browser.find_element(By.NAME, 'submit').click()

        # This is the error message the registration site gives when the passwords don't match
        # Wait for the error message to appear
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='PAssword and con.password does not match']"))
        )

        # Check if the error message is displayed
        error_message = self.browser.find_element(By.XPATH, "//span[text()='PAssword and con.password does not match']")
        self.assertTrue(error_message.is_displayed())

        # Verify that the user remains on the registration page
        current_url = self.browser.current_url
        self.assertEqual(current_url, 'https://demo.guru99.com/test/newtours/register.php')

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)