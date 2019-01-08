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

    #读取已下载过种子的集数保存到ep
    with open('ep.txt','r') as f:
        ep = int(f.read())

    url = "http://www.opfans.org/" #?cat=1,FINAL分类
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html = response.read()
    #print html

    links = re.finditer(r'<a href="([^>]*?)"[^>]*第(.*?)话.*?FINAL(.*?)>',html)
    for i in links:
        if "V2" in i.group(3) or int(i.group(2)) > ep:
            url = i.group(1)
            print url

            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            html = response.read()

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

            dd = urllib2.urlopen(link)
            isv2 = ""
            if "V2" in i.group(3):
                isv2 = "v2"
            with open("torrent/"+i.group(2)+isv2+".torrent","wb") as f:
                f.write(dd.read())
            #种子下载完成，只有当前集数较新时才写入ep.txt
            with open('ep.txt','r') as f:
                tempep = int(f.read())
            if int(i.group(2)) > tempep:
                with open('ep.txt','w') as f:
                    f.write(i.group(2))

if __name__ == '__main__':
    main()
