from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# class EmailInstructionPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#         self.actions = ActionChains(self.driver)
#
#
#         self.email_instrt_link = (By.XPATH,"//a[@href='/email-link']")
#         self.no_email_linked_status = (By.XPATH,"//span[@class='text-danger']")
#         self.gmail_address = (By.XPATH,"//input[@placeholder='your-email@gmail.com']")
#         self.app_password = (By.XPATH,"//input[@placeholder='xxxx xxxx xxxx xxxx']")
#         self.update_instr_link_btn = (By.XPATH,"//button[@type='submit']")
#         self.email_active = (By.XPATH,"//button[@type='submit']")
#
#     def email_email_instruction_link(self):
#         email_module = self.driver.wait.until(EC.visibility_of_element_located(self.email_instrt_link))
#         email_module.click()
#
#     def check_status_connection(self,gmail,apppassword):
#         # status = "No Email Linked"
#         status = self.driver.find_element(self.no_email_linked_status).text.strip()
#         if status == "No Email Linked":
#             self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             gmail_field = self.driver.wait.until(EC.presence_of_element_located(self.gmail_address))
#             gmail_field.clear()
#             gmail_field.send_keys(gmail)
#             password_field = (self.driver.find_element(self.app_password))
#             password_field.clear()
#             password_field.send_keys(apppassword)
#             self.driver.find_element(self.update_instr_link_btn).click()
#
#
#
#
#
#
#
#
#
#
#
#
#

class EmailInstructionPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(self.driver)
        self.email_instrt_link = (By.XPATH,"//a[@href='/email-link']")
        self.no_email_linked_status = (By.XPATH,"//span[@class='text-danger']")
        self.gmail_address = (By.XPATH,"//input[@placeholder='your-email@gmail.com']")
        self.app_password = (By.XPATH,"//input[@placeholder='xxxx xxxx xxxx xxxx']")
        self.update_instr_link_btn = (By.XPATH,"//button[@type='submit']")
        self.email_active = (By.XPATH,"//h1[normalize-space()='Email Link is Active']")

    def email_instruction_link(self):
        email_module = self.wait.until(
            EC.visibility_of_element_located(self.email_instrt_link)
        )
        email_module.click()

    def check_status_connection(self, gmail, apppassword):
        # status = self.driver.find_element(*self.no_email_linked_status).text.strip()
        #
        # if status == "No Email Linked":
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        gmail_field = self.wait.until(
                EC.presence_of_element_located(self.gmail_address)
            )
        gmail_field.clear()
        gmail_field.send_keys(gmail)
        password_field = self.driver.find_element(*self.app_password)
        password_field.clear()
        password_field.send_keys(apppassword)
        self.driver.find_element(*self.update_instr_link_btn).click()

    def check_status_isactive(self):
        self.driver.execute_script("window.scrollTo(0,0);")
        checkstatus = self.wait.until(EC.presence_of_element_located(self.email_active))
        active = checkstatus.text.strip()
        # driver.find_element(*self.email_active).text.strip()
        assert "Active" in active