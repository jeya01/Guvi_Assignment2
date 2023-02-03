from selenium import webdriver
from selenium.webdriver.common.by import By

class PIMNewEmployeePageObjects:
    pim_menu_pim_xpath = "//span[text()='PIM']"
    pim_add_button_xpath = "//button[normalize-space()='Add']"
    firstname_textbox_xpath = "//input[@name='firstName']"
    lastname_textbox_xpath = "//input[@name='lastName']"
    create_login_check_box_xpath = "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']"
    create_new_username_xpath = "//label[normalize-space()='Username']/../following-sibling::div/input"
    create_new_password_xpath = "//label[normalize-space()='Password']/../following-sibling::div/input"
    confirm_password_path = "//label[normalize-space()='Confirm Password']/../following-sibling::div/input"
    status_enabled_radio_xpath = "//label[text()='Enabled']"
    save_button_xpath = "//button[normalize-space()='Save']"
    after_employee_creation = "//a[text()='Employee List']"


    def __init__(self, driver):
        self.driver = driver

    def click_pim(self):
        self.driver.find_element(By.XPATH, self.pim_menu_pim_xpath).click()

    def validate_pim_menu_item(self):
        pim_menu_item = self.driver.find_element(By.XPATH, self.pim_menu_pim_xpath)
        return pim_menu_item.text

    def click_add_button(self):
        self.driver.find_element(By.XPATH,self.pim_add_button_xpath).click()


    def enterFirstName(self, firstName):
        self.driver.find_element(By.XPATH, self.firstname_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.firstname_textbox_xpath).send_keys(firstName)


    def enterLastName(self, lastName):
        self.driver.find_element(By.XPATH, self.lastname_textbox_xpath).clear()
        # self.driver.find_element(By.XPATH, self.lastname_textbox_xpath).send_keys(Keys.CONTROL +'a',Keys.BACKSPACE)
        # to clear the text box
        self.driver.find_element(By.XPATH, self.lastname_textbox_xpath).send_keys(lastName)

    def click_create_login_check_box(self):
        self.driver.find_element(By.XPATH,self.create_login_check_box_xpath).click()


    def enter_new_username(self,username):
        self.driver.find_element(By.XPATH,self.create_new_username_xpath).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.XPATH, self.create_new_password_xpath).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(By.XPATH, self.confirm_password_path).send_keys(confirm_password)

    def select_enabled_status(self):
        self.driver.find_element(By.XPATH,self.status_enabled_radio_xpath).click()

    def click_save_button(self):
        self.driver.find_element(By.XPATH,self.save_button_xpath).click()

    def validate_after_new_employee_creation(self):
        return self.driver.find_element(By.XPATH,self.after_employee_creation).text





