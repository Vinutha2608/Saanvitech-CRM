from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ClientRegistryPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

        self.clients = (By.XPATH, "//a[@class='nav-item ' and @href='/clients']")
        self.search = (By.XPATH,"//input[@placeholder='Search by name or PAN...']")
        self.result = (By.XPATH,"//div[@class='clients-grid']")

    def click_client_registry(self):
        client_registry_btn = self.wait.until(EC.element_to_be_clickable(self.clients))
        client_registry_btn.click()
        title = self.driver.current_url
        assert "clients" in title

    def search_client(self,keyword):
        element = self.wait.until(EC.element_to_be_clickable(self.search))
        element.clear()
        element.send_keys(keyword)
        keyword = keyword.lower()
        # 🔥 wait until text updates
        self.wait.until(
            lambda d: keyword in self.driver.find_element(*self.result).text.lower()
                      or "no" in self.driver.find_element(*self.result).text.lower()
        )

        text = self.driver.find_element(*self.result).text.strip().lower()
        if keyword in text:
            print("Client found:", text)
            return True
        else:
            print("No client found:", text)
            return False

