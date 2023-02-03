from selenium.webdriver.common.by import By


class LoginPage:
    username_textbox_xpath = "//input[@name='username']"
    password_textbox_xpath = "//input[@name='password']"
    login_button_xpath = "//button[@type='submit']"
    show_error_message = "//p[text()='Invalid credentials']"
    login_assert_text_xpath = "//h6[text()='Dashboard']"

    def __init__(self, driver):
        self.driver = driver

    def enterUserName(self, userName):
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).send_keys(userName)

    def enterPassword(self, password):
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def getLoginAssetText(self):
        return self.driver.find_element(By.XPATH,self.login_assert_text_xpath).text

    def getErrorMessage(self):
        return self.driver.find_element(By.XPATH, self.show_error_message).text

