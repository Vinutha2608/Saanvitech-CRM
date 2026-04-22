import time

import pytest

from CRM.pages.client_registry_page import ClientRegistryPage


class TestClientRegistry:
    @pytest.fixture(autouse=True)
    def setup_class(self,setup):
        self.driver = setup
        self.client = ClientRegistryPage(self.driver)

    @pytest.mark.usefixtures("login")
    def test_client_registry(self):
        self.client.click_client_registry()
        self.driver.implicitly_wait(25)

    def test_verify_search(self):
        keyword = "fhft"
        result = self.client.search_client(keyword)
        assert result==True




