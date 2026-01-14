import time

import pytest
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib3 import response
from webdriver_manager.core import driver


@pytest.mark.usefixtures("driver")
class TestWebSite:
    def test_main(self):
        driver.get("https://automationexercise.com/")
        response = requests.get("https://automationexercise.com/")
        assert response.status_code == 200, f"Site açılamadı! Status kod: {response.status_code}"
        # COMPLATED URL VERİFİCATİON

      # REGİSTER VERİFİCATİON
@pytest.mark.usefixtures("driver")
class Test_sign_in:
    def test_sign_in(self):
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]').click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, 'input[data-qa="signup-name"]').send_keys("Alpay Demircioğlu")
        self.driver.find_element(By.CSS_SELECTOR, 'input[data-qa="signup-email"]').send_keys("testlessons1@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, 'button[data-qa="signup-button"]').click()
        time.sleep(3)
        self.driver.find_element(By.ID, "id_gender1").click()
        self.driver.find_element(By.ID, "password").send_keys("testTEST34")
        self.driver.find_element(By.ID, "days").send_keys("12")
        self.driver.find_element(By.ID, "months").send_keys("May")
        self.driver.find_element(By.ID, "years").send_keys("1998")
        element = self.driver.find_element(By.ID,"first_name")
        self.driver.execute_script("arguments[0].scrollIntoView(true);" , element )
        element.send_keys("Alpay")
        self.driver.find_element(By.ID,"last_name").send_keys("Demircioğlu")
        self.driver.find_element(By.ID,"company").send_keys("NonCompany")
        self.driver.find_element(By.ID,"address1").send_keys("TURKEY xxxxxxxxxxxxxx")
        self.driver.find_element(By.ID, "address2").send_keys("TURKEY xxxxxxxxxxxxxx")
        self.driver.find_element(By.ID,"country").send_keys("Singapore")
        self.driver.find_element(By.ID,"state").send_keys("XXXXX")
        self.driver.find_element(By.ID, "city").send_keys("XXXXX")
        self.driver.find_element(By.ID, "zipcode").send_keys("010101")
        self.driver.find_element(By.ID,"mobile_number").send_keys("00000000000")
        self.driver.find_element(By.CSS_SELECTOR,'button[data-qa="create-account"]').click()




