# -*- coding: utf-8 -*-
# @Time : 2021-04-13 14:57
# @Author : bai ping
# @QQ : 376706275
from quote.db.dbhandle import DbHandle


class DbCustomerOp:

    def __init__(self):
        self.db_handle = DbHandle('localhost', 3306, 'root', '123456', 'quote')

    def delete_customer_account(self,para_number):
        self.db_handle.sql_modify('delete from tb_customer where customerNo=%s', para_number)


    def search_id_name(self,para_id):
        res=self.db_handle.sql_search('select customerNo,customerName from tb_customer where customerNo=%s',para_id)
        return list(res[0])

db = DbCustomerOp()
print(db.search_id_name(['c23334513']))