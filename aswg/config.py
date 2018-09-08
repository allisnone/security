# -*- coding: utf-8 -*-
#from source_ulrs import *
from aswg.source_urls import EXE_URLS, MALICIOUS_WEBSITES, PHISHING_ATTACK,\
    SESSION_HIJACKING, BOTNET_CALLBACK, CROSS_SITE_SCRIPTING,\
    OLDER_KNOWN_VIRUSES, VIRUS_HIDDEN_IN_ZIP,\
    COMMON_VIRUS_FROM_KNOWN_MALICIOUS_SITE, ANONYMIZING_WEBSITES,\
    EMBARGOED_COUNTRIE, ADULT_WEBSITES, CREDIT_CARD, SOCIAL_SECURITY_NUMBER,\
    SOURCE_CODE,INTERAL_URL,INTERAL_POST_URL,CROSS_POST_URL

VIRUS_BLOCK_INFO = "访问的URL中含有安全风险"
URL_BLOCK_INFO = '本次访问违反了公司的网络安全策略'
DLP_BLOCK_INFO = '本次访问违反了公司的数据防泄漏策略'
#PROXIES = {'http': 'http://172.18.200.240:8080'}
PROXIES = {'http': 'http://49.4.84.41:8066'}
IMAGE_STATUS = {'pass':'../static/images/pass.png','fail':'../static/images/fail.png'}

SECURITY_CONFIG = {
    'Security Assessment': {
        'Threat Prevention': [
            #'Block an executable (.exe) download': 
                {
                'name':'可执行文件下载',
                'urls':EXE_URLS,
                'detail':'这项测试将验证您是否可以直接下载可执行文件，网络下载的exe文件通常是病毒常见载体',
                'description':'This test tries to download an executable file from a website with a good reputation that uses a Content Distribution Network (CDN) like Akamai or AWS. It tests whether your security infrastructure can block the executable, limiting the possible introduction of malware and other threats.',
                'method': 'get',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'html',
                'para': 'securypreview_exe.exe',
                'id':'1',
                
                },
                              
            #'Block threats in known malicious websites': 
                {
                'name':'恶意木马网站访问',
                'urls':MALICIOUS_WEBSITES,
                'detail':'该测试验证您是否可以访问恶意木马网站，该测试不会直接下载木马软件',
                'description':'This test checks to see if a benign object hosted on a known malicious site is blocked by your security solution. It uses a \
                compromised site from a list published by Google. The test does not attempt to download actual malware.',
                'method': 'get',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'html',
                'para': '',
                'id':'2',
                
                },
                              
            #'Detect a phishing attack': 
                {
                'name':'钓鱼网站访问',
                'urls': PHISHING_ATTACK,
                'detail':'该测试验证您是否可以访问钓鱼网站，来源于 Phishtank.com权威识别的最新钓鱼站点 ',
                'description':'待描述',
                'method': 'get',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'html',
                'para': '',
                'id':'3',
                },
            #'Block a virus hidden in a zip file': 
                {
                'name':'压缩文件病毒',
                'urls':VIRUS_HIDDEN_IN_ZIP,
                'detail':' 该测试验证您是否可以识别压缩文件中的病毒',
                'description':'待描述',
                'method': 'get',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'html',
                'para': '',
                'id':'4',
                },
                              
            #'Prevent a common virus from a known malicious site': 
                {
                'name':'普通病毒',
                'urls': OLDER_KNOWN_VIRUSES,
                'detail':' 该测试验证您已知病毒，来源权威病毒网站-卡饭',
                'description':'待描述',
                'method': 'get',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'html',
                'para': '',
                'id':'5',
                }
            ],
        'Access Control':[
            #'Block websites in embargoed countrie': 
                {
                'name':'暴力武器网站访问',
                'urls': EMBARGOED_COUNTRIE,
                'detail':'该测试验证您是否可以访问宣扬暴力的网站',
                'description':'This test tries to connect to websites in countries under embargo by the Unites States and European Union, such as North Korea. Most companies want to prevent users from connecting to websites in countries that are under embargo in order to comply with trade laws. Additionally, compromised websites are often hosted in countries that are hostile to the United States and the European Union, and they place a low priority on Internet security. ',
                'method': 'get',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'html',
                'para': '',
                'id':'6',
                },
                          
            #'Block access to adult websites': 
                {
                'name':'成人网站访问',
                'urls': ADULT_WEBSITES,
                'method': 'get',
                'detail':'该测试验证是否可以访问涉黄成人网站',
                'description':'待定',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'html',
                'para': '',
                'id':'7',
                },
            
            ]
        },
    'Data Protection Assessment': {
        'Data Protection': [
            #'Block credit card exfiltration': 
                {
                'name':'个人隐私信息保护',
                'urls': CROSS_POST_URL,#CREDIT_CARD,
                'method': 'POST',
                'detail':'验证是否可以外发保护个人隐私信息',
                'description':'个人隐私信息包括信用卡号，手机号、中国护照号',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'html',
                'para': '13922119451',
                'id':'8',
                },
            #'Block credit card exfiltration': 
                {
                'name':'个人隐私信息保护',
                'urls': CROSS_POST_URL,#CREDIT_CARD,
                'method': 'POST',
                'detail':'隐私信息图片外发',
                'description':'隐私信息图片外发',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'html',
                'para': '13922119451',
                'id':'8',
                },
            #'Block credit card exfiltration': 
                {
                'name':'个人隐私信息保护',
                'urls': CROSS_POST_URL,#CREDIT_CARD,
                'method': 'POST',
                'detail':'隐私信息Word,Excel外发',
                'description':'隐私信息Word,Excel外发',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'html',
                'para': '13922119451',
                'id':'8',
                },
                            
                            
            #'Block Social Security number exfiltration': 
                {
                'name':'企业机密保护',
                'urls': CROSS_POST_URL,
                'method': 'POST',
                'detail':'标准合同，财务报表',
                'description':'待完善',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'json',
                'para': '资产负债率',
                'id':'9',
                },
            #'Block Social Security number exfiltration': 
                {
                'name':'企业机密保护',
                'urls': CROSS_POST_URL,
                'method': 'POST',
                'detail':'源代码',
                'description':'待完善',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'json',
                'para': '资产负债率',
                'id':'9',
                },
            #'Block Social Security number exfiltration': 
                {
                'name':'企业机密保护',
                'urls': CROSS_POST_URL,
                'method': 'POST',
                'detail':'企业薪酬福利信息',
                'description':'待完善',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'json',
                'para': '资产负债率',
                'id':'9',
                },
            #'Block Social Security number exfiltration': 
                {
                'name':'企业机密保护',
                'urls': CROSS_POST_URL,
                'method': 'POST',
                'detail':'网络拓扑图，Password/Shadow文件上传',
                'description':'待完善',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'json',
                'para': '资产负债率',
                'id':'9',
                },
        
            #'Block source code exfiltration': 
                {
                'name':'不正当言论',
                'urls': CROSS_POST_URL,
                'method': 'POST',
                'detail':'淫秽文字',
                'description':'待完善',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'text',
                'para': '法轮功',
                'id':'10',
                },
            #'Block source code exfiltration': 
                {
                'name':'不正当言论',
                'urls': CROSS_POST_URL,
                'method': 'POST',
                'detail':'暴力武器 ',
                'description':'待完善',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'text',
                'para': '病例',
                'id':'11',
                },
            #'Block source code exfiltration': 
                {
                'name':'不正当言论',
                'urls': CROSS_POST_URL,
                'method': 'POST',
                'detail':'反党反政府言论 ',
                'description':'待完善',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'text',
                'para': '病例',
                'id':'11',
                },
            #'Block source code exfiltration': 
                {
                'name':'行业特点信息保护',
                'urls': CROSS_POST_URL,
                'method': 'POST',
                'detail':'住院信息',
                'description':'待完善',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'text',
                'para': '病例',
                'id':'11',
                },
            #'Block source code exfiltration': 
                {
                'name':'行业特点信息保护',
                'urls': CROSS_POST_URL,
                'method': 'POST',
                'detail':'健康病症 ',
                'description':'待完善',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'text',
                'para': '病例',
                'id':'11',
                },
            #'Block source code exfiltration': 
                {
                'name':'行业特点信息保护',
                'urls': CROSS_POST_URL,
                'method': 'POST',
                'detail':'理赔记录',
                'description':'待完善',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'text',
                'para': '病例',
                'id':'11',
                },
            #'Block source code exfiltration': 
                {
                'name':'行业特点信息保护',
                'urls': CROSS_POST_URL,
                'method': 'POST',
                'detail':'AutoCAD图纸 ',
                'description':'待完善',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'text',
                'para': '病例',
                'id':'11',
                }
            ]
        }
    }

def get_url_mapping():
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

URL_MAPPING = get_url_mapping()
#print(SECURITY_CONFIG)