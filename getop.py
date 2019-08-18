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

    url = "http://www.opfans.org/?cat=1" #?cat=1,FINAL分类
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html = response.read()
    #print html

    links = re.finditer(r'<a href="([^>]*?)"[^>]*第(.*?话).*?FINAL(.*?)>',html)

    #将迭代器转成list
    links = list(links)

    for i in links:
        if i.group(1) not in ep:
            url = i.group(1)
            #print url

            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            html = response.read()

            link = re.search(r'href="(.*?torrent)"',html)
            link = link.group(1)
            #print link

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
