import time
import pytest

from CRM.pages.homedashboad_page import HomeDashboardPage
from CRM.utils.excel_reader import get_excel_data, get_add_new_client


class TestHomeDashboard:

    @pytest.fixture(autouse=True)
    def setup_class(self,setup):
        self.driver = setup
        self.home = HomeDashboardPage(self.driver)

    @pytest.mark.usefixtures("login")
    def test_homedashboard(self):
        self.home.click_homedashboard()
        # self.home.handle_change_password_popup()

    def test_navigation_bar_items(self):
        Expected_items = ["Home Dashboard","Client Registry","WhatsApp Link","Email Instruction Link"]
        actual_items = self.home.check_nav_item()
        for item in Expected_items:
            assert item in actual_items,f"{item} is missing"

    def test_verify_add_new_client(self):
        row = get_add_new_client("add_client")
        assert row is not None, "No testdata with NO Status found"
        client_name = row["client_name"]
        PAN_NO = row["PAN_NO"]
        email_add = row["email_add"]
        whatsapp_no = str(row["whatsapp_no"])
        whatsapp_group = row["whatsapp_group"]
        # 👉 BEFORE state
        before_count = self.home.get_total_clients()
        before_rows = self.home.get_table_row_count()
        # 👉 Action
        self.home.add_new_client(client_name, PAN_NO, email_add, whatsapp_no, whatsapp_group)
        # 🔥 WAIT for BOTH updates (VERY IMPORTANT)
        self.home.wait.until(
            lambda d: self.home.get_table_row_count() == before_rows + 1
        )
        self.home.wait.until(
            lambda d: self.home.get_total_clients() == before_count + 1
        )
        # 👉 AFTER state
        after_count = self.home.get_total_clients()
        after_rows = self.home.get_table_row_count()
        # 👉 VALIDATIONS
        assert after_count == before_count + 1, "Total client count not increased"
        assert after_rows == before_rows + 1, "Table row count not increased"

    def test_cancel_and_cross_btn(self):
        self.home.verify_cross_cancel_btn()

    def test_sync_gmail(self):
        before_docs = self.home.get_documents_count()
        self.home.click_sync_gmail()
        msg = self.home.get_sync_message()
        attachment_count = self.home.extract_attachment_count(msg)
        if attachment_count > 0:
            self.home.wait.until(
                lambda d: self.home.get_documents_count() == before_docs + 1
            )
        else:
            self.home.wait.until(
                lambda d: self.home.get_documents_count() == before_docs
            )
        after_docs = self.home.get_documents_count()
        if attachment_count > 0:
            assert after_docs == before_docs + 1, "Docs should increase by 1"
        else:
            assert after_docs == before_docs, "Docs should not change"

    def test_global_serach(self):
        keyword = "Vinu"
        result = self.home.search_and_validate(keyword)
        assert result == True























