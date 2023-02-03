import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMDependentsPageObjects:
    pim_link_xpath = "//span[text()='PIM']"
    pim_dependents_link_path = "//div[@role='tab']/a[text()='Dependents']"
    pim_dependents_add_button_xpath = "//div[@class='orangehrm-edit-employee-content']/div/div/button"
    pim_dependents_name_text_box_xpath = "//label[text()='Name']/../following-sibling::div/input"
    pim_dependents_relationship_dropdown_path = "//label[text()='Relationship']/../" \
                                                "following-sibling::div/div/div/div[2]/i"
    pim_dependents_dropdown_elements = "//div[@role='listbox']/div/span"
    pim_dependents_save_button_xpath = "//div[@class='orangehrm-edit-employee']/div[2]/div[1]/form[@class='oxd-form']" \
                                      "/div[@class='oxd-form-row']/../div[@class='oxd-form-actions']/button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def clickPIM(self):
        self.driver.find_element(By.XPATH, self.pim_link_xpath).click()

    def click_dependents(self):
        self.driver.find_element(By.XPATH, self.pim_dependents_link_path).click()

    def click_added_employee(self,emp_id):
        pim_added_employee = "//div[@role='table']//div[contains(text()," + emp_id + ")]" \
                                                                    "/../following-sibling::div[7]/div/button[2]/i"
        self.driver.find_element(By.XPATH,pim_added_employee).click()

    def click_dependents_add_button(self):
        self.driver.find_element(By.XPATH, self.pim_dependents_add_button_xpath).click()

    def enter_dependents_name(self, dependents_name):
        self.driver.find_element(By.XPATH, self.pim_dependents_name_text_box_xpath).send_keys(dependents_name)



    def select_dependents_relationship(self, relationship_status):


        self.driver.find_element(By.XPATH, self.pim_dependents_relationship_dropdown_path).click()
        #relationship_elements = self.driver.find_elements(By.XPATH, self.pim_dependents_dropdown_elements)
        wait = WebDriverWait(self.driver, 10)
        relationship_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, self.pim_dependents_dropdown_elements)))
        for relation in relationship_elements:
            if relation.text == relationship_status:
                wait.until(EC.element_to_be_clickable(relation))


    def click_save_button(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_dependents_save_button_xpath)))
