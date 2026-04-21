import pytest

from CRM.pages.email_instruction_link_page import EmailInstructionPage
from CRM.utils.excel_reader import get_excel_data


class TestEmailInstructionLink:

    @pytest.fixture(autouse=True)
    def setup_class(self, setup):
        self.driver = setup
        self.emp = EmailInstructionPage(self.driver)

    @pytest.mark.usefixtures("login")
    def test_get_email_instruction_link(self):
        self.emp.email_instruction_link()

    # @pytest.mark.usefixtures("login")
    @pytest.mark.parametrize("gmail,apppassword", get_excel_data("email_connect"))
    def test_connect_email(self, gmail, apppassword):
        self.emp.email_instruction_link()   # 👈 navigation
        self.emp.check_status_connection(gmail, apppassword)
        self.emp.check_status_isactive()

    def test_verify_status_is_active(self):
        self.emp.check_status_isactive()








