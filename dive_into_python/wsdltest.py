#!/usr/bin/python
# -*- coding: utf-8 -*-
#fileName:wsdltest.py

import os, re
import sys

from SOAPpy import WSDL

try:
    proxy_url=os.environ['http_proxy']
    phost, pport = re.search('http://([^:]+):([0-9]+)', proxy_url).group(1,2)
    print phost
    print pport
except:
    proxy = None

#wsdlFile='http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl'
wsdlFile='http://www.example.org/stock'
print wsdlFile
#server = WSDL.Proxy(wsdlFile, http_proxy=proxy)
print u'中文测试'