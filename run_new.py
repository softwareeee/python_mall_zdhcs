# -*- coding: utf-8 -*-
# @Author  : leizi
from testCase.ddt_case import MyTest
import unittest, time, os
from Public import BSTestRunner
from Public.emmail import sendemali

BASH_DIR = "history"
if __name__ == '__main__':
    # basedir = os.path.abspath(os.path.dirname(__file__))
    # file_dir = os.path.join(basedir, 'test_Report')
    # file_reslut = os.path.join(file_dir, 'caseresult.yaml')
    # try:
    #     os.remove(file_reslut)
    # except:
    #     pass
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTest))
    # now = time.strftime('%Y-%m%d', time.localtime(time.time()))
    # file = os.path.join(file_dir, (now + '.html'))
    # re_open = open(file, 'wb')
    # besautiful = BSTestRunner.BSTestRunner(title="报告",
    #                                        description="下单流程测试报告",
    #                                        stream=re_open,
    #                                        trynum=0,
    #                                        filepath=BASH_DIR,
    #                                        is_show=True)
    # besautiful.run(suite)
    filepath=os.path.join(os.path.join(os.getcwd(), 'test_Report'), '2024-0301.html')
    sendemali(filepath)

