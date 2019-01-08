# 自动下载枫雪动漫的海贼王种子
自动从枫雪动漫字幕组的论坛opfans.org里下载FINAL版的海贼王种子文件。

``crontab -e``

``0 3 * * * cd /home/dir/getop && python getop.py >/dev/null 2>&1``

update:
20190108:枫雪动漫改用WordPress，开启了防爬虫，增加headers模拟。

20180703:增加对V2种子的判断，只要标题带V2就下载种子。
