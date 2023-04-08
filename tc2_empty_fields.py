import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestEmptyFields(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_empty_fields(self):
        self.browser.get('https://demo.guru99.com/test/newtours/register.php')

        # Step 1: Leave all fields empty

        # Step 2: Click the submit button
        self.browser.find_element(By.NAME, 'submit').click()

        # Step 3: Verify if the browser redirects to the register_sucess.php page
        # This is a defect in the website and is covered in Defect 001
        WebDriverWait(self.browser, 10).until(
            EC.url_contains("register_sucess.php")
        )

        current_url = self.browser.current_url
        self.assertIn("register_sucess.php", current_url)

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)