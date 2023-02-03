import time
import unittest
import os
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager

from PageObjects.PIM_login_page_objects import LoginPage
from PageObjects.PIM_admin_user_mgmt_page_objects import PIMMAdminUserManagementPageObjects
from Testcases.TestData.class_expected_items_list import ExpectedItemList


class PIMAdminUserManagement(unittest.TestCase):
    driver = None
    cwd = os.getcwd()
    json_test_data_file_path = '%s%s' % (cwd, '\\TestData\\login_data.json')
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


    def test_admin_menu_option(self):
        self.user_management = PIMMAdminUserManagementPageObjects(self.driver)
        admin_menu_text = self.user_management.validate_admin_menu_option()
        assert admin_menu_text == 'Admin'


    def test_user_role_drop_down(self):
        self.user_management = PIMMAdminUserManagementPageObjects(self.driver)
        self.user_management.click_admin_menu()
        self.user_management.click_user_role()
        actual_user_role_list = self.user_management.get_actual_user_role_items()
        assert actual_user_role_list == ExpectedItemList.pim_expected_user_role_elements


    def test_status_drop_down(self):
        self.user_management = PIMMAdminUserManagementPageObjects(self.driver)
        admin_text = self.user_management.validate_admin_menu_option()
        self.user_management.click_admin_menu()
        self.user_management.click_status()
        actual_status_list = self.user_management.get_acutal_status_items()
        assert actual_status_list == ExpectedItemList.pim_expected_status_list



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
