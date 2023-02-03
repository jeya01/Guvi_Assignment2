import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PimEditEmployeePage:
    pim_link_xpath = "//span[text()='PIM']"

    pim_edit_license_expiry_date_xpath = "//label[text()='License Expiry Date']/../../div/child::div/div/input"

    edit_license_month_dropdown_xpath = "//div[@class='oxd-calendar-selector-month-selected']/i"
    edit_license_month_list_xpath = "//ul[@class='oxd-calendar-dropdown']/li"

    edit_license_year_list_xpath = "//ul[@class='oxd-calendar-dropdown']/li[@class='oxd-calendar-dropdown--option']"
    edit_license_year_dropdown_xpath = "//div[@class='oxd-calendar-selector-year-selected']/i"

    edit_license_date_table_xpath = "//div[@class='oxd-calendar-date']"

    pim_save_button_xpath = "//div[@class='orangehrm-edit-employee']/div[2]/div[1]/form[@class='oxd-form']/div[@class='oxd-form-row']/../div[@class='oxd-form-actions']/button[@type='submit']"

    '''
    to click the date icon
    //div[@class='orangehrm-background-container']/child::div/div[@class='orangehrm-edit-employee']/div[2]/div[1]/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[2]/div[2]/child::div/div[2]/div[@class='oxd-date-wrapper']/div/input
    
    '''

    def __init__(self, driver):
        self.driver = driver

    def clickPIM(self):
        self.driver.find_element(By.XPATH, self.pim_link_xpath).click()

    def clickEditPencil(self):
        pim_emp_id = "0217"
        pim_edit_pencil_button_xpath = "//div[@role='table']//div[contains(text()," + pim_emp_id + ")]" \
                                        "/../following-sibling::div[7]/div/button[2]/i"
        self.driver.find_element(By.XPATH, pim_edit_pencil_button_xpath).click()

    def clickEditDate(self, license_year, license_month, license_date):
        self.driver.find_element(By.XPATH, self.pim_edit_license_expiry_date_xpath).click()

        year_dropdown = self.driver.find_element(By.XPATH, self.edit_license_year_dropdown_xpath)
        year_dropdown.click()
        year_list = self.driver.find_elements(By.XPATH, self.edit_license_year_list_xpath)
        for year in year_list:
            if year.text == license_year:
                year.click()
                break

        month_dropdown = self.driver.find_element(By.XPATH, self.edit_license_month_dropdown_xpath)
        month_dropdown.click()
        month_list = self.driver.find_elements(By.XPATH, self.edit_license_month_list_xpath)
        for month in month_list:
            if month.text == license_month:
                month.click()
                break

        date_list = self.driver.find_elements(By.XPATH, self.edit_license_date_table_xpath)
        for dates in date_list:
            if dates.text == license_date:
                dates.click()
                break


    def clickSaveButton(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_save_button_xpath)))
