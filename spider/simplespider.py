#!/usr/bin/python
#filename:simplespider.py
# -*- coding: utf-8 -*-



import os
import sys
import urllib2
import requests
import re
from lxml import etree

def StringListSave(save_path, filename, slist):
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    path = save_path + "/" +filename + ".txt"
    with open(path, "w+") as fp:
        for s in slist:
            fp.write("%s\t\t%s\n" %(s[0].encode("utf8"),s[1].encode("utf8")))
def Page_Info(myPage):
    '''Regex'''
    mypage_Info = re.findall(r'<div class="titleBar" id=".*?"><h2>(.*?)</h2><div class="more"><a href="(.*?)">.*?</a></div></div>', myPage,re.S)
    return mypage_Info

def New_Page_Info(new_page):
    '''Regex(slowly) or Xpath(fast)'''
    dom = etree.HTML(new_page)
    new_items = dom.xpath('//tr/td/a/text()')
    new_urls = dom.xpath('//tr/td/a/@href')
    assert(len(new_items) == len(new_urls))
    return zip(new_items, new_urls)

def Spider(url):
    i = 0
    print 'Downloading ', url
    myPage = requests.get(url).content.decode("gbk")
    myPageResults = Page_Info(myPage)
    save_path = "163"
    filename = str(i)+"_"+"162"
    StringListSave(save_path, filename, myPageResults)
    i += 1
    for item, url in myPageResults:
        print "downloading...", url
        new_page = requests.get(url).content.decode("gbk")
        newPageResults = New_Page_Info(new_page)
        filename = str(i) + "_" +item
        StringListSave(save_path, filename, newPageResults)
        i += 1

if __name__ == "__main__":
    print "start"
    start_url = "http://news.163.com/rank/"
    Spider(start_url)
    print "end"
    
    