*** Settings ***
Documentation    To Validate SauceDemo Login\
Library    ../../keywords/SetupAndTeardown.py
Library    ../../keywords/ElementHandler.py
Test Setup    SetupAndTeardown.Setup    https://www.saucedemo.com/


*** Test Cases ***
TC01 Valid Login
    SetupAndTeardown.openURL    https://www.saucedemo.com/
    ElementActions.input_text    //input[@id='user-name']    username


*** Keywords ***