import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import *

def TestProject():
    os.environ['WDM_SSL_VERIFY'] = '0'
    option = webdriver.ChromeOptions()
    option.add_argument('--no-sandbox')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)
    driver.implicitly_wait(5)
    driver.maximize_window()
    url = "https://practicetestautomation.com/practice-test-login"
    driver.get(url)

# Test Case 01 - Successful Login

    username = 'student'
    password = 'Password123'
    driver.find_element(By.ID, 'username').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'submit').click()

    try:
        driver.find_element(By.XPATH, '//h1[text()="Logged In Successfully"]')
        print('Successful Login')
    except NoSuchElementException:
        print('User not able to login')
    driver.find_element(By.XPATH, '//a[text()="Log out"]').click()
    driver.implicitly_wait(5)

# Test Case 02 - Incorrect Username

    username = 'incorrectUser'
    password = 'Password123'
    driver.find_element(By.ID, 'username').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'submit').click()

    try:
        driver.find_element(By.XPATH, '//div[text()="Your username is invalid!"]')
        print('Incorrect Username')
    except NoSuchElementException:
        print('User was able to login with an incorrect username.')

# Test Case 03 - Incorrect Username

    username = 'student'
    password = 'incorrectPassword'
    driver.find_element(By.ID, 'username').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'submit').click()

    try:
        driver.find_element(By.XPATH, '//div[text()="Your password is invalid!"]')
        print('Incorrect Password')
    except NoSuchElementException:
        print('User was able to login with an incorrect password.')

if __name__ == '__main__':
    TestProject()

