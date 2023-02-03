from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PIMUpdatePersonalDetailsPageObjects:
    pim_link_xpath = "//span[text()='PIM']"
    pim_employee_info_menu_list_xpath = "//div[@role='tab']"
    pim_employee_personal_details_link_xpath = "//div[@role='tab']/a[text()='Personal Details']"
    pim_ssn_number_xpath = "//label[text()='SSN Number']/../following-sibling::div/input"
    pim_sin_number_xpath = "//label[text()='SIN Number']/../following-sibling::div/input"
    pim_save_button_xpath = "//div[@class='orangehrm-edit-employee']/div[2]/div[1]/form[@class='oxd-form']" \
                            "/div[@class='oxd-form-row']/../div[@class='oxd-form-actions']/button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def clickPIM(self):
        self.driver.find_element(By.XPATH, self.pim_link_xpath).click()

    def click_added_employee(self, emp_id):
        pim_added_employee = "//div[@role='table']//div[contains(text()," + emp_id + ")]" \
                                                                                     "/../following-sibling::div[7]/div/button[2]/i"
        self.driver.find_element(By.XPATH, pim_added_employee).click()

    def click_personal_details_link(self):
        self.driver.find_element(By.XPATH, self.pim_employee_personal_details_link_xpath).click()

    def enter_ssn_number(self, ssn_no):
        self.driver.find_element(By.XPATH, self.pim_ssn_number_xpath).click()
        self.driver.find_element(By.XPATH, self.pim_ssn_number_xpath).send_keys(ssn_no)

    def enter_sin_number(self, sin_no):
        self.driver.find_element(By.XPATH, self.pim_sin_number_xpath).click()
        self.driver.find_element(By.XPATH, self.pim_sin_number_xpath).send_keys(sin_no)

    def clickSaveButton(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_save_button_xpath)))
