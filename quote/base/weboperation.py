# -*- coding: utf-8 -*-
# @Time : 2021-04-08 16:03
# @Author : bai ping
# @QQ : 376706275
from quote.base.usebrowser import UseBrowser
import time


class WebOperation:

    def __init__(self, driver):
        self.driver = driver

    #打开网址
    def open_url(self,url):
        self.driver.get(url)

    #通过name输入文本
    def input_text_name(self,name_locator,text):
        self.driver.find_element_by_name(name_locator).send_keys(text)

    #通过xpath输入文本
    def input_text_xpath(self,xpath_locator,text):
        self.driver.find_element_by_xpath(xpath_locator).send_keys(text)


    #通过xpath点击
    def click_xpath(self,xpath_locator):
        time.sleep(1)
        self.driver.find_element_by_xpath(xpath_locator).click()

    #获取文本信息
    def get_text_xpath(self,xpath_locator):
        return self.driver.find_element_by_xpath(xpath_locator).text


    #切换frame
    def change_frame_element(self,xpath_locator):
        self.driver.switch_to.default_content()
        element =self.driver.find_element_by_xpath(xpath_locator)
        self.driver.switch_to.frame(element)


    #切换窗体
    def change_windows(self,title):
        for window in self.driver.window_handles:
            self.driver.switch_to.window(window)
            if self.driver.title==title:
                break


# if __name__=='__main__':
#     ub = UseBrowser('Chrome')
#     op = WebOperation(UseBrowser.driver)
#     op.open_url('http://localhost:8080/JavaPrj_6/')
#     op.input_text_name('username','admin')
#     op.input_text_name('password', '123456')
#     op.click_xpath('/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[6]/td/input[1]')
#     time.sleep(3)
#     UseBrowser.quit()
