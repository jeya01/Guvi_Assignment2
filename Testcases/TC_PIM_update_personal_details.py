import json
import os
import time
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chromeService

from PageObjects.PIM_login_page_objects import LoginPage
from PageObjects.PIM_update_personal_details_page_objects import PIMUpdatePersonalDetailsPageObjects


class PIMUpdatePersonalDetails(unittest.TestCase):
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




    def test_update_personal_details(self):
        self.update_personal_details = PIMUpdatePersonalDetailsPageObjects(self.driver)
        self.update_personal_details.clickPIM()
        emp_id= "0304"
        self.update_personal_details.click_added_employee(emp_id)
        self.update_personal_details.click_personal_details_link()
        self.update_personal_details.enter_ssn_number("123")
        self.update_personal_details.enter_sin_number("456")
        time.sleep(10)
        self.update_personal_details.clickSaveButton()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

