# -*- coding: utf-8 -*-
#https://wkhtmltopdf.org/downloads.html
#https://pypi.org/project/pdfkit/
#https://www.cnblogs.com/my8100/p/7738366.html
import pdfkit
url = 'http://114.116.87.228:8001/json'
#url = 'www.baidu.com'
#url = 'https://ask.csdn.net/questions/387309'
pk = pdfkit.from_url(url,'out.pdf')