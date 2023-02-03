import json
import os
import time
import unittest

import HtmlTestRunner

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from PageObjects.PIM_login_page_objects import LoginPage
from PageObjects.PIM_search_page_objects import PimSearchBoxPageObjects
from Testcases.TestData.class_expected_items_list import ExpectedItemList

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PIMSearchBox(unittest.TestCase):
    driver = None
    cwd = os.getcwd()
    print(cwd)
    json_test_data_file_path = '%s%s' % (cwd, '\\TestData\\login_data.json') # '''use this when run from pycharm '''
    #json_test_data_file_path = '%s%s' % (cwd, '\\Testcases\\TestData\\login_data.json')  # '''use this when run from
    # command prompt'''
    with open(json_test_data_file_path) as json_file:
        data_dict = json.load(json_file)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
        # cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        cls.driver.get(baseURL)
        cls.driver.maximize_window()

        login_page = LoginPage(cls.driver)
        valid_username = cls.data_dict.get("login_test_data").get("valid_username")
        valid_password = cls.data_dict.get("login_test_data").get("valid_password")
        login_page.enterUserName(valid_username)
        login_page.enterPassword(valid_password)
        login_page.clickLogin()

    def test_search_box_presence(self):
        self.search_page = PimSearchBoxPageObjects(self.driver)
        assert self.search_page.search_box_presence()

    def test_menu_options_on_side_pane(self):
        self.search_page = PimSearchBoxPageObjects(self.driver)
        actual_menu_items = self.search_page.get_actual_menu_items()
        assert actual_menu_items == ExpectedItemList.pim_expected_menu_list

    def test_menu_items_lowercase_check(self):
        self.search_page = PimSearchBoxPageObjects(self.driver)
        for item in ExpectedItemList.pim_expected_menu_list:
            self.search_page.menu_item_search(item.lower())
            assert self.driver.find_element(By.XPATH, "//ul[@class='oxd-main-menu']/li/a/span").text == item

    # def test_menu_items_uppercase_check(self):
    #     self.search_page = PimSearchBoxPageObjects(self.driver)
    #     for item in ExpectedItemList.pim_expected_menu_list:
    #         self.search_page.menu_item_search(item.upper())
    #         assert self.driver.find_element(By.XPATH, "//ul[@class='oxd-main-menu']/li/a/span").text == item

    @classmethod
    def tearDownClass(cls) -> None:  # none means when we don't return anything
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\jeyalakshmi\\PycharmProjects\\Guvi_Pom_Project1\\Reports"))
