# -*- coding: utf-8 -*-
# @Time : 2021-04-14 11:25
# @Author : bai ping
# @QQ : 376706275
import yaml
class YamlOperation:

    def __init__(self,path='../../config/elocation.yaml'):
        with open(path,'r+', encoding='utf8') as file:
            self.data = yaml.load(file,Loader=yaml.FullLoader)

    def get_locator(self,page,locator_name):
        return self.data[page][locator_name]

# yaml_op = YamlOperation('../config/elocation.yaml')
# print(yaml_op.get_locator('CustomerPage','framemain'))