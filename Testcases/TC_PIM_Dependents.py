import json
import os
import time
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chromeService

from PageObjects.PIM_login_page_objects import LoginPage
from PageObjects.PIM_dependents_page_objects import PIMDependentsPageObjects


class PIMDependents(unittest.TestCase):
    driver = None
    cwd = os.getcwd()
    json_test_data_file_path = '%s%s' % (cwd, '\TestData\\login_data.json')
    with open(json_test_data_file_path) as json_file:
        data_dict = json.load(json_file)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        cls.driver.get(baseURL)
        cls.driver.maximize_window()

        login_page = LoginPage(cls.driver)
        valid_username = cls.data_dict.get('login_test_data').get('valid_username')
        valid_password = cls.data_dict.get('login_test_data').get('valid_password')
        login_page.enterUserName(valid_username)
        login_page.enterPassword(valid_password)
        login_page.clickLogin()

    def test_dependents_page(self):
        self.dependents = PIMDependentsPageObjects(self.driver)
        self.dependents.clickPIM()
        self.dependents.click_added_employee("0070")
        self.dependents.click_dependents()
        self.dependents.click_dependents_add_button()
        self.dependents.enter_dependents_name("Name")
        self.dependents.select_dependents_relationship("Other")
        time.sleep(10)
        self.dependents.click_save_button()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()