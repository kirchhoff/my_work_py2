#!/usr/bin/env python
"""python crawler """
# encoding:UTF-8

import requests
import sys
import time
name=""
password=""
def login():
    """login work"""
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, sdch, br',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36'}
    s = requests.Session()
    s.headers = headers
    post_data = {'username': name, 'password': password}
    r = s.post('http://p.nju.edu.cn/portal_io/login', data=post_data, verify=False)
    print "log in, status = %s" % r.status_code




while True:
    f = open("C:/networkLogin/account.txt","r")
    d = f.read()
    name,password=d.split(":")
    #print name,password
    login()
    time.sleep(43200)