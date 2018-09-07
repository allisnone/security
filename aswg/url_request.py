# -*- coding: utf-8 -*-
import re
import os
import csv
import string
import requests
from urllib.parse import quote
from aswg.config import VIRUS_BLOCK_INFO,URL_BLOCK_INFO,DLP_BLOCK_INFO,PROXIES

def encodeURL(url):
    """
    处理包含中文字符串/空格的URL编码问题
    :param url:
    :return:
    """
    return quote(url, safe=string.printable).replace(' ', '%20')

def get_block_info(response_text):
    if VIRUS_BLOCK_INFO in response_text:
        return 'VIRUS_BLOCK'
    elif URL_BLOCK_INFO in response_text:
        return 'URL_BLOCK'
    elif DLP_BLOCK_INFO in response_text:
        return 'DLP_BLOCK'
    else:
        return 'OTHER_BLOCK'

def http_request(url,type,uri='',data={},headers={},proxy=PROXIES):
    """
    下载文件，分析是否被SWG阻断
    :param url:
    :return: callback
    """
    try:
        r = None
        if type.lower()=='get':
            r = requests.get(encodeURL(url), proxies=proxy, verify=False)
        elif type.lower()=='post':
            url = ''.join([url,uri])
            r = requests.post(url,data=data,headers=headers,proxies=proxy,verify=False)
        else:
            return []
        print(url, r.status_code)
        if r.status_code == 403:
            r.encoding = 'utf-8'
            block_info = get_block_info(r.text)
            return [url, url.split('/')[-1], r.status_code, block_info]
        else:
            return [url, url.split('/')[-1], r.status_code, 'pass']
    except Exception as e:
        print('ERROR=',e)
        return [url, url.split('/')[-1], 0, e]
    
def get_request(url,proxy=PROXIES):
    return http_request(url,type='get',proxy=PROXIES)

def post_request(url,uri='',data={},headers={},proxy=PROXIES):
    return http_request(url,type='post',uri=uri,data=data,headers=headers,proxy=PROXIES)

if __name__ == '__main__':
    url = 'http://www.sogaoqing.com/upload/nymaim.exe'
    result = http_request(url,type='get',proxy=PROXIES)
    print('result=',result)
    
    post_url = 'http://www.sogaoqing.com/'
    uri = 'post.php'
    data = {'content':'13922119451'}
    headers = {"User-Agent":"test request headers"}
    post_reponse = http_request(post_url,type='post',uri=uri,data=data,headers=headers,proxy=PROXIES)
    print('post_reponse=',post_reponse)
    