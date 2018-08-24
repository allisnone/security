# -*- coding: utf-8 -*-
#from source_ulrs import *
from aswg.source_urls import EXE_URLS, MALICIOUS_WEBSITES, PHISHING_ATTACK,\
    SESSION_HIJACKING, BOTNET_CALLBACK, CROSS_SITE_SCRIPTING,\
    OLDER_KNOWN_VIRUSES, VIRUS_HIDDEN_IN_ZIP,\
    COMMON_VIRUS_FROM_KNOWN_MALICIOUS_SITE, ANONYMIZING_WEBSITES,\
    EMBARGOED_COUNTRIE, ADULT_WEBSITES, CREDIT_CARD, SOCIAL_SECURITY_NUMBER,\
    SOURCE_CODE

SECURITY_CONFIG = {
    'Security Assessment': {
        'Threat Prevention': [
            #'Block an executable (.exe) download': 
                {
                'name':'Block an executable (.exe) download',
                'urls':EXE_URLS,
                'detail':'This tests if you can download .exe files from websites that use a content delivery network (CDN). A CDN makes you vulnerable to malware.',
                'description':'This test tries to download an executable file from a website with a good reputation that uses a Content Distribution Network (CDN) like Akamai or AWS. It tests whether your security infrastructure can block the executable, limiting the possible introduction of malware and other threats.',
                'method': 'get',
                },
                              
            #'Block threats in known malicious websites': 
                {
                'name':'Block threats in known malicious websites',
                'urls':MALICIOUS_WEBSITES,
                'detail':'This tests if you can download a benign object from a known malicious site. It does not attempt to download actual malware.',
                'description':'This test checks to see if a benign object hosted on a known malicious site is blocked by your security solution. It uses a \
                compromised site from a list published by Google. The test does not attempt to download actual malware.',
                'method': 'get',
                },
                              
            #'Detect a phishing attack': 
            {
                'name':'Detect a phishing attack',
                'urls': PHISHING_ATTACK,
                'detail':'This checks if you can access one of the latest validated phishing sites uncovered by Phishtank.com. ',
                'description':'This test tries to access one of the latest validated phishing sites uncovered by Phishtank.com. The test covers all infection vectors, including mobile traffic. Criminals take advantage of mobile traffic as a key weakness in many security solutions. The test does not attempt to download actual malware.',
                'method': 'get',
                },
            #'Prevent cookie stealing or session hijacking': 
                {
                'name':'Prevent cookie stealing or session hijacking',
                'urls':SESSION_HIJACKING,
                'detail':' ',
                'description':'',
                'method': 'get',
                },
                              
            #'Stop a botnet callback': 
                {
                'name':'Stop a botnet callback',
                'urls':BOTNET_CALLBACK,
                'detail':' ',
                'description':'',
                'method': 'get',
                },
            #'Prevent cross-site scripting': 
                {
                'name':'Prevent cross-site scripting',
                'urls': CROSS_SITE_SCRIPTING,
                'detail':' ',
                'description':'',
                'method': 'get',
                },
            #'Stop older known viruses': 
                {
                'name':'Stop older known viruses',
                'urls':OLDER_KNOWN_VIRUSES,
                'detail':' ',
                'description':'',
                'method': 'get',
                },
                              
            #'Block a virus hidden in a zip file': 
                {
                'name':'Block a virus hidden in a zip file',
                'urls':VIRUS_HIDDEN_IN_ZIP,
                'detail':' ',
                'description':'',
                'method': 'get',
                },
                              
            #'Prevent a common virus from a known malicious site': 
                {
                'name':'Prevent a common virus from a known malicious site',
                'urls': COMMON_VIRUS_FROM_KNOWN_MALICIOUS_SITE,
                'detail':' ',
                'description':'',
                'method': 'get',
                },
            #'D': {
            #    'name':'',
            #    'urls':[],
            #    'detail':' ',
            #    'description':''
            #    },
            
            ],
        'Access Control':[
            #'Block websites in embargoed countrie': 
                {
                'name':'Block websites in embargoed countrie',
                'urls': EMBARGOED_COUNTRIE,
                'detail':'This tests your ability to access websites in countries that are embargoed by the United States and the European Union, such as North Korea.',
                'description':'This test tries to connect to websites in countries under embargo by the Unites States and European Union, such as North Korea. Most companies want to prevent users from connecting to websites in countries that are under embargo in order to comply with trade laws. Additionally, compromised websites are often hosted in countries that are hostile to the United States and the European Union, and they place a low priority on Internet security. ',
                'method': 'get',
                },
                          
            #'Block access to anonymizing websites ': 
                {
                'name':'Block access to anonymizing websites ',
                'urls': ANONYMIZING_WEBSITES,
                'detail':'This test tries to connect to an anonymizing website. Failing this test means you can bypass company policy and access restricted content.',
                'description':'This test tries to connect to an anonymizing website. Employees often try to bypass company policy by using anonymizing proxies that allow them to visit blacklisted websites, view pornography, or access restricted content. These anonymizers can open a backdoor for malware, expose your company to litigation risk, and expose your data to untrusted third parties.',
                'method': 'get',
                },
                          
            #'Block access to adult websites': 
                {
                'name':'Block access to adult websites',
                'urls': ADULT_WEBSITES,
                'method': 'get',
                'detail':'This test attempts to visit a known adult website and download a benign icon.',
                'description':'This test tries to visit a known adult website and download a benign icon. Employees often violate company policy and try to visit blacklisted websites and view pornography. These sites act as common watering holes to propagate malware, and they might expose your company to litigation risk and your data to untrusted third parties.'
                },
            
            ]
        },
    'Data Protection Assessment': {
        'Data Protection': [
            #'Block credit card exfiltration': 
                {
                'name':'Block credit card exfiltration',
                'urls': CREDIT_CARD,
                'method': 'get',
                'detail':'This test attempts to exfiltrate numbers that match the format of valid credit card numbers.',
                'description':'This test tries to exfiltrate numbers out of your network that match the format of credit card numbers. Your network security solution should easily identify this leakage.'
                },
                            
            #'Block Social Security number exfiltration': 
                {
                'name':'Block Social Security number exfiltration',
                'urls': SOCIAL_SECURITY_NUMBER,
                'method': 'get',
                'detail':'This test attempts to exfiltrate numbers that match the format of U.S. Social Security numbers.',
                'description':'This test tries to exfiltrate numbers out of your network that match the format of U.S. Social Security numbers. Your network security solution should easily identify this leakage.'
                },
        
            #'Block source code exfiltration': 
                {
                'name':'Block source code exfiltration',
                'urls': SOURCE_CODE,
                'method': 'get',
                'detail':'This test attempts to exfiltrate typical patterns found in source code. ',
                'description':'This test tries to exfiltrate typical patterns found in source code. Stealing your intellectual property is the goal of some of the world most dangerous hackers and state-sponsored actors seeking a competitive advantage. A leak of intellectual property can have profound consequences for your enterprise — from rewriting source code to re-issuing binaries.'
                }
    
            ]
        }
    }

#print(SECURITY_CONFIG)