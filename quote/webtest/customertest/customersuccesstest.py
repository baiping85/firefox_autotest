import unittest

from quote.base.usebrowser import UseBrowser
from quote.db.customer.customeroperation import DbCustomerOp
from quote.page.customerpage import CustomerPage


class CustomerSuccCase(unittest.TestCase):

    # def set_up(self):
    #     self.ub = UseBrowser()
    #     self.customerpage = CustomerPage()

    def setUp(self) -> None:
        self.db_customer = DbCustomerOp()
        self.ub = UseBrowser()
        self.customerpage = CustomerPage()


    def test_1_customer_No(self):
        self.db_customer.delete_customer_account(['c56576658'])
        self.customerpage.add_customer('c56576658', '', '', '', '', '')
        self.assertEqual(self.customerpage.get_success_text(), '添加记录成功！')

    def test_2_customer_No_name(self):
        self.db_customer.delete_customer_account(['c56576659'])
        self.customerpage.add_customer('c56576659', 'jack', '', '', '', '')

        self.assertEqual(self.customerpage.get_success_text(),'添加记录成功！')
        bool = False
        print(self.db_customer.search_id_name(['c56576659']))
        print(self.customerpage.get_cutomer_name_id())
        if self.db_customer.search_id_name(['c56576659'])==self.customerpage.get_cutomer_name_id():
            bool=True
        self.assertEqual(bool,True)

    def tearDown(self) -> None:
        UseBrowser.quit()