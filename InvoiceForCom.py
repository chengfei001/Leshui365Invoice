# -*- coding: utf-8 -*-
"""
国税发票查询
@author: chengfei
"""


# import urllib2
from requests import request, post
from json import loads

# appKey 与 appSecret 配置
appKey1 ="13120591957"
appSecret1 ="88888888"
# 获取token的url
token_url = "https://open.leshui365.com/getToken?appKey=d7291ae73f504eeba4bcb42502cf608c&appSecret=4112f507-33a6-4b8a-ab08-ebb48b543283" #% ('d7291ae73f504eeba4bcb42502cf608c','4112f507-33a6-4b8a-ab08-ebb48b543283')


### 发票api接口
fapiao_url = "https://open.leshui365.com/api/invoiceInfoForCom"
invoiceCode = "1100171320"
invoiceNumber = "58369155"
billTime = "2017-06-23"
checkCode = "527925"
invoiceAmount = "128"


def get_token(token_url):
    response = request(method='get', url=token_url)
    return response.text

def get_fapiao(invoiceCode, invoiceNumber, billTime, invoiceAmount, token):
    fp_data = {"invoiceCode": invoiceCode,  # 发票代码
               "invoiceNumber": invoiceNumber,  # 发票号码
               "billTime": billTime,  # 开票时间
               "checkCode": checkCode,  # 验证码（发票后六位，专票，机动车票可以不传）
               "invoiceAmount":invoiceAmount,  # 开票金额、不含税价(普票、电子发票可以不传)
               "token": token  # 授权码，token取get_token返回值
               }
    response = post(url=fapiao_url, data=fp_data).text
    print(response)
    if loads(response)['RtnCode'] == '00':
        invoiceResult = loads(response)['invoiceResult']
        salesName = loads(invoiceResult)['salesName']
        print(salesName+invoiceResult)
    else:
        print(loads(response)['resultMsg'])
    # 打印 返回值
    return response

if __name__ == "__main__":
    # 两小时内不需要执行获取token
    token =loads(get_token(token_url))['token']
    print(token)
    # 两小时内不需要执行获取token
##
result = get_fapiao(invoiceCode, invoiceNumber, billTime, checkCode, token)
# print(result)