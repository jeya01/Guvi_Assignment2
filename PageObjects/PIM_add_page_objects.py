import os

import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import autoit


class PimAddNewEmployeeObjects:
    pim_link_xpath = "//span[text()='PIM']"
    firstname_textbox_xpath = "//input[@name='firstName']"
    lastname_textbox_xpath = "//input[@name='lastName']"
    add_button_xpath = "//button[normalize-space()='Add']"
    photo_upload_button_xpath = "//div[@class='employee-image-wrapper']/../button/i"

    def __init__(self, driver):
        self.driver = driver

    def clickPIM(self):
        self.driver.find_element(By.XPATH, self.pim_link_xpath).click()

    def clickAdd(self):
        self.driver.find_element(By.XPATH, self.add_button_xpath).click()

    def enterFirstName(self, firstName):
        self.driver.find_element(By.XPATH, self.firstname_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.firstname_textbox_xpath).send_keys(firstName)

    def enterLastName(self, lastName):
        self.driver.find_element(By.XPATH, self.lastname_textbox_xpath).clear()
        # self.driver.find_element(By.XPATH, self.lastname_textbox_xpath).send_keys(Keys.CONTROL +'a',Keys.BACKSPACE)
        # to clear the text box
        self.driver.find_element(By.XPATH, self.lastname_textbox_xpath).send_keys(lastName)

    def uploadPhoto(self):
        self.driver.find_element(By.XPATH, self.photo_upload_button_xpath).click()
        time.sleep(5)
        os.startfile("C:\\Users\\jeyalakshmi\\OneDrive\\Desktop\\upload_img.exe")
        #autoit.run("C:\\Users\\jeyalakshmi\\OneDrive\\Desktop\\upload_img.exe")
        time.sleep(10)

    def clickSave(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
