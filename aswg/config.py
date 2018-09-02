# -*- coding: utf-8 -*-
#from source_ulrs import *
from aswg.source_urls import EXE_URLS, MALICIOUS_WEBSITES, PHISHING_ATTACK,\
    SESSION_HIJACKING, BOTNET_CALLBACK, CROSS_SITE_SCRIPTING,\
    OLDER_KNOWN_VIRUSES, VIRUS_HIDDEN_IN_ZIP,\
    COMMON_VIRUS_FROM_KNOWN_MALICIOUS_SITE, ANONYMIZING_WEBSITES,\
    EMBARGOED_COUNTRIE, ADULT_WEBSITES, CREDIT_CARD, SOCIAL_SECURITY_NUMBER,\
    SOURCE_CODE,INTERAL_URL,INTERAL_POST_URL,CROSS_POST_URL

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
                'cross': '1',
                'type': 'jsonp',
                'para': '',
                
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
                'cross': '1',
                'type': 'jsonp',
                'para': '',
                
                },
                              
            #'Detect a phishing attack': 
                {
                'name':'钓鱼网站访问',
                'urls': PHISHING_ATTACK,
                'detail':'该测试验证您是否可以访问钓鱼网站，来源于 Phishtank.com权威识别的最新钓鱼站点 ',
                'description':'待描述',
                'method': 'get',
                'icon': '../static/images/fail.png',
                'cross': '1',
                'type': 'jsonp',
                'para': '',
                },
            #'Block a virus hidden in a zip file': 
                {
                'name':'压缩文件病毒',
                'urls':VIRUS_HIDDEN_IN_ZIP,
                'detail':' 该测试验证您是否可以识别压缩文件中的病毒',
                'description':'待描述',
                'method': 'get',
                'icon': '../static/images/fail.png',
                'cross': '1',
                'type': 'jsonp',
                'para': '',
                },
                              
            #'Prevent a common virus from a known malicious site': 
                {
                'name':'普通病毒',
                'urls': COMMON_VIRUS_FROM_KNOWN_MALICIOUS_SITE,
                'detail':' 该测试验证您已知病毒，来源权威病毒网站-卡饭',
                'description':'待描述',
                'method': 'get',
                'icon': '../static/images/fail.png',
                'cross': '1',
                'type': 'jsonp',
                'para': '',
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
                'cross': '1',
                'type': 'jsonp',
                'para': '',
                },
                          
            #'Block access to adult websites': 
                {
                'name':'成人网站访问',
                'urls': ADULT_WEBSITES,
                'method': 'get',
                'detail':'该测试验证是否可以访问涉黄成人网站',
                'description':'待定',
                'icon': '../static/images/fail.png',
                'cross': '1',
                'type': 'jsonp',
                'para': '',
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
                'para': '13922119451'
                },
                            
            #'Block Social Security number exfiltration': 
                {
                'name':'企业机密保护',
                'urls': CROSS_POST_URL,
                'method': 'POST',
                'detail':'企业薪酬福利，财务报表',
                'description':'待完善',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'json',
                'para': '资产负债率'
                },
        
            #'Block source code exfiltration': 
                {
                'name':'不正当言论',
                'urls': INTERAL_POST_URL,
                'method': 'POST',
                'detail':'淫秽文字，暴力武器，反党反政府，压缩凡是发送 ',
                'description':'待完善',
                'icon': '../static/images/fail.png',
                'cross': '0',
                'type': 'text',
                'para': '法轮功'
                },
            #'Block source code exfiltration': 
                {
                'name':'行业特点信息保护',
                'urls': INTERAL_POST_URL,
                'method': 'POST',
                'detail':'住院信息，健康病症，理赔记录，AutoCAD图纸 ',
                'description':'待完善',
                'icon': '../static/images/fail.png',
                'cross': '0',
                'type': 'text',
                'para': '病例'
                }
            ]
        }
    }

#print(SECURITY_CONFIG)