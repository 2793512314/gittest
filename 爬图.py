#!/usr/bin/python
#-*-coding:utf-8-*-
import  re
import requests

class  price(object):
    b = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    def __init__(self):
        r = requests.get(url='https://www.58pic.com/newpic/28836836.html', headers=self.b)
        self.d = r.content.decode(encoding='gbk')
    def fenxi(self):

        r1 = re.compile(r'<img src="(.*?)" class="show-area-pic" id="show-area-pic')
        b = re.findall(r1, self.d)
        # print(b)
        c=[]
        for  i in b:
            c.append('https:'+i)
        return c
    def download(self):
        n=1
        for i in self.fenxi():
            e=requests.get(url=i,headers=self.b)
            jieguo=e.content
            f=open(file=f'{n}.jpg',mode='wb')
            f.write(jieguo)
            n+=1
            # print(f)

p=price()
p.download()

