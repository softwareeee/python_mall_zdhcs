# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:35
# @Author  : lileilei
# @File    : get_excel.py
import xlrd, os
from Public.log import LOG, logger


@logger('解析测试用例文件')
def datacel(filrpath):
    try:
        all_users = []
        file = xlrd.open_workbook(filrpath)
        me = file.sheets()[0]
        nrows = me.nrows
        for i in range(1, nrows):
            all_users.append({"users": int(me.cell(i, 0).value)})
        return all_users
    except Exception as e:
         print(e)
         LOG.info('打开测试用例失败，原因是:%s' % e)
         return


@logger('生成数据驱动所用数据')
def makeusers():
    path = os.path.join(os.path.join(os.getcwd(), 'test_case_data'), 'users.xlsx')
    make_users = []
    make_users=datacel(path)
    return make_users