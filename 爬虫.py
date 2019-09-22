#!/usr/bin/python
#-*-coding:utf-8-*-
#网络爬虫：是一种自动获取网页内容的程序，通过python代码获取网络中存放的资源
#反爬虫：防止资源被爬虫代码获取
#反扒机制：属于反爬虫的技术手段之一，
#反扒机制最常见的 1、封IP地址  2、封物理网卡的Mac地址   3、验证码： 4、服务器传输给浏览器的数据通过异步加载
"""
re 模块
requests python 发送http/HTTPS请求，接受相应数据的一个第三库
github
"""
import  re
import requests
b={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
#get 请求获取或查询资源

#第一步：发送请求
r=requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/17125664.html',headers=b)
#第二部：获取响应的结果  content
a=r.content.decode(encoding='gbk')
print(a)

z=re.compile(r'<h2>(.*?)</h2>')
x=re.findall(z,a)
print(x)
# <br /><br />&nbsp;&nbsp;&nbsp;&nbsp;
c=re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br /><br />')
f=re.findall(c,a)
print(f)

# d=open(file='a.txt',mode='wb',encoding='utf-8')
# for i in x:
#     d.write(i)
#     d.write('\n')
# for j in f:
#     d.write('j')
#     d.write('/n')
    # # d1=open(file=a.txt,mode=r,encoding='gbk')
# print(d1.read())




#
# r=requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/',headers=b)
# a=r.content.decode(encoding='gbk')
# print(a)
# c=re.compile(r"<dd><a href=(.*?)>(.*?)</a></dd>")
# f=re.findall(c,a)
# print(f)

# class xiaoshuo(object):
#     def __init__(self):
#         self.mulu='mulu'
#     def mingling(self):
r = requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/', headers=b)
a = r.content.decode(encoding='gbk')
# print(a)
c = re.compile(r'<dd><a href="(.*?)">(.*?)</a></dd>')
f=re.findall(c,a)
# print(f)
for i in f:
    y=requests.get(url=f'https://www.fpzw.com/xiaoshuo/87/87590/{i[0]}',headers=b)
    t=y.content.decode(encoding='gbk')
    # print(t)
    # < br / > < br / > & nbsp; & nbsp; & nbsp; & nbsp
#     k=re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br /><br />')
#     d=re.findall(k,t)
#     print(d)
#
# e=open(file='b.txt',mode='w',encoding='utf-8')
# for i in f:
#     e.write(i)
#     # e.write(\n)
# for j in a:
#     e.write(j)
#     # e.write(/n)
# print(e)

# 库 包 模块
"""
模块：一个.py文件就是一个模块
包：多个.py文件组成的文件夹，python包里必须有一个__init__.py
库：有多个包，模块组成的一个集合
"""
#python with语句
#gc  垃圾回收机制，释放不被使用内存。
import  requests

