from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from CRM.pages.login_page import LoginPage


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(self.driver)
        self.lp = LoginPage(driver)

        self.signup = (By.XPATH,"//button[@class='auth-toggle-btn']")
        self.full_name = (By.XPATH,"//input[@placeholder='Enter your name']")
        self.bemail = (By.XPATH,"//input[@placeholder='name@company.com']")
        self.pword = (By.XPATH,"//input[@placeholder='••••••••']")
        self.create_acct = (By.XPATH,"//button[normalize-space()='Create Account']")
        self.back_to_login = (By.XPATH,"//button[normalize-space()='Already have an account? Log in']")

    def verify_signup(self,fullname,email,password):
        click_signup = self.wait.until(EC.visibility_of_element_located(self.signup))
        click_signup.click()
        fname = self.wait.until(EC.presence_of_element_located(self.full_name))
        fname.send_keys(fullname)
        mail = self.wait.until(EC.presence_of_element_located(self.bemail))
        mail.send_keys(email)
        passkey = self.wait.until(EC.presence_of_element_located(self.pword))
        passkey.send_keys(password)
        self.wait.until(EC.presence_of_element_located(self.create_acct)).click()
        assert self.driver.find_element(self.lp.title_home).is_displayed()



    def verify_back_to_login(self):
        click_signup = self.wait.until(EC.visibility_of_element_located(self.signup))
        click_signup.click()
        self.wait.until(EC.presence_of_element_located(self.back_to_login)).click()



