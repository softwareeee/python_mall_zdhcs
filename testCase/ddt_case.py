import urllib.request
import json
import ddt, unittest, os,yaml
from Interface.testFengzhuang import TestApi
from Public.get_excel import makedata
from Public.get_users import makeusers
from Public.log import LOG
from Public.panduan import assertre
from Public.replace_global import replace_global
from config.config import TestPlanUrl

from config.eqmall_base_conf import malltag,appid,account,vcode



file_dir = os.path.join(os.getcwd(), 'test_Report')
file_reslut = os.path.join(file_dir, 'caseresult.yaml')

data_test = makedata("加入隐形购物车.xls")
data_test2 = makedata("生成临时订单号.xls")
data_test3 = makedata("金额计算.xls")
data_test4 = makedata("下单.xls")
data_test5 = makedata("输入支付密码.xls")
data_test6 = makedata("支付.xls")

global_variables = {
    'skuid': 1149945,
    'spcids':'null',
    'torderId':'null',
    'orderid':'null',
    'guid':'null'
}

def write(data):
    with open(file_reslut, 'a', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True)


def read(data):
    f = open(file_reslut, 'r', encoding='utf-8')
    d = yaml.load(f, Loader=yaml.FullLoader)
    return d[data]


@ddt.ddt
class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global token
        headers = {"Content_type":"apllication/json"}
        api = TestApi(url=TestPlanUrl+"/api/login/auth",
                      parame={
                              "extIdLogin": "true",
                              "loginName": account,
                              "account": "",
                              "password": "",
                              "mallTag": malltag,
                              "vcode": vcode,
                              "appId": appid,
                              "forceLogin": "true"
                            },
                      method="POST",
                      headers=headers,
                      data_type='json')
        header=api.getHeaders()
        token=header['Authorization']
    @classmethod
    def tearDownClass(cls):
        print("end!===================")

    def setUp(self):
        LOG.info('测试用例开始执行')

    def tearDown(self):
        LOG.info('测试用例执行完毕')

    @ddt.data(*data_test)
    def test_api_01(self,data_test):
        '''
        1.处理参数
        2.判断参数是否有依赖
        3.依赖用例参数从全局变量获取
        4.获取失败，用例失败
        5.拼接后请求
        '''
        parem_dict = replace_global(data_test['coneent'], global_variables)
        headers = {
            "Authorization":token
        }
        api = TestApi(url=TestPlanUrl + data_test['url'],
                      parame=eval(parem_dict),
                      method=data_test['method'],headers=headers,data_type='json')
        LOG.info('输入参数：地址:%s,url:%s,key:%s,参数:%s,期望:%s,请求方式：%s,headers:%s' % (TestPlanUrl, data_test['url'], data_test['key'],parem_dict ,data_test['assert'],
                                                           data_test['method'],headers))
        apijson = api.getJson()
        LOG.info('返回结果:%s' % apijson)
        global_variables['spcids']=apijson['result']
        assertall = assertre(data_test['assert'])
        expected_status_code=assertall.get('expected_status_code','Unknown')
        self.assertEqual(str(api.get_status_code()),expected_status_code, msg='预期和返回结果一致')

    @ddt.data(*data_test2)
    def test_api_02(self, data_test2):
        parem_dict = replace_global(data_test2['coneent'], global_variables)
        headers = {
            "Content-Type": 'application/json',
            "Authorization": token
            }
        api = TestApi(url=TestPlanUrl + data_test2['url'],
                        parame=eval(parem_dict),
                        method=data_test2['method'], headers=headers,data_type='data')
        LOG.info('输入参数：地址:%s,url:%s,key:%s,参数:%s,期望:%s,请求方式：%s,headers:%s' % (
            TestPlanUrl, data_test2['url'], data_test2['key'], parem_dict, data_test2['assert'],
            data_test2['method'], headers))
        global_variables['torderId'] = api.getText()
        print(global_variables['torderId'])
        assertall = assertre(data_test2['assert'])
        expected_status_code = assertall.get('expected_status_code', 'Unknown')
        self.assertEqual(str(api.get_status_code()), expected_status_code, msg='预期和返回结果一致')

    @ddt.data(*data_test3)
    def test_api_03(self, data_test3):
        parem_dict = replace_global(data_test3['coneent'], global_variables)
        headers = {
            "Content-Type": 'application/json',
            "Authorization": token
            }
        api = TestApi(url=TestPlanUrl + data_test3['url'],
                        parame=eval(parem_dict),
                        method=data_test3['method'], headers=headers,data_type='json')
        LOG.info('输入参数：地址:%s,url:%s,key:%s,参数:%s,期望:%s,请求方式：%s,headers:%s' % (
            TestPlanUrl, data_test3['url'], data_test3['key'], parem_dict, data_test3['assert'],
            data_test3['method'], headers))
        LOG.info('返回结果:%s' %api.getJson())
        assertall = assertre(data_test3['assert'])
        expected_status_code = assertall.get('expected_status_code', 'Unknown')
        self.assertEqual(str(api.get_status_code()), expected_status_code, msg='预期和返回结果一致')

    @ddt.data(*data_test4)
    def test_api_04(self, data_test4):
        parem_dict = replace_global(data_test4['coneent'], global_variables)
        headers = {
            "Content-Type": 'application/json',
            "Authorization": token
            }
        api = TestApi(url=TestPlanUrl + data_test4['url'],
                        parame=eval(parem_dict),
                        method=data_test4['method'], headers=headers,data_type='json')
        LOG.info('输入参数：地址:%s,url:%s,key:%s,参数:%s,期望:%s,请求方式：%s,headers:%s' % (
            TestPlanUrl, data_test4['url'], data_test4['key'], parem_dict, data_test4['assert'],
            data_test4['method'], headers))
        apijson=api.getJson()
        LOG.info('返回结果:%s' % api.getJson())
        global_variables['orderid'] = apijson['result']['orderId']
        assertall = assertre(data_test4['assert'])
        expected_status_code = assertall.get('expected_status_code', 'Unknown')
        self.assertEqual(str(api.get_status_code()), expected_status_code, msg='预期和返回结果一致')

    @ddt.data(*data_test5)
    def test_api_05(self, data_test5):
        parem_dict = replace_global(data_test5['coneent'], global_variables)
        headers = {
            "Content-Type": 'application/json',
            "Authorization": token
        }
        api = TestApi(url=TestPlanUrl + data_test5['url'],
                      parame=eval(parem_dict),
                      method=data_test5['method'], headers=headers, data_type='json')
        LOG.info('输入参数：地址:%s,url:%s,key:%s,参数:%s,期望:%s,请求方式：%s,headers:%s' % (
            TestPlanUrl, data_test5['url'], data_test5['key'], parem_dict, data_test5['assert'],
            data_test5['method'], headers))
        apijson = api.getJson()
        LOG.info('返回结果:%s' % api.getJson())
        global_variables['guid'] = apijson['result']['guid']
        assertall = assertre(data_test5['assert'])
        expected_status_code = assertall.get('expected_status_code', 'Unknown')
        self.assertEqual(str(api.get_status_code()), expected_status_code, msg='预期和返回结果一致')

    @ddt.data(*data_test6)
    def test_api_06(self, data_test6):
        parem_dict = replace_global(data_test6['coneent'], global_variables)
        headers = {
            "Content-Type": 'application/json',
            "Authorization": token
        }
        api = TestApi(url=TestPlanUrl + data_test6['url'],
                      parame=eval(parem_dict),
                      method=data_test6['method'], headers=headers, data_type='json')
        LOG.info('输入参数：地址:%s,url:%s,key:%s,参数:%s,期望:%s,请求方式：%s,headers:%s' % (
            TestPlanUrl, data_test6['url'], data_test6['key'], parem_dict, data_test6['assert'],
            data_test6['method'], headers))
        apijson = api.getJson()
        LOG.info('返回结果:%s' % apijson)
        assertall = assertre(data_test6['assert'])
        expected_status_code = assertall.get('expected_status_code', 'Unknown')
        self.assertEqual(str(api.get_status_code()), expected_status_code, msg='预期和返回结果一致')

