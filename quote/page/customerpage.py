# -*- coding: utf-8 -*-
# @Time : 2021-04-08 16:07
# @Author : bai ping
# @QQ : 376706275
from quote.base.usebrowser import UseBrowser
from quote.base.weboperation import WebOperation
from quote.page.loginpage import LoginPage


class CustomerPage:

    def __init__(self):
        self.op=WebOperation(UseBrowser.driver)
        self.loginpage = LoginPage()


    def add_customer(self,customerNo,customerName,phone,address,relationman,otherInfo):
        self.loginpage.login('admin','123456')
        self.op.change_frame_element('/html/frameset/frame[1]')
        self.op.click_xpath('//*[@id="Bar_panel0_b0"]/img')
        self.op.change_frame_element('/html/frameset/frame[2]')
        self.op.click_xpath('/html/body/center/table[2]/tbody/tr[2]/td[2]/a')
        self.op.change_windows('新增客户信息')
        self.op.input_text_name('customerNO',customerNo)
        self.op.input_text_name('customerName', customerName)
        self.op.input_text_name('phone', phone)
        self.op.input_text_name('address', address)
        self.op.input_text_name('relationman', relationman)
        self.op.input_text_name('otherInfo', otherInfo)
        self.op.click_xpath('/html/body/center/form/table[2]/tbody/tr/td/input[1]')


    #获取新增成功的提示信息
    def get_success_text(self):
        return self.op.get_text_xpath('/html/body/center')[0:7]

    #获取数据

    def modify_customer(self):
        pass



    def remove_cusotmer(self):
        pass


    def get_cutomer_name_id(self):
        return ['c56576659', 'jack']


# if __name__=='__main__':
#     ub=UseBrowser()
#     customerpage = CustomerPage()
#     customerpage.add_customer('c56576655','','','','','')
#     UseBrowser.quit()