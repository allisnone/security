# -*- coding: utf-8 -*-
import re
import os
import csv
import string
import requests
from urllib.parse import quote
from aswg.config import VIRUS_BLOCK_INFO,URL_BLOCK_INFO,DLP_BLOCK_INFO,PROXIES
#from aswg.config import SECURITY_CONFIG
import datetime

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

def http_request(url,uri='',params={},type='get',headers={},proxy=PROXIES):
    """
    下载文件，分析是否被SWG阻断
    :param url:
    :return: callback
    """
    try:
        r = None
        if uri:
            url = ''.join([url,uri])
        if type.lower()=='get':
            print('get_url=',url)
            r = requests.get(encodeURL(url), params=params, proxies=proxy, verify=False)
        elif type.lower()=='post':
            r = requests.post(encodeURL(url),params=params,headers=headers,proxies=proxy,verify=False)
        else:
            return []
        r.encoding = 'utf-8'
        #print(url, r.text)
        if r.status_code == 403:
            
            block_info = get_block_info(r.text)
            return [url, url.split('/')[-1], r.status_code, block_info]
        else:
            return [url, url.split('/')[-1], r.status_code, 'pass']
    except Exception as e:
        print('ERROR=',e)
        return [url, url.split('/')[-1], 0, e]
    
def get_request(url,params={},proxy=PROXIES):
    return http_request(url,type='get',proxy=PROXIES)

def post_request(url,uri='',params={},headers={},proxy=PROXIES):
    return http_request(url,uri=uri,params=params,type='post',headers=headers,proxy=PROXIES)

def get_url_mapping(SECURITY_CONFIG):
    data_threat = SECURITY_CONFIG['Security Assessment']['Threat Prevention']
    data_access = SECURITY_CONFIG['Security Assessment']['Access Control']
    data_protection = SECURITY_CONFIG['Data Protection Assessment']['Data Protection']
    result= {}
    for li in data_threat:
        result[li['id']]=li
        
    for li in data_access:
        result[li['id']]=li
    
    for li in data_protection:
        result[li['id']]=li    
    return result
        
def get_all_http_result(proxy=PROXIES,config={}):
    data_threat = config['Security Assessment']['Threat Prevention']
    print('您的公网IP是： %s' % get_my_public_ip())
    for data in data_threat:
        pass
    return    

def get_my_public_ip():#from ip138
    url = 'http://%s.ip138.com/ic.asp' % datetime.datetime.now().year
    r = requests.get(encodeURL(url),verify=False)
    r.encoding = 'gb2312'
    pattern = re.compile(r'(2(5[0-5]{1}|[0-4]\d{1})|[0-1]?\d{1,2})(\.(2(5[0-5]{1}|[0-4]\d{1})|[0-1]?\d{1,2})){3}')
    #str = re.findall(pattern, r.text)
    return pattern.search(r.text).group()
#get_all_http_result()
#print(get_my_public_ip())
#print(get_url_mapping())    
#print(len(get_url_mapping()))  


    
"""
if __name__ == '__main__':
    print("您的公网IP地址是： ",get_my_public_ip())
    url = 'http://www.sogaoqing.com/upload/nymaim.exe'
    result = http_request(url,type='get',proxy=PROXIES)
    print('result=',result)
    url = 'http://www.sogaoqing.com/upload/VirusSamples/virus1'
    result = http_request(url,type='get',proxy=PROXIES)
    print('result=',result)
    
    url = 'http://www.sogaoqing.com/upload/11.zip'
    result = http_request(url,type='get',proxy=PROXIES)
    print('result=',result)
    
    url = 'http://www.sogaoqing.com/upload/virus.zip'
    result = http_request(url,type='get',proxy=PROXIES)
    print('result=',result)
    
    post_url = 'http://www.sogaoqing.com/'
    uri = 'post.php'
    data = {'content':'13922119451'}
    headers = {"User-Agent":"test request headers"}
    post_reponse = http_request(post_url,type='post',uri=uri,params=data,headers=headers,proxy=PROXIES)
    print('post_reponse=',post_reponse)
    
    
    
"""