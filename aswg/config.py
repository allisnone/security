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
        'Threat Prevention': {
            'Block an executable (.exe) download': {
                'TEST NAME':'Block an executable (.exe) download',
                'TEST URL':EXE_URLS,
                'TEST DETAIL':'This tests if you can download .exe \
                files from websites that use a content delivery network \
                (CDN). A CDN makes you vulnerable to malware.',
                'TEST DESCRIPTION':'This test tries to download an executable \
                file from a website with a good reputation that uses a Content \
                Distribution Network (CDN) like Akamai or AWS. It tests whether \
                your security infrastructure can block the executable, limiting \
                the possible introduction of malware and other threats.',
                'METHOD': 'get',
                },
                              
            'Block threats in known malicious websites': {
                'TEST NAME':'Block threats in known malicious websites',
                'TEST URL':MALICIOUS_WEBSITES,
                'TEST DETAIL':'This tests if you can download a benign object from \
                a known malicious site. It does not attempt to download actual malware.',
                'TEST DESCRIPTION':'This test checks to see if a benign object hosted on \
                a known malicious site is blocked by your security solution. It uses a \
                compromised site from a list published by Google. The test does not \
                attempt to download actual malware.',
                'METHOD': 'get',
                },
                              
            'Detect a phishing attack': {
                'TEST NAME':'Detect a phishing attack',
                'TEST URL': PHISHING_ATTACK,
                'TEST DETAIL':'This checks if you can access one of the latest validated phishing sites uncovered by Phishtank.com. ',
                'TEST DESCRIPTION':'This test tries to access one of the latest validated phishing sites uncovered by Phishtank.com. The test covers all infection vectors, including mobile traffic. Criminals take advantage of mobile traffic as a key weakness in many security solutions. The test does not attempt to download actual malware.',
                'METHOD': 'get',
                },
            'Prevent cookie stealing or session hijacking': {
                'TEST NAME':'Prevent cookie stealing or session hijacking',
                'TEST URL':SESSION_HIJACKING,
                'TEST DETAIL':' ',
                'TEST DESCRIPTION':'',
                'METHOD': 'get',
                },
                              
            'Stop a botnet callback': {
                'TEST NAME':'Stop a botnet callback',
                'TEST URL':BOTNET_CALLBACK,
                'TEST DETAIL':' ',
                'TEST DESCRIPTION':'',
                'METHOD': 'get',
                },
            'Prevent cross-site scripting': {
                'TEST NAME':'Prevent cross-site scripting',
                'TEST URL': CROSS_SITE_SCRIPTING,
                'TEST DETAIL':' ',
                'TEST DESCRIPTION':'',
                'METHOD': 'get',
                },
            'Stop older known viruses': {
                'TEST NAME':'Stop older known viruses',
                'TEST URL':OLDER_KNOWN_VIRUSES,
                'TEST DETAIL':' ',
                'TEST DESCRIPTION':'',
                'METHOD': 'get',
                },
                              
            'Block a virus hidden in a zip file': {
                'TEST NAME':'Block a virus hidden in a zip file',
                'TEST URL':VIRUS_HIDDEN_IN_ZIP,
                'TEST DETAIL':' ',
                'TEST DESCRIPTION':'',
                'METHOD': 'get',
                },
                              
            'Prevent a common virus from a known malicious site': {
                'TEST NAME':'Prevent a common virus from a known malicious site',
                'TEST URL': COMMON_VIRUS_FROM_KNOWN_MALICIOUS_SITE,
                'TEST DETAIL':' ',
                'TEST DESCRIPTION':'',
                'METHOD': 'get',
                },
            #'D': {
            #    'TEST NAME':'',
            #    'TEST URL':[],
            #    'TEST DETAIL':' ',
            #    'TEST DESCRIPTION':''
            #    },
            
            },
        'Access Control':{
            'Block websites in embargoed countrie': {
                'TEST NAME':'Block websites in embargoed countrie',
                'TEST URL': EMBARGOED_COUNTRIE,
                'TEST DETAIL':'This tests your ability to access websites in countries that are embargoed by the United States and the European Union, such as North Korea.',
                'TEST DESCRIPTION':'This test tries to connect to websites in countries under embargo by the Unites States and European Union, such as North Korea. Most companies want to prevent users from connecting to websites in countries that are under embargo in order to comply with trade laws. Additionally, compromised websites are often hosted in countries that are hostile to the United States and the European Union, and they place a low priority on Internet security. ',
                'METHOD': 'get',
                },
                          
            'Block access to anonymizing websites ': {
                'TEST NAME':'Block access to anonymizing websites ',
                'TEST URL': ANONYMIZING_WEBSITES,
                'TEST DETAIL':'This test tries to connect to an anonymizing website. Failing this test means you can bypass company policy and access restricted content.',
                'TEST DESCRIPTION':'This test tries to connect to an anonymizing website. Employees often try to bypass company policy by using anonymizing proxies that allow them to visit blacklisted websites, view pornography, or access restricted content. These anonymizers can open a backdoor for malware, expose your company to litigation risk, and expose your data to untrusted third parties.',
                'METHOD': 'get',
                },
                          
            'Block access to adult websites': {
                'TEST NAME':'Block access to adult websites',
                'TEST URL': ADULT_WEBSITES,
                'METHOD': 'get',
                'TEST DETAIL':'This test attempts to visit a known adult website and download a benign icon.',
                'TEST DESCRIPTION':'This test tries to visit a known adult website and download a benign icon. Employees often violate company policy and try to visit blacklisted websites and view pornography. These sites act as common watering holes to propagate malware, and they might expose your company to litigation risk and your data to untrusted third parties.'
                },
            
            }
        },
    'Data Protection Assessment': {
        'Data Protection': {
            'Block credit card exfiltration': {
                'TEST NAME':'Block credit card exfiltration',
                'TEST URL': CREDIT_CARD,
                'METHOD': 'get',
                'TEST DETAIL':'This test attempts to exfiltrate numbers that match the format of valid credit card numbers.',
                'TEST DESCRIPTION':'This test tries to exfiltrate numbers out of your network that match the format of credit card numbers. Your network security solution should easily identify this leakage.'
                },
                            
            'Block Social Security number exfiltration': {
                'TEST NAME':'Block Social Security number exfiltration',
                'TEST URL': SOCIAL_SECURITY_NUMBER,
                'METHOD': 'get',
                'TEST DETAIL':'This test attempts to exfiltrate numbers that match the format of U.S. Social Security numbers.',
                'TEST DESCRIPTION':'This test tries to exfiltrate numbers out of your network that match the format of U.S. Social Security numbers. Your network security solution should easily identify this leakage.'
                },
        
            'Block source code exfiltration': {
                'TEST NAME':'Block source code exfiltration',
                'TEST URL': SOURCE_CODE,
                'METHOD': 'get',
                'TEST DETAIL':'This test attempts to exfiltrate typical patterns found in source code. ',
                'TEST DESCRIPTION':'This test tries to exfiltrate typical patterns found in source code. Stealing your intellectual property is the goal of some of the world most dangerous hackers and state-sponsored actors seeking a competitive advantage. A leak of intellectual property can have profound consequences for your enterprise — from rewriting source code to re-issuing binaries.'
                }
    
            }
        }
    }

#print(SECURITY_CONFIG)