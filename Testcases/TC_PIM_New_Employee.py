import json
import os
import time
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chromeService

from PageObjects.PIM_login_page_objects import LoginPage
from PageObjects.PIM_new_employee_page_objects import PIMNewEmployeePageObjects

class PIMNewEmployee(unittest.TestCase):
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

    def test_pim_menu_option(self):
        self.new_employee = PIMNewEmployeePageObjects(self.driver)
        pim_menu_option = self.new_employee.validate_pim_menu_item()
        assert pim_menu_option == 'PIM'

    def test_add_new_employee(self):
        self.new_employee = PIMNewEmployeePageObjects(self.driver)
        self.new_employee.click_pim()
        self.new_employee.click_add_button()
        self.new_employee.enterFirstName("ccddee123")
        self.new_employee.enterLastName("bbbbbb1")
        self.new_employee.click_create_login_check_box()
        self.new_employee.enter_new_username("ccddeee123")
        self.new_employee.enter_password("Abcd@123")
        self.new_employee.enter_confirm_password("Abcd@123")
        self.new_employee.select_enabled_status()
        self.new_employee.click_save_button()
        employee_list_link_text = self.new_employee.validate_after_new_employee_creation()
        assert employee_list_link_text == "Employee List"
       



    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


