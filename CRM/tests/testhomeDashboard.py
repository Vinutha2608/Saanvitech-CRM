import time
import pytest

from CRM.pages.homedashboad_page import HomeDashboardPage
from CRM.utils.excel_reader import get_excel_data


class TestHomeDashboard:

    @pytest.fixture(autouse=True)
    def setup_class(self,setup):
        self.driver = setup
        self.home = HomeDashboardPage(self.driver)

    @pytest.mark.usefixtures("login")
    def test_homedashboard(self):
        self.home.click_homedashboard()

        # self.home.handle_change_password_popup()

    def _verify_add_client(self):
        data = get_excel_data("add_client")[0]
        # client_logo = data[1]
        client_name = data[2]
        PAN_NO = data[3]
        email_add = data[4]
        whatsapp_no = data[5]
        whatsapp_group = data[6]

        self.home.add_new_client(client_name,PAN_NO,email_add,whatsapp_no,whatsapp_group)
        time.sleep(4)

    def test_cancel_and_cross_btn(self):
        self.home.verify_cross_cancel_btn()
















