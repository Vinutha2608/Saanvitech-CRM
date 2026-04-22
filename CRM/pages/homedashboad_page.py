import re
from tkinter import Listbox
from tkinter.constants import SEL_LAST

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

        self.total_clients = (By.XPATH,"//div[contains(@class,'stats-grid')]//div[1]//div[2]")
        self.toast =(By.XPATH,"//div[@class='snackbar-item success animate-slide-in']")

        self.loader = (By.CLASS_NAME,"loading-spinner")
    #     sync-overlay
        self.document_count = (By.XPATH,"//div[contains(@class,'stats-grid')]//div[2]//div[2]")

        self.global_search = (By.XPATH,"//input[@placeholder='Quick search: PAN, Client, or File Name...']")
        self.search_result = (By.XPATH,"//div[@class='search-results-dropdown glass-panel animate-fade-in']")

        self.navigation_bar = (By.XPATH,"//header[@class='top-header glass-panel']//button[@class='icon-btn mobile-toggle']//*[name()='svg']")
        self.nav_item = (By.XPATH,"//nav[@class='sidebar-nav']")

        self.whatsapp_link = (By.XPATH,"//a[@class='nav-item ' and @href='/whatsapp-link']")



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
        self.wait.until(EC.visibility_of_element_located(self.wtsp_num)).send_keys(str(whstapp_no))
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

    def get_total_clients(self):
        count = self.wait.until(EC.visibility_of_element_located(self.total_clients)).text.strip()
        number = int(re.search(r"\d+", count).group())
        return number

    def get_table_row_count(self):
        rows = self.driver.find_elements(By.XPATH, "//table//tbody/tr")
        return len(rows)

        # CLICK SYNC + WAIT

    def click_sync_gmail(self):
        self.wait.until(EC.element_to_be_clickable(self.sync_gmail)).click()

        # Wait for loader (if appears)
        try:
            self.wait.until(EC.presence_of_element_located(self.loader))
            self.wait.until(EC.invisibility_of_element_located(self.loader))
        except:
            print("Loader not found, continuing...")

        # GET ALERT MESSAGE

    def get_sync_message(self):
        alert = self.wait.until(EC.alert_is_present())
        msg = alert.text
        alert.accept()
        return msg


        # EXTRACT ATTACHMENT COUNT

    def extract_attachment_count(self, msg):
        match = re.search(r"\d+", msg)
        return int(match.group()) if match else 0


        # GET DOCUMENT COUNT

    def get_documents_count(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.document_count)
        ).text.strip()

    def search_and_validate(self,keyword):
        search = self.wait.until(EC.visibility_of_element_located(self.global_search))
        search.clear()
        search.send_keys(keyword)
        self.driver.implicitly_wait(5)
        result = self.wait.until(EC.presence_of_element_located(self.search_result))
        text = result.text.strip().lower()
        keyword = keyword.lower()
        if keyword in text:
            print(" Client found:",text)
            return True
        else:
            print("No client found:",text)
            return False

    def click_navbar(self):
        nav = self.wait.until(EC.presence_of_element_located(self.navigation_bar))
        nav.click()

    def check_nav_item(self):
        items = self.driver.find_elements(*self.nav_item)
        nav_list = []
        for item in items:
            text = item.text.strip()
            if text:
                nav_list.extend(text.split("\n"))
        return nav_list






        



