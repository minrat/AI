#!/usr/bin/python
# -*- coding: UTF-8 -*-

from urllib import request
from bs4 import BeautifulSoup

response = request.urlopen("https://movie.douban.com/chart")
html = response.read()
soup = BeautifulSoup(html, features="html")
# 有效的URL
links = soup.select('a[class=""]')
# 带有无效的URL信息
# links = soup.select('a[href]')

for link in links:
    print(link.get("href"))
