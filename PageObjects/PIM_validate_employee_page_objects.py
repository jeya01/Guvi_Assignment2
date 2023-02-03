from selenium import webdriver
from selenium.webdriver.common.by import By


class PIMValidateEmployeePageObjects:
    pim_link_xpath = "//span[text()='PIM']"
    pim_employee_info_menu_list_xpath = "//div[@role='tab']"


    def __init__(self, driver):
        self.driver = driver

    def clickPIM(self):
        self.driver.find_element(By.XPATH, self.pim_link_xpath).click()

    def click_added_employee(self,emp_id):
        pim_added_employee = "//div[@role='table']//div[contains(text()," + emp_id + ")]" \
                                                                    "/../following-sibling::div[7]/div/button[2]/i"
        self.driver.find_element(By.XPATH,pim_added_employee).click()

    def get_emp_info_menu(self):
        emp_info_menu_elements = self.driver.find_elements(By.XPATH,self.pim_employee_info_menu_list_xpath)
        menu_elements= []

        for item in emp_info_menu_elements:
            menu_elements.append(item.text)

        return menu_elements
