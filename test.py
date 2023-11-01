import urllib.request

import ddt, unittest, os, yaml
from Interface.testFengzhuang import TestApi
from Public.get_excel import makedata
from Public.log import LOG
from Public.panduan import assertre
from config.config import TestPlanUrl


data_test = makedata()
if __name__ == "__main__":
    print(data_test[0]['coneent'])
    api = TestApi(url=TestPlanUrl + data_test[0]['url'],
                  parame=data_test[0]['coneent'],
                  method=data_test[0]['method'])
    api.getJson()
