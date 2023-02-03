import json
import os
import time
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chromeService

from PageObjects.PIM_login_page_objects import LoginPage
from PageObjects.PIM_validate_employee_page_objects import PIMValidateEmployeePageObjects
from Testcases.TestData.class_expected_items_list import ExpectedItemList

class PIMValidateEmployee(unittest.TestCase):
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




    def test_validate_added_employee(self):
        self.validate_employee = PIMValidateEmployeePageObjects(self.driver)
        self.validate_employee.clickPIM()
        emp_id= "0275"
        self.validate_employee.click_added_employee(emp_id)
        emp_list_menu_items = self.validate_employee.get_emp_info_menu()
        assert emp_list_menu_items == ExpectedItemList.pim_employee_list_expected_menu_list




    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


