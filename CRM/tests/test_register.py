import time

import pytest

from CRM.pages.register_page import RegisterPage


class TestRegister:
    def test_verify_back_to_login_click(self,setup):
        self.driver = setup
        self.rp = RegisterPage(self.driver)
        self.rp.verify_back_to_login()


    @pytest.mark.parametrize("fname,email,password",
                             [
                                 ("", "", ""),
                              ("ghj","","123"),
                              ("jjk","gdg","uio"),
                              ("xyz","xyz@gmail.com","Test@123")
                              ])
    def test_verify_signup(self,setup,fname,email,password):
        self.driver = setup
        self.rp = RegisterPage(self.driver)
        self.rp.verify_signup(fname,email,password)
        time.sleep(2000)


