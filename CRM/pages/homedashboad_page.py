from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomeDashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(self.driver)

        self.home_db_btn = (By.XPATH,"//a[@class='nav-item active']")
        self.db_title = (By.XPATH,"//h1[normalize-space()='SaanviTech Dashboard']")
        self.search = (By.XPATH,"//input[@placeholder='Quick search: PAN, Client, or File Name...']")

        self.client_logo = (By.XPATH,"//label[@class='logo-upload-zone']//*[name()='svg']")
        self.client_name = (By.XPATH,"//input[@placeholder='e.g. Acme Corp']")
        self.pan_num = (By.XPATH,"//input[@placeholder='e.g. ABCDE1234F']")
        self.email_address = (By.XPATH,"//input[@placeholder='e.g. client@email.com']")
        self.wtsp_num = (By.XPATH,"//input[@placeholder='10-digit mobile']")
        self.wtsp_group = (By.XPATH,"//input[@placeholder='e.g. Sanvi Group']")
        self.add_client = (By.XPATH,"//button[normalize-space()='Add Client']")
        self.cross_btn = (By.XPATH,"//button[@class='icon-btn']//*[name()='svg']")
        self.cancel_btn = (By.XPATH,"//button[normalize-space()='Cancel']")
        self.sync_gmail = (By.XPATH,"//button[normalize-space()='Sync Gmail']")
        self.new_client = (By.XPATH,"//button[normalize-space()='New Client']")

        self.ok_btn = (By.XPATH, "//button[contains(text(),'OK') or contains(text(),'Ok')]")
        self.modal_overlay = (By.CLASS_NAME, "modal-overlay")

    def click_homedashboard(self):
        self.handle_popup()
        home_db = (self.wait.until(EC.visibility_of_element_located(self.home_db_btn)))
        home_db.click()
        self.driver.implicitly_wait(2)

    def add_new_client(self,  clientname, pan_no, email, whstapp_no, whstapp_grp):
        self.handle_popup()

        self.wait.until(EC.element_to_be_clickable(self.new_client)).click()

        # print("Logo path:", logo)

        # # 🔥 HANDLE FILE UPLOAD CORRECTLY
        # upload = self.wait.until(EC.presence_of_element_located(self.client_logo))
        #
        # # If hidden → make visible
        # self.driver.execute_script("arguments[0].style.display='block';", upload)
        #
        # upload.send_keys(logo)

        # 🔥 Fill form (FIXED *)
        self.wait.until(EC.visibility_of_element_located(self.client_name)).send_keys(clientname)
        self.wait.until(EC.visibility_of_element_located(self.pan_num)).send_keys(pan_no)
        self.wait.until(EC.visibility_of_element_located(self.email_address)).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(self.wtsp_num)).send_keys(whstapp_no)
        self.wait.until(EC.visibility_of_element_located(self.wtsp_group)).send_keys(whstapp_grp)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait.until(EC.element_to_be_clickable(self.add_client)).click()

    def verify_cross_cancel_btn(self):
        new_cleint_btn = (self.wait.until(EC.presence_of_element_located(self.new_client)))
        new_cleint_btn.click()
        self.driver.implicitly_wait(10)
        self.driver.execute_script("window.scrollTo(0,0);")
        cross_button = self.wait.until(EC.element_to_be_clickable(self.cross_btn))
        cross_button.click()
        self.driver.implicitly_wait(3)
        new_cleint_btn = (self.wait.until(EC.presence_of_element_located(self.new_client)))
        new_cleint_btn.click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        self.wait.until(EC.presence_of_element_located(self.cancel_btn)).click()

    def check_sync_gmail(self):
        sync = self.driver.wait_until(EC.element_to_be_clickable(self.sync_gmail))
        sync.click()

    def handle_popup(self):
        try:
            popups = self.driver.find_elements(By.XPATH, "//div[contains(@class,'modal-overlay')]")
            if popups and popups[0].is_displayed():
                ok_btn = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK' or normalize-space()='Ok']"))
                )
                ok_btn.click()
                WebDriverWait(self.driver, 5).until(
                    EC.invisibility_of_element_located((By.XPATH, "//div[contains(@class,'modal-overlay')]"))
                )
        except Exception as e:
            print("Popup not handled:", e)


        



