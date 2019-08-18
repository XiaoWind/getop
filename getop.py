#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import re
import os

def main():
    #检查ep文件是否存在，检查torrent文件夹是否存在
    #不存在就创建
    if not os.path.exists('ep.txt'):
        with open('ep.txt','w') as f:
            f.write('0')

    if not os.path.exists('torrent'):
        os.makedirs('torrent')

    #读取已下载过种子的链接，保存到ep
    with open('ep.txt','r') as f:
        ep = f.read()

<<<<<<< HEAD
    url = "http://www.opfans.org/" #?cat=1,FINAL分类
=======
    url = "http://www.opfans.org/?cat=1" #?cat=1,FINAL分类
>>>>>>> ep to url
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html = response.read()
    #print html

<<<<<<< HEAD
    links = re.finditer(r'<a href="([^>]*?)"[^>]*第(.*?)话.*?FINAL(.*?)>',html)
    for i in links:
        if "V2" in i.group(3) or int(i.group(2)) > ep:
            url = i.group(1)
            print url
=======
    links = re.finditer(r'<a href="([^>]*?)"[^>]*第(.*?话).*?FINAL(.*?)>',html)

    #将迭代器转成list
    links = list(links)

    for i in links:
        if i.group(1) not in ep:
            url = i.group(1)
            #print url
>>>>>>> ep to url

            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            html = response.read()

<<<<<<< HEAD
            link = re.search(r'<a href="(.*?)".*?下载地址',html)
            link = link.group(1)
            print link

            #该link有防爬虫
            headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5;Windows NT)','Referer':url}

            request = urllib2.Request(link,'',headers)
            response = urllib2.urlopen(request)
            html = response.read()

            link = re.search(r'href="(.*?torrent)"',html)
            link = link.group(1)
            print link
=======
            link = re.search(r'href="(.*?torrent)"',html)
            link = link.group(1)
            #print link
>>>>>>> ep to url

            dd = urllib2.urlopen(link)
            with open("torrent/"+i.group(2)+url.partition("=")[2]+".torrent","wb") as f:
                f.write(dd.read())

    #种子下载完成，将所有已下种子的链接写入ep.txt
    tempep = ""
    for i in links:
        tempep = tempep + i.group(1) + "\n"
    with open('ep.txt','w') as f:
        f.write(tempep)

if __name__ == '__main__':
    main()
