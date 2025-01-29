*** Settings ***
Documentation    To Validate SauceDemo Login
Library    ../../keywords/SetupAndTeardown.py
Library    ../../pageobject/SauceDemo/LoginPage.py
Test Setup    SetupAndTeardown.Setup    https://www.saucedemo.com/


*** Test Cases ***
TC01 Valid Login
    LoginPage.input_username    standard_user
    LoginPage.input_password    secret_sauce
*** Keywords ***