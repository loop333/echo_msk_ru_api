#!/usr/bin/python3
# -*- coding: utf-8 -*-
import urllib.request
import json
import ssl
import re

context = ssl._create_unverified_context()
resp = urllib.request.urlopen('https://echo.msk.ru/api/news.json?fields=title,body', context=context)

t = json.load(resp)
news = t['content']

with open('news.html', 'w') as fout:
    fout.write('<html>\n')
    fout.write('<head>\n')
    fout.write('<meta charset="utf-8">\n')
    fout.write('<style>\n')
    fout.write('div {\n')
    fout.write(' margin-left: 30px;\n')
    fout.write('}\n')
    fout.write('</style>\n')
    fout.write('</head>\n')
    fout.write('<body>\n')
    for n in news:
        title = re.sub(r' +', ' ', n['title'])
        title = re.sub(r'^ +', '', title)
        body = re.sub(r' +', ' ', n['body'])
        body = re.sub(r'^ +', '', body)
        fout.write('<details>\n')
        fout.write('<summary>' + title + '</summary>\n')
        fout.write('<div>' + body + '</div>\n')
        fout.write('</details>\n')
    fout.write('</body>\n')
    fout.write('</html>\n')
