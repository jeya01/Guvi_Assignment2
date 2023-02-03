import time

from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PimSearchBoxPageObjects:
    pim_search_box_xpath = "//input[@placeholder='Search']"
    pim_menu_elements_xpath = "//ul[@class='oxd-main-menu']/li/a/span"
    pim_actual_menu_list = []


    def __init__(self,driver):
        self.driver = driver

    def search_box_presence(self):
        return EC.presence_of_element_located((By.XPATH,self.pim_search_box_xpath))
        #'''returns locator'''
        #return self.driver.find_element(By.XPATH,self.pim_search_box_xpath).is_displayed() '''returns boolen'''

    def get_actual_menu_items(self):
        pim_menu_elements = self.driver.find_elements(By.XPATH, self.pim_menu_elements_xpath)
        for item in pim_menu_elements:
            self.pim_actual_menu_list.append(item.text)
        return self.pim_actual_menu_list

    def menu_item_search(self,menu_item):
        self.driver.find_element(By.XPATH,self.pim_search_box_xpath).send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH,self.pim_search_box_xpath).send_keys(menu_item)

