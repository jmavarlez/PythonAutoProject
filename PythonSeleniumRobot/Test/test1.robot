*** Settings ***
Documentation    To Validate SauceDemo Login
Library    SeleniumLibrary
#Resource

*** Test Cases ***
TC01 Valid Login
    Open Browser and enter URL
    Login SauceDemo
    Verify HomePage


*** Keywords ***
Open Browser and enter URL
    Create Webdriver    Chrome
    Go To    https://www.saucedemo.com/
    
Login SauceDemo
    Input Text    //input[@id='user-name']    standard_user
    Input Text    //input[@id='password']    secret_sauce
    Click Button    //input[@id='login-button']

Verify HomePage
    Wait Until Element Is Not Visible    //h3[contains(text(),'Username and password do not match')]
