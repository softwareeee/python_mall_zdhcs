# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:36
# @Author  : lileilei
# @Site    : 
# @File    : testFengzhuang.py

from Public.test_requests import requ
import json


class TestApi(object):
    def __init__(self, url, parame,method,headers,data_type):
        self.url = url
        self.parame = parame
        self.method = method
        self.headers = headers
        self.data_type = data_type
        self.reques = requ()


    def testapi(self):
        if self.method == 'POST':
            self.response = self.reques.post(self.url, self.parame , self.headers,self.data_type)
        elif self.method == "GET":
            self.response = self.reques.get(url=self.url, params=self.parame)
        elif self.method == "PUT":
            self.response = self.reques.putparams(url=self.url, params=self.parame)
        elif self.method == "DELETE":
            self.response = self.reques.delparams(url=self.url, params=self.parame)
        return self.response

    def getJson(self):
        json_data = self.testapi()
        if json_data.status_code == 200:
            json_response = json.loads(json_data.text)
            return {'code': 0, 'result': json_response}
        else:
            return {'code': 1, 'result': '接口请求失败，返回状态码：%s' % str(json_data.status_code)}


    def getText(self):
        return self.testapi().text

    def getHeaders(self):
        json_data = self.testapi()
        headers=json_data.headers
        return headers

    def get_status_code(self):
        json_data = self.testapi()
        return json_data.status_code

