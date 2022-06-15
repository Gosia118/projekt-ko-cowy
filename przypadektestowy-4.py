import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

my_email = 'aaa@jigdrsrs.com'

class ProjectLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://automationpractice.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)

    def test_sign_in_to_website(self):
        #otwieranie karty signin
        driver = self.driver
        sign_in = driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign in')
        sign_in.click()
        #podanie address email
        email_address = driver.find_element(By.ID, 'email_create')
        email_address.send_keys(my_email)
        #przycisk create an account
        create_an_account = driver.find_element(By.ID, 'SubmitCreate')
        create_an_account.click()

        sleep(6)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
