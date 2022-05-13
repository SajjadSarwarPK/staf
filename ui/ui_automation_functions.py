import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UiTesting:

    def __init__(self):
        self.check = ''
        self.response = ''

    def define_chrome_driver(self):

        driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\staf\\browsers\\chromedriver.exe')

        print("hello")
        return driver

    def navigateto(self, url):
        self.driver = self.define_chrome_driver()
        self.driver.get("https://www.google.com")
        self.driver.maximize_window()
        # WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "q")))
        return True
        # search = driver.find_element_by_name('q')

    def verify_string(self, keyword):
        string = self.driver.find_element_by_xpath("//div[@id='SIvCob']").text
        print(string)
        if keyword in string:
            print("==============Following String Found==============")
            print(keyword)
            return True
        else:
            return False

    def close_driver(self):
        self.driver.quit()
        return True
