#IMPORT BIBLIOTEK
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#DANE TESTOWE UZYTKOWNIKA
invalid_email = "aa@jigdrsrs.com"
my_password = "AAApass567"

class ProjectLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://automationpractice.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)

    def test_sing_in_to_website(self):
        driver = self.driver
        sign_in = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
        sign_in.click()

        registered_email = driver.find_element(By.ID, "email")
        registered_email.send_keys(invalid_email)

        registered_password = driver.find_element(By.ID, "passwd")
        registered_password.send_keys(my_password)

        sign_in_button = driver.find_element(By.ID, "SubmitLogin")
        sign_in_button.click()

        sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
