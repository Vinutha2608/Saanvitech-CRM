from CRM.pages.homedashboad_page import HomeDashboardPage
from CRM.utils.excel_reader import get_add_new_client


class TestAddNewClient:

    def setup_class(self,setup):
        self.driver = setup
        self.home = HomeDashboardPage(self.driver)

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