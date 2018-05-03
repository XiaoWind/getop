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

    url = "http://bbs.opfans.org/forum.php?mod=forumdisplay&fid=37"
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html = response.read()

    html = unicode(html, "gbk").encode("utf8")
    #print html

    links = re.finditer(r'<a href="(.*?)".*第(.*)话.*FINAL',html)
    for i in links:
        if int(i.group(2)) > ep:
            #link[i.group(2)] = i.group(1)
            url = "http://bbs.opfans.org/" + i.group(1)
            url = url.replace('amp;','')

            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            html = response.read()
            html = unicode(html, "gbk").encode("utf8")

            link = re.search(r'<a href="(.*?)".*torrent',html)
            link = "http://bbs.opfans.org/" + link.group(1)
            link = link.replace('amp;','')

            dd = urllib2.urlopen(link)
            with open("torrent/"+i.group(2)+".torrent","wb") as f:
                f.write(dd.read())
            #种子下载完成，只有当前集数较新时才写入ep.txt
            with open('ep.txt','r') as f:
                tempep = int(f.read())
            if int(i.group(2)) > tempep:
                with open('ep.txt','w') as f:
                    f.write(i.group(2))

if __name__ == '__main__':
    main()
