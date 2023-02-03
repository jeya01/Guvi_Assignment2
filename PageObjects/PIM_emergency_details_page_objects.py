
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PIMEmergencyContactsPageObjects:
    pim_link_xpath = "//span[text()='PIM']"
    pim_emergency_contact_page_link_xpath = "//div[@role='tab']/a[text()='Emergency Contacts']"
    pim_emergency_add_button_xpath = "//div[@class='orangehrm-edit-employee-content']/div/div/button"
    pim_emergency_name_text_box_xpath = "//label[text()='Name']/../following-sibling::div/input"
    pim_emergency_relationship_text_box_xpath= "//label[text()='Relationship']/../following-sibling::div/input"
    pim_emergency_save_button_xpath = "//div[@class='orangehrm-edit-employee']/div[2]/div[1]/form[@class='oxd-form']" \
                                      "/div[@class='oxd-form-row']/../div[@class='oxd-form-actions']/button[@type='submit']"

    def __init__(self,driver):
        self.driver = driver

    def clickPIM(self):
        self.driver.find_element(By.XPATH, self.pim_link_xpath).click()

    def click_added_employee(self,emp_id):
        pim_added_employee = "//div[@role='table']//div[contains(text()," + emp_id + ")]" \
                                                                    "/../following-sibling::div[7]/div/button[2]/i"
        self.driver.find_element(By.XPATH,pim_added_employee).click()

    def click_emergency_contact(self):
        self.driver.find_element(By.XPATH, self.pim_emergency_contact_page_link_xpath).click()

    def click_emergency_contact_add_button(self):
        self.driver.find_element(By.XPATH, self.pim_emergency_add_button_xpath).click()

    def enter_emergency_contact_name(self, emergency_name):
        self.driver.find_element(By.XPATH, self.pim_emergency_name_text_box_xpath).send_keys(emergency_name)

    def enter_emergency_relationship_name(self, relationship):
        self.driver.find_element(By.XPATH, self.pim_emergency_relationship_text_box_xpath).send_keys(relationship)

    def click_save_button(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_emergency_save_button_xpath)))

