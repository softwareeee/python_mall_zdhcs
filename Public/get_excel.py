# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:35
# @Author  : lileilei
# @File    : get_excel.py
import xlrd, os
from Public.log import LOG, logger


@logger('解析测试用例文件')
def datacel(filrpath):
    try:
        all_case = []
        print(filrpath)
        file = xlrd.open_workbook(filrpath)
        me = file.sheets()[0]
        nrows = me.nrows
        for i in range(1, nrows):
            all_case.append({"id": me.cell(i, 0).value, 'key': me.cell(i, 2).value,
                             'coneent': me.cell(i, 3).value, 'url': me.cell(i, 4).value,
                             'name': me.cell(i, 1).value, 'method': me.cell(i, 5).value,
                             'assert': me.cell(i, 6).value})
        return all_case
    except Exception as e:
         print(e)
         LOG.info('打开测试用例失败，原因是:%s' % e)
         return


@logger('生成数据驱动所用数据')
def makedata(casename):
    path = os.path.join(os.path.join(os.getcwd(), 'test_case_data'), casename)
    make_data = []
    make_data=datacel(path)
    return make_data