import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

from PageObjects.PIM_edit_page_objects import PimEditEmployeePage
from PageObjects.PIM_login_page_objects import LoginPage


class PIMEditEmployee(unittest.TestCase):
    driver = None
    cwd = os.getcwd()
    print(cwd)
    json_test_data_file_path = '%s%s' % (cwd, '\\TestData\\login_data.json')
    print(json_test_data_file_path)
    with open(json_test_data_file_path) as json_file:
        data_dict = json.load(json_file)
    print(data_dict)


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        login_page = LoginPage(cls.driver)
        valid_username = cls.data_dict.get("login_test_data").get("valid_username")
        valid_password = cls.data_dict.get("login_test_data").get("valid_password")
        login_page.enterUserName(valid_username)
        login_page.enterPassword(valid_password)
        login_page.clickLogin()

    def testEditEmployee(self):
        self.edit_employee = PimEditEmployeePage(self.driver)
        self.edit_employee.clickPIM()
        self.edit_employee.clickEditPencil()
        emp_license_expiry_year = "1985"
        emp_license_expiry_month = "01"
        emp_license_expiry_date = "01"

        self.edit_employee.clickEditDate(emp_license_expiry_year, emp_license_expiry_month, emp_license_expiry_date)
        time.sleep(10)
        self.edit_employee.clickSaveButton()
        print("Save is clicked")
        time.sleep(10)
        expiry_date_box = self.driver.find_element(By.XPATH,"//label[text()='License Expiry Date']/../../div/child::div/div/input")
        time.sleep(10)
        print(expiry_date_box.text)

        # time.sleep(20)
        # expiry_date_box = self.driver.find_element(By.XPATH,
        #                                            "//label[text()='License Expiry Date']/../../div/child::div/div/input")
        # license_expiry_date = emp_license_expiry_year + "-" + emp_license_expiry_month + "-" + emp_license_expiry_date
        # assert WebDriverWait(self.driver,20).until(expected_conditions.text_to_be_present_in_element(expiry_date_box,license_expiry_date))
        # print(expiry_date_box.text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()
