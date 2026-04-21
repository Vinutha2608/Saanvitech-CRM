import pytest
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver
import os
from CRM.conftest import setup
from CRM.pages.login_page import LoginPage
from CRM.utils.excel_reader import get_excel_data


class TestLogin:

    @pytest.mark.parametrize("bussiness_email,password",[
        ("xyz","ghj"),
        ("fghj",""),
        ("","klop"),
        ("",""),
        ("test1@gmail.com", "Test@123"),
    ])

    def test_login(self,setup,bussiness_email, password):
        driver = setup
        lp = LoginPage(driver)
        lp.verify_login(bussiness_email,password)
        driver.implicitly_wait(30)


    def test_return_to_login(self,setup):
        driver = setup
        lp = LoginPage(driver)
        lp.verify_return_to_login()

    def test_verify_forgotpassword(self,setup):
        email = "vinuthaacharya26@gmail.com"
        driver = setup
        lp = LoginPage(driver)
        lp.verify_forgot_password(email)

















