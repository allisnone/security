# -*- coding: utf-8 -*-
#https://wkhtmltopdf.org/downloads.html
#https://pypi.org/project/pdfkit/
#https://www.cnblogs.com/my8100/p/7738366.html
import pdfkit
url = 'http://114.116.87.228:8001/jsonp'
#url = 'www.baidu.com'
#url = 'https://ask.csdn.net/questions/387309'
url ='https://www.cnblogs.com/niejinmei/p/8157680.html'
options = { 'page-size': 'A4', 'margin-top': '0mm', 
           'margin-right': '0mm', 'margin-bottom': '0mm', 'margin-left': '0mm'}# 'orientation':'Landscape',#横向 'encoding': "UTF-8", 'no-outline': None, # 'footer-right':'[page]' 设置页码 }

pk = pdfkit.from_url(url,'out.pdf',options=options)
