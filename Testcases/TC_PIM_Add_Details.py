import json
import os
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from PageObjects.PIM_add_page_objects import PimAddNewEmployeeObjects
from PageObjects.PIM_login_page_objects import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PIMAddNewEmployee(unittest.TestCase):
    driver = None
    cwd = os.getcwd()
    json_test_data_file_path = '%s%s' % (cwd,'\\TestData\\login_data.json')
    with open(json_test_data_file_path) as json_file:
        data_dict = json.load(json_file)
    print(data_dict)




    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
        # cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

        login_page = LoginPage(cls.driver)
        valid_username = self.data_dict.get("login_test_data").get("valid_username")
        valid_password = self.data_dict.get("login_test_data").get("valid_password")
        login_page.enterUserName(valid_username)
        login_page.enterPassword(valid_password)
        login_page.clickLogin()

    def test_add_employee(self):
        self.add_employee = PimAddNewEmployeeObjects(self.driver)
        self.add_employee.clickPIM()
        self.add_employee.clickAdd()
        emp_firstname = "And"
        emp_lastname = "Kni"
        self.add_employee.enterFirstName(emp_firstname)
        self.add_employee.enterLastName(emp_lastname)
        emp_name = emp_firstname + ' ' + emp_lastname
        self.add_employee.uploadPhoto()
        self.add_employee.clickSave()

        # employee_element_text = self.driver.find_element(By.XPATH,
        #                                                  "//div[@class='orangehrm-edit-employee-name']/h6").text
        #
        # print(f'{employee_element_text}')
        #
        assert WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='orangehrm-edit-employee-name']/h6"), emp_name))

        employee_element_text = self.driver.find_element(By.XPATH,
                                                         "//div[@class='orangehrm-edit-employee-name']/h6").text

        print(f'{employee_element_text}')
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main':
    unittest.main()
