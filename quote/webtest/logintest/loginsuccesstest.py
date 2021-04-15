# from HTMLTestRunner import HTMLTestRunner
import sys
sys.path.append('D:\\Python\\pythonwork\\project02')
from HwTestReport import HTMLTestReportEN
import time
import unittest

from quote.base.usebrowser import UseBrowser
from quote.page.loginpage import LoginPage
from quote.util.exlopertion import ExlOperation
from quote.webtest.customertest.customersuccesstest import CustomerSuccCase

from quote.webtest.logintest.loginfailedtest import LoginFailedCase


class LoginSuccessCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ub = UseBrowser()
        self.login_page = LoginPage()
        self.exl = ExlOperation()

    def test_1_uname_upasswd_correct(self):
        self.login_page.login(self.exl.get_cell_value(1,2), self.exl.get_cell_value(1,3))
        self.assertEqual(self.login_page.get_success_text(),self.exl.get_cell_value(1,4))

    def tearDown(self) -> None:
        UseBrowser.quit()


if __name__ == '__main__':
    #测试套件
    suite = unittest.TestSuite()
    #加载测试用例
    login_succ_case = unittest.TestLoader().loadTestsFromTestCase(LoginSuccessCase)
    login_fail_case = unittest.TestLoader().loadTestsFromTestCase(LoginFailedCase)
    customer_succ_case = unittest.TestLoader().loadTestsFromTestCase(CustomerSuccCase)
    #case加入到测试套件中
    case_content=[login_succ_case,login_fail_case,customer_succ_case]
    suite.addTests(case_content)
    #日期
    # file_date=time.strftime('%Y-%m-%d_%H_%M_%S')
    # print(file_date)
    #报告文件
    # fp = open('../../report/report'+file_date+'.html','wb+')
    with open('../../report/report.html','wb+') as fp:
        runner = HTMLTestReportEN(stream=fp, verbosity=2, title='Quote Project', description='UI Auto Test')
        # #文本测试运行对象
        # runner = unittest.TextTestRunner(verbosity=2)
        #执行套件case
        runner.run(suite)
