import json
import os
import unittest


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager

from PageObjects.PIM_login_page_objects import LoginPage


class TestLogin(unittest.TestCase):
    driver = None
    cwd = os.getcwd()
    print(cwd)
    json_test_data_file_path = '%s%s' % (cwd, '\\Testcases\\TestData\\login_data.json')
    #json_test_data_file_path = '%s%s' % (cwd,'\\TestData\\login_data.json')
    #print(json_test_data_file_path)
    with open(json_test_data_file_path) as json_file:
        data_dict = json.load(json_file)
    #print(data_dict)

    @classmethod
    def setUpClass(cls):
        driver = cls.driver
        cls.driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        cls.driver.get(base_url)
        cls.driver.maximize_window()

    '''Test with valid credentials'''

    def test_valid_login(self):
        self.login_page = LoginPage(self.driver)
        valid_username = self.data_dict.get("login_test_data").get("valid_username")
        valid_password = self.data_dict.get("login_test_data").get("valid_password")
        self.login_page.enterUserName(valid_username)
        self.login_page.enterPassword(valid_password)
        self.login_page.clickLogin()
        assert_text = self.login_page.getLoginAssetText()
        self.assertEqual("Dashboard", assert_text)

        '''Test with invalid username'''

    def test_invalid_username_login(self):
        self.login_page = LoginPage(self.driver)
        invalid_username = self.data_dict.get("login_test_data").get("invalid_username")
        valid_password = self.data_dict.get("login_test_data").get("valid_password")
        self.login_page.enterUserName(invalid_username)
        self.login_page.enterPassword(valid_password)
        self.login_page.clickLogin()
        error_message = self.login_page.getErrorMessage()
        assert error_message == "Invalid credentials"

        '''Test with invalid password'''

    def test_invalid_password_login(self):
        self.login_page = LoginPage(self.driver)
        valid_username = self.data_dict.get("login_test_data").get("valid_username")
        invalid_password = self.data_dict.get("login_test_data").get("invalid_password")
        self.login_page.enterUserName(valid_username)
        self.login_page.enterPassword(invalid_password)
        self.login_page.clickLogin()
        error_message = self.login_page.getErrorMessage()
        assert error_message == "Invalid credentials"

    @classmethod
    def tearDownClass(cls) -> None:  # none means when we don't return anything
        cls.driver.quit()


if __name__ == '__main_':
    unittest.main()
