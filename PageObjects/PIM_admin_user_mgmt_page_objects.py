from selenium import webdriver
from selenium.webdriver.common.by import By


class PIMMAdminUserManagementPageObjects:
    pim_menu_admin_xpath = "//span[text()='Admin']"
    pim_user_role_drop_down_arrow_xpath = "//label[text()='User Role']/../following-sibling::div/div/div/child::div[2]/i"
    pim_status_drop_down_arrow_xpath = "//label[text()='Status']/../following-sibling::div/div/div/child::div[2]/i"
    pim_user_role_drop_down_list_elements_xpath = "//label[text()='User Role']/../" \
                                         "following-sibling::div/div/child::div[@role='listbox']/div/span"
    pim_status_drop_down_list_elements_xpath = "//label[text()='Status']/.." \
                                      "/following-sibling::div/div/child::div[@role='listbox']/div/span"
    actual_user_role_elements = []
    actual_status_elements = []


    def __init__(self,driver):
        self.driver = driver

    def validate_admin_menu_option(self):
        admin_text = self.driver.find_element(By.XPATH, self.pim_menu_admin_xpath)
        return admin_text.text


    def click_admin_menu(self):
        self.driver.find_element(By.XPATH,self.pim_menu_admin_xpath).click()

    def click_user_role(self):
        self.driver.find_element(By.XPATH,self.pim_user_role_drop_down_arrow_xpath).click()

    def get_acutal_user_role_items(self):
        user_role_elements = self.driver.find_elements(By.XPATH, self.pim_user_role_drop_down_list_elements_xpath)
        for user_role in user_role_elements:
            self.actual_user_role_elements.append(user_role.text)
        return self.actual_user_role_elements

    def click_status(self):
        self.driver.find_element(By.XPATH,self.pim_status_drop_down_arrow_xpath).click()

    def get_acutal_status_items(self):
        status_elements = self.driver.find_elements(By.XPATH, self.pim_status_drop_down_list_elements_xpath)
        for status in status_elements:
            self.actual_status_elements.append(status.text)
        return self.actual_status_elements
