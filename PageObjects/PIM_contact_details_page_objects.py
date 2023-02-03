from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PIMContactDetailsPageObjects:
    pim_link_xpath = "//span[text()='PIM']"
    pim_employee_info_menu_list_xpath = "//div[@role='tab']"
    pim_contact_page_link_xpath = "//div[@role='tab']/a[text()='Contact Details']"
    pim_contact_steet1_text_xpath = "//label[text()='Street 1']/../following-sibling::div/input"
    pim_contact_city_text_xpath = "//label[text()='City']/../following-sibling::div/input"
    pim_contact_mobile_text_xpath = "//label[text()='Mobile']/../following-sibling::div/input"
    pim_save_button_xpath = "//div[@class='orangehrm-edit-employee']/div[2]/div[1]/form[@class='oxd-form']" \
                            "/div[@class='oxd-form-row']/../div[@class='oxd-form-actions']/button[@type='submit']"




    def __init__(self, driver):
        self.driver = driver

    def clickPIM(self):
        self.driver.find_element(By.XPATH, self.pim_link_xpath).click()

    def click_added_employee(self,emp_id):
        pim_added_employee = "//div[@role='table']//div[contains(text()," + emp_id + ")]" \
                                                                    "/../following-sibling::div[7]/div/button[2]/i"
        self.driver.find_element(By.XPATH,pim_added_employee).click()


    def click_contact_details(self):
        self.driver.find_element(By.XPATH, self.pim_contact_page_link_xpath).click()

    def enter_street1(self, street):
        self.driver.find_element(By.XPATH, self.pim_contact_steet1_text_xpath).click()
        self.driver.find_element(By.XPATH, self.pim_contact_steet1_text_xpath).send_keys(street)

    def enter_city(self, city):
        self.driver.find_element(By.XPATH, self.pim_contact_city_text_xpath).click()
        self.driver.find_element(By.XPATH, self.pim_contact_city_text_xpath).send_keys(city)

    def enter_mobile(self, mobile):
        self.driver.find_element(By.XPATH, self.pim_contact_mobile_text_xpath).click()
        self.driver.find_element(By.XPATH, self.pim_contact_mobile_text_xpath).send_keys(mobile)


    def clickSaveButton(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_save_button_xpath)))
