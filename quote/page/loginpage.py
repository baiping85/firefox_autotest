# -*- coding: utf-8 -*-
# @Time : 2021-04-08 16:06
# @Author : bai ping
# @QQ : 376706275
from quote.base.usebrowser import UseBrowser
from quote.base.weboperation import WebOperation
from quote.util.exlopertion import ExlOperation
from quote.util.loginfo import LogInfo
from quote.util.yamloperation import YamlOperation


class LoginPage:


    def __init__(self):
        self.op = WebOperation(UseBrowser.driver)
        self.exl = ExlOperation()
        self.yam = YamlOperation()
        self.log = LogInfo()

    #登录功能
    def login(self,username,password):
        self.log.set_message('info','打开Quote网址')
        self.op.open_url(self.exl.get_cell_value(1,1))
        self.log.set_message('info', '输入用户名:'+username)
        self.op.input_text_name(self.yam.get_locator('LoginPage','username'),username)
        self.log.set_message('info', '输入密码:'+password)
        self.op.input_text_name(self.yam.get_locator('LoginPage','password'),password)
        self.log.set_message('info', '点击提交')
        self.op.click_xpath(self.yam.get_locator('LoginPage','submit'))

    #获取正确信息功能
    def get_success_text(self):
        self.op.change_frame_element(self.yam.get_locator('LoginPage','framemain'))
        return self.op.get_text_xpath(self.yam.get_locator('LoginPage','successinfo'))

    #获取未登录成功的信息
    def get_failed_text(self):
        return self.op.get_text_xpath('/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[5]/td')


# if __name__ == '__main__':
    # ub = UseBrowser('Chrome')
    # loginpage = LoginPage()
    # loginpage.login('admin','123456')
    # UseBrowser.quit()