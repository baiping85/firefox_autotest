# -*- coding: utf-8 -*-
# @Time : 2021-04-08 16:02
# @Author : bai ping
# @QQ : 376706275
from selenium import webdriver
import time

class UseBrowser:

    driver = None

    def __init__(self,browser_name='Firefox'):
        if browser_name == 'Chrome':
            self.driver = webdriver.Chrome('../../chromedriver.exe')
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            UseBrowser.driver = self.driver

        elif browser_name == 'Firefox':
            self.driver = webdriver.Firefox(executable_path='../../geckodriver.exe')
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            UseBrowser.driver = self.driver
        else:
            pass


    @classmethod
    def quit(cls):
        cls.driver.quit()


# if __name__=='__main__':
#     ub = UseBrowser()
#     time.sleep(3)
#     UseBrowser.quit()