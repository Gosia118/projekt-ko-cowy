#IMPORT BIBLIOTEK
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class ProjectSearchAndAddingProduct(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://automationpractice.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)

    def test_choose_and_add_product(self):
        driver = self.driver
        choose_dresses = driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[2]/a")
        choose_dresses.click()

        choose_casual_dresses = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/ul/li[1]/div[1]/a/img")
        choose_casual_dresses.click()

        choose_printed_dress = driver.find_element(By.LINK_TEXT, "Printed Dress")
        choose_printed_dress.click()

        select_printed_dress = driver.find_element(By.ID, "add_to_cart")
        select_printed_dress.click()

        go_to_cart = driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/a")
        go_to_cart.click()

        sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
