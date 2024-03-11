# -*- coding: utf-8 -*-# @Author  : leiziimport requests, jsonfrom requests import Timeout, RequestExceptionclass requ():    def __init__(self):        self.headers = {            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0"        }    def get(self, url, params):  # get消息        try:            r = requests.get(url, params=params, headers=self.headers)            r.encoding = 'UTF-8'            if r.status_code == 200:                json_response = json.loads(r.text)                return {'code': 0, 'result': json_response}            else:                return {'code': 1, 'result': '接口请求失败，返回状态码：%s' % str(r.status_code)}        except Timeout as e:            return {'code': 1, 'result': '请求超时:%s' % e}        except RequestException as e:            return {'code': 1, 'result': '请求异常:%s' % e}        except Exception as e:            return {'code': 1, 'result': 'get请求出错，出错原因:%s' % e}    def post(self, url, params,headers,data_type):  # post消息        try:            if data_type == "json":                r = requests.post(url, json=params, headers=headers)            else:                params = json.dumps(params)                r = requests.post(url, data=params, headers=headers)            return r        except Timeout as e:            return {'code': 1, 'result': '请求超时:%s' % e}        except RequestException as e:            return {'code': 1, 'result': '请求异常:%s' % e}        except Exception as e:            return {'code': 1, 'result': 'post请求出错，出错原因:%s' % e}    def delparams(self, url, params):  # 删除的请求        try:            del_word = requests.delete(url, params=params, headers=self.headers)            if del_word.status_code == 200:                json_response = json.loads(del_word.text)                return {'code': 0, 'result': json_response}            else:                return {'code': 1, 'result': '接口请求失败，返回状态码：%s' % str(del_word.status_code)}        except Timeout as e:            return {'code': 1, 'result': '请求超时:%s' % e}        except RequestException as e:            return {'code': 1, 'result': '请求异常:%s' % e}        except Exception as e:            return {'code': 1, 'result': 'del请求出错，出错原因:%s' % e}    def putparams(self, url, params):  # put请求        try:            data = json.dumps(params)            result = requests.put(url, data)            if result.status_code == 200:                json_response = json.loads(result.text)                return {'code': 0, 'result': json_response}            else:                return {'code': 1, 'result': '接口请求失败，返回状态码：%s' % str(result.status_code)}        except Timeout as e:            return {'code': 1, 'result': '请求超时:%s' % e}        except RequestException as e:            return {'code': 1, 'result': '请求异常:%s' % e}        except Exception as e:            return {'code': 1, 'result': 'put请求出错，出错原因:%s' % e}