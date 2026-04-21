from logging import raiseExceptions

from openpyxl.styles.builtins import title
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.actions = ActionChains(self.driver)

    # locators
        self.title = (By.XPATH,"//h1[normalize-space()='SaanviTech CRM']")
        self.bussiness_email = (By.XPATH,"//input[@placeholder='Enter Email']")
        self.password = (By.XPATH,"//input[@placeholder='Enter Password']")
        self.login_btn = (By.XPATH,"//button[normalize-space()='Log In']")
        # self.title_home = (By.XPATH,"//h1[normalize-space()='SaanviTech Dashboard']")
        self.title_home = (By.XPATH,"//*[@id='root']/div/main/header")
        self.forgot_password = (By.XPATH,"//a[normalize-space()='Forgot Password?']")
        self.registered_email = (By.XPATH,"//input[@placeholder='name@company.com']")
        self.send_recovery_pulse = (By.XPATH,"//button[normalize-space()='Send Recovery Pulse']")
        self.return_to_login = (By.XPATH,"//a[normalize-space()='Return to Login Hub']")
        self.recoverypulse_sent = (By.XPATH,"//h3[normalize-space()='Recovery Pulse Sent!']")
        self.back_to_login = (By.XPATH,"//a[normalize-space()='Return to Login Hub']")

#     actions
    def verify_login(self,email,password):
        mail = self.wait.until(EC.visibility_of_element_located(self.bussiness_email))
        mail.clear()
        mail.send_keys(email)
        pswd = (self.driver.find_element(*self.password))
        pswd.clear()
        pswd.send_keys(password)
        self.driver.find_element(*self.login_btn).click()
        self.driver.implicitly_wait(10)
        # assert self.driver.find_element(self.title_home).is_displayed()

    def verify_return_to_login(self):
        fp = self.wait.until(EC.presence_of_element_located(self.forgot_password))
        fp.click()
        self.wait.until(EC.presence_of_element_located(self.return_to_login)).click()

    def verify_forgot_password(self,email):
        fp = self.wait.until(EC.presence_of_element_located(self.forgot_password))
        fp.click()
        rm = self.wait.until(EC.presence_of_element_located(self.registered_email))
        rm.send_keys(email)
        srp = self.wait.until(EC.presence_of_element_located(self.send_recovery_pulse))
        srp.click()
        self.wait.until(EC.presence_of_element_located(self.back_to_login)).click()
        # assert self.driver.find_element(self.title).is_displayed()























