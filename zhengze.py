#!/usr/bin/python
#-*-coding:utf-8-*-
#python 正则表达式  re 正则模块
"""
1、  .  在python中表示除了换行符\以外任意一个字符
2、  *  匹配*前面的字符0次或多次
3、  +  匹配+前面的字符一次或多次
4、  ?  匹配?前面的字符0次或1次
5、  $  以某个字符结尾
6、  ^  以某个字符开头
7、  {n} 匹配前一个字符n次
8、  {n,m} 匹配前一个字符最少n次最多m次
9、
"""

"""
match :一旦匹配不到，立刻结束匹配
search： 匹配继续匹配，直到匹配成功第一次或者字符串结束为止，如果继续存在符合的字符串，不输出
共同点：匹配成功第一次后就停止
"""
import  re

s='11111123345'
#写正则的步骤
#第一步  编译正则表达式  r1代表编译完成的正则表达式
r1=re.compile(r'.')
#第二部执行正则表达式
print(re.search(r1,s))     #  search（)搜索   参数1已经编译好的正则表达式   参数二 ：要匹配的字符串

r2=re.compile(r'123*')
print(re.search(r2,s))

r3=re.compile(r'1+')
print(re.search(r3,s))

r4=re.compile(r'1?')
print(re.search(r4,s))

r5=re.compile(r'5$')
print(re.search(r5,s))

r6=re.compile(r'^1')
print(re.search(r6,s))

r7=re.compile(r'1{3}')
print(re.search(r7,s))

r8=re.compile(r'1{1,4}')
print(re.search(r8,s))

r9=re.compile(r'1[0-9]')
print(re.search(r9,s))

#过滤手机号
# d=open(r'D:\py\study\a.txt')
# for i in d:
a='1254567891234567891234'
s=re.compile(r'(123)[0-9]{8}|(345)[0-9]{8}')
print(re.search(s,a))

#\d [0-9]
#\D除了0-9以外任意一个字符
#\s 表示空白字符 \t \n \r \f \v
#\S除了空白字符以外任意字符


#贪婪模式  指的是尽可能匹配更多的字符
#fei贪婪模式 指的是匹配到符合规则的就停止匹配

#sub(参数1,2,3)  替换的意思  str.replace('旧的'，'新的')
#参数1： 正则   参数2：新的字符  参数3：被更改的字符串
#group （)  将匹配的东西拿出来
#groups()  多个分组

URL='https://www.baidu.com'
r10=re.compile(r'\.(.*)\.')
a=re.search(r10,URL).group()
b=re.sub(r'\.','',a)
print(b)

URL='https://www.baidu.comhttps://www.jd.com'
r10=re.compile(r'\.(.*?)\.')     #非贪婪模式 ？
a=re.search(r10,URL).group()      #没有问号是贪婪模式
b=re.sub(r'\.','',a)
print(b)

#findall 结果是列表，每个元素都是字符串  作用：找到所有符合正则规则的结果
URL='https://www.baidu.comhttps://www.jd.com'
r10=re.compile(r'\.(.*?)\.')
a=re.findall(r10,URL)
print(a)

#match 只匹配第一个，第一个匹配不到就停止，search是接着往后匹配，直到匹配到一个就停止。