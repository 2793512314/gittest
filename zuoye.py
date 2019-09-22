#!/usr/bin/python
# -*-coding:utf-8-*-
#  判断成绩
'''
while True:
    a = int (input("请输入你的成绩："))
    if a > 90 and a <= 100:
        print("优秀")
    elif a > 80 and a <= 90:
        print("良好")
    elif a >=60 and a <=80:
        print("一般")
    elif a < 60 and a >= 0 :
        print("不及格")
    else:
        print("输入的成绩格式有误")
'''

#  将列表去重

a = [1 ,2 ,3,1,2,3,3,4,5,5,5]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)


#  99乘法表

for i in range(1,10):
    for j in range(1,i+1):
        if i >= j:
            print("{} * {} = {}".format(j,i,i*j),end="    ") # end 是一个结束标志
            # print(j,'*',i,'=',i*j,'\t',end='')
print("  ")


#  登录信息 输入3次密码失败就在跳转到输入用户名
'''
print("天猫登录功能")
dict = {"admin":"1234","user1":"4321"}
while True:
    name = input ("请输入用户名：")
    if name in dict.keys():
        passwd = input("请输入你的密码:")
        if passwd == dict[name]:
            print("登录成功")
            break
        else:
            print("登录失败")
    else:
        print("请重新输入")
'''

#  字典查东西的
'''
d = {
    "data": {
        "msg":
        [
            {
                "s_1": ["Jim", "男",  19, "175cm"],
                "country": "美国"
            },
            {
                "s_2": ["Kity", "女",  17, "165cm"],
                "country": "法国"
            },
            {
                "s_3": ["Tom", "男",  19, "173cm"],
                "country": "美国"
            },
            {
                "s_4": ["拖拉斯基", "男",  18, "180cm"],
                "country": "俄罗斯"
            },
            {
                "s_5": ["阿卡丽", "女",  17, "175cm"],
                "country": "乌克兰"
            },
            {
                "s_6": ["牙买稻子", "女",  18, "161cm"],
                "country": "日本"
            },
            {
                "s_7": ["龟田一郎", "男",  19, "175cm"],
                "country": "日本"
            },
            {
                "s_8": ["张三", "男",  20, "180cm"],
                "country": "中国"
            },
            {
                "s_9": ["李秀琴", "女",  19, "175cm"],
                "country": "中国"
            },
            {
                "s_10": ["宋仲基", "女",  19, "175cm"],
                "country": "韩国"
            },
            {
                "s_11": ["金正鞋", "男",  19, "168cm"],
                "country": "朝鲜"
            },
            {
                "s_12": ["卡列夫斯基", "男",  21, "190cm"],
                "country": "俄罗斯"
            },
        ]
    },
}

a = []
country_1 = []
name = []
height = []
sex = []
for i in d['data']['msg']:
    # print(i)
    for j in i.values():
        # print(j)
        if type(j) == list:
            a.append(j)
            # print(a)
        else:
            country_1.append(j)
# print(country_1)
for b in a:
# print(b)
    name.append(b[0])
    # print(name)
    sex.append(b[1])
    # print(sex)
    height.append(b[3])
    # print(height)
# 求国家个数
print(len(set(country_1)))
# # 求所有学生的身高范围
print(f'最大值为：{max(height)}，最小值为：{min(height)}')
# 求统计男女比例
print(f'男生的数量：{sex.count("男")},女生的数量：{sex.count("女")},比例是：{sex.count("男")/sex.count("女")}')
# 求平均身高
# print(height)
a = str(height).replace('cm','')
# b = []
# # b.append(int(a[2:5]))
# i = 2
# while i < len(a):
#     b.append(int(a[i:(i + 3)]))
#     i += 7
#     # print(b)
# print(f'平均身高是：{sum(b) / len(b)}')
# # 查询身高在170到180之间的学生名
# for i in range(12):
#     if 170 <= b[i] <= 180:
#         print(name[i])

# a = []
# b = []
# c = []
# for i in d["data"]["msg"][0:12]:
#     print(i)
#     a.append(i)
# # print(a)
# for g in range(0,12):
#     # print(a[g]["country"])
#     f = a[g]["country"]
#     b.append(f)
# # print(b)
# for k in b :
#     if k not in c:
#         c.append(k)
# # print(c)
# print(len(c))
# # 求所有学生的身高范围
# a = []
# b = []
# c = []
# e = []
# p = 5
# for i in d["data"]["msg"][0:12]:
#     # print(i)
#     a.append(i)
# # print(a)
# for g in range(0,12):
#     # print(a[g])
#     for j in a[g].keys():
#         b.append(j)
#         b.append(a[g][j])
# print(b)
# print(len(b))
# c.append(b[1])
# while p <= len(b):
#         c.append(b[p])
#         p += 4
# # print(c)
# # print(len(c))
# for x in range(0,12):
#     # print(c[x][3])
#     e.append(c[x][3])
# print(e)
# print("身高范围是： %s 到 %s"%(min(e),max(e)))

# 求统计男女比例
# a = []
# b = []
# c = []
# e = []
# p = 5
# for i in d["data"]["msg"][0:12]:
#     # print(i)
#     a.append(i)
# # print(a)
# for g in range(0,12):
#     # print(a[g])
#     for j in a[g].keys():
#         b.append(j)
#         b.append(a[g][j])
# print(b)
# print(len(b))
# c.append(b[1])
# while p <= len(b):
#         c.append(b[p])
#         p += 4
# print(c)
# # print(len(c))
# for x in range(0,12):
#     # print(c[x][3])
#     e.append(c[x][1])
# # print(e)
# print("男女比例是：{}:{}".format(e.count("男"),e.count("女")))


# 求平均身高
# a = []
# b = []
# c = []
# e = []
# h = []
# q = 2
# p = 5
# for i in d["data"]["msg"][0:12]:
#     # print(i)
#     a.append(i)
# # print(a)
# for g in range(0,12):
#     # print(a[g])
#     for j in a[g].keys():
#         b.append(j)
#         b.append(a[g][j])
# # print(b)
# # print(len(b))
# c.append(b[1])
# while p <= len(b):
#         c.append(b[p])
#         p += 4
# # print(c)
# # print(len(c))
# for x in range(0,12):
#     # print(c[x][3])
#     e.append(c[x][3])
# print(e)
# z = str(e)
# h.append(int(z[2:5]))
# # print(e[11:14])
# # print(e[20:23])
# while q <= len(z):
#     h.append(int(z[q:q+3]))
#     q += 9
# print(h)
# # print(sum(h))
# y = sum(h) / len(h)
# print("平均身高为： {}".format(y))

# 查询身高在170到180之间的学生名字
# a = []
# b = []
# c = []
# nv = []
# e = []
# h = []
# q = 2
# p = 5
# for i in d["data"]["msg"][0:12]:
#     # print(i)
#     a.append(i)
# # print(a)
# for g in range(0,12):
#     # print(a[g])
#     for j in a[g].keys():
#         b.append(j)
#         b.append(a[g][j])
# # print(b)
# # print(len(b))
# c.append(b[1])
# while p <= len(b):
#         c.append(b[p])
#         p += 4
# print(c)
# # print(len(c))
# for x in range(0,12):
#     # print(c[x][3])
#     e.append(c[x][3])
# # print(e)
# z = str(e)
# h.append(int(z[2:5]))
# # print(e[11:14])
# # print(e[20:23])
# while q <= len(z):
#     h.append(int(z[q:q+3]))
#     q += 9
# # print(h)
#
# # de dao ['Jim', 'Kity', 'Tom', '拖拉斯基', '阿卡丽', '牙买稻子', '龟田一郎', '张三', '李秀琴', '宋仲基', '金正鞋', '卡列夫斯基']
# for xx in range(0,12):
#     # print(c[xx][3])
#     nv.append(c[xx][0])
# # print(nv)
#
# dict = {}
# for ii in range(0,12):
#     dict[nv[ii]] = h[ii]
# # print(dict)
#
# name_q = []
# # if dict[dict.keys()] <= 180 and dict[dict.keys()] >= 170:
# #     print(dict.keys())
# for name,num in dict.items():
#     if dict[name] <= 180 and dict[name] >= 170:
#         # print(name)
#         name_q.append(name)
# print(name_q)
'''

#  字符串
'''
text = "Early in the day it was whispered that we should sail in a boat, only thou and I, and never a soul in the world would know of this our pilgrimage to no country and to no end"
# 1、将text中每个首字符大写的英文单词添加到一个列表中
# a = text.split(" ")
# # print(a)
# b = []
# for i in a:
#     t = ord(i[0])
#     # print(t)
#     if  65 < t <97: # houzhe  if  a.istitle():
#         b.append(i)
# print(b)

# 2、将首字符小写的单词转换为首字符大写

# a = text.split(" ")
# b = ' '.join(a)
# # print(a)
# # print(b)
# c = b.title()
# print(type(c))
# print(c)
# d = list(c)
#
# q = ' '.join(d)
# print(type(q))
# print(q)


# 3、将text中所有的包含a的字符替换成博文两个字

# a = text.replace('a',"博文")
# print(a)

# # 4、删除包含小t字符的单词后，组成一个新的字符串
# a = text.split(" ")
# print(a)
# for i in range(len(a) - 1) :
#     for j in a:
#       if "t" in  j:
#           a.remove(j)
# print(a)
# # print(type(a))
# b = ' '.join(a)
# print(b)

# a = 'a ad af sd dff'
# b = a.split()
# for i in range(len(b)-1):
#     print(i)
#     for j in b:
#         print(j)
#         if "a" in j:
#             b.remove(j)
#             print(b)
# print(b)
'''

#  回文 输入一个字符串 判断字符串是不是回文     aba 或者abba 的格式
'''
a = input("请输入一个字符串 :")
n,m = 0,0
# print(a)
b = a[::-1]
# print(b)
for i in range(0,len(a)):
    if b[i] == a[i]:
        n += 1
    else:
        m += 1
if m >= 1:
    print("这不是回文")
else:
    print('这是回文')
'''

#  排序
'''
# 冒泡排序
# a = list(input("请输入一组数据:"))
# print(a)
# for i in range(0,len(a)-1):
#     for j in range(0,len(a)-i-1):
#         if a[j] > a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]
# print(a)


def maopao(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j+1]:
                list[j] , list[j + 1] = list[j + 1] , list[j]
    return list
# print(maopao([2,1,5,6,8]))

a =input( "请输入一组数：" )
while True:
    if a.isdigit():
        print(maopao(list(a)))
        break
    else:
        print('请重新输入')


# 选择排序
a = list(input("请输入一组数据:"))
print(a)
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if a[j] > a[i]:
            a[j],a[i] = a[i],a[j]
print(a)


'''

#  超市计算
'''
a = ["香蕉","菠萝","提子","胡萝卜"]
b = [100,80,50,30]
merber = {'1001':'12345','1002':'54321'}
sum = 0

print(f"产品编号\t\t\t产品名称\t\t\t产品单价")
for i,j in enumerate(a):
    print(f"{i}\t\t\t\t{j}\t\t\t\t{b[i]}")

while True:
    c = int ( input( "请选择购物编号(购物编号为0,1,2,3)，退出按4）:" ) )

    if c <= 3:
        print(f"您要选购的是{a[c]}")
        num = int ( input( "请选择购买数量 :") )
    if c == 0:
        sum += b[0] * num
        continue
    elif c == 1:
        sum += b[1] * num
        continue
    elif c == 2:
        sum += b[2] * num
        continue
    elif c == 3:
        sum += b[3] * num
        continue
    else:
        break
sum = float(sum)
while True:
    mer = input("您的会员卡号：")
    if mer in merber.keys():
        #print("请输入您的会员卡密码！")
        passwd = input("您的密码是:")
        if passwd == merber[mer]:
            sum *= 0.95
            break
        else:
            for p in range(3):
                print("请重新输入您的密码")
                passwd = input("你的密码是:")
                if passwd == merber[mer]:
                    sum *= 0.95
                    break
                else:
                    print(f"你还有 {2 - p} 次机会")
            else:
                print("请去服务台寻求帮助")
                break
    else:
        print("您不是会员")
        break

# mer = input("您是不是会员（Y是会员，N不是会员）：")
# if mer == 'Y':
#     sum *= 0.95
print(f"您要支付{sum}")
'''

#  1 2 3 4 可以形成多少个3位数
'''
a = '1234'
b = []
for i in a:
    # print(i)
    for j in a :
        # print(j)
        for z in a :
            # print(z)
            if i != j and  i != z and j != z:
                b.append(f'{i}{j}{z}')
set(b)
# print(c)
sum = 0
for q in b:
    # print(q)
    sum += 1
print(sum)
'''

#  字符串类型在不适用int的情况下转int '123456'
'''
# str = '123456'
# sum = 0
# for i,j in enumerate(str):
#     print(f'{i}\t\t\t{j}')
# for z in range(i + 1):
#     # print(z)
#     a = ( 10 ** z ) * ( 6 - z )
#     sum += a
#     # print(f'{sum}')
# print(f'{sum}')
# print(type(sum))


# import time
# str_1 = '123409'
# sum = 0
# c = len(str_1)
# # for i,j in enumerate(str_1):
# #     # print(f'{i}\t\t\t{j}')
# for j in str_1:
#     # print(j)
#     for k in range(10):
#         if str(k) == j:
#             a = ( 10 ** c ) * k
#             sum += a
#             # print(f'{sum}')
#             c = c - 1
# print(f'{sum}')
# print(type(sum))
'''

#  一张纸0.08mm 珠穆朗玛峰高8848m 求多少次能到珠穆朗玛峰高度
'''
num = 0
s = 0.08
t = 8848*1000
while t >= s:
    s *= 2
    num += 1
print(num)
'''

#  账号长度在6～8之间为合法的账号
#  密码的长度在5～7之间为合法的密码
#  账号和密码都符合上述要求，将账号密码以键值对的形式保存
'''
aount = ["ads", "dafdsa"," jjajs", "dfdsdas"]
passwd = ["fdsfd", "fdsfdsaffdsa", "", "jjja", '213232']
dict = {}
list_1 = []
list_2 = []
for i in range(len(aount)):
    if len(aount[i]) >= 6 and len(aount[i]) <= 8:
        list_1.append(aount[i])
print(list_1)
for a in range(len(passwd)):
    if len(passwd[a]) >= 5 and len(passwd[a]) <= 7:
        list_2.append(passwd[a])
print(list_2)
for z in range( len(list_2) ):
     dict[f'{list_1[z]}'] = list_2[z]
print(dict)
# d = dict.fromkeys(list_1,list_2)
# print(d)
'''

#  质数之和 1 100
'''
# s = 2
# for i in range(2,101):
#     for j in range(2,i):
#         if (i % j) == 0:
#             break
#     # else:
#     #     s += i
#         elif j == i - 1:
#             s += i
# print(s)

def add(x):
    s = 2
    for i in range(2 , x):
        for j in range(2 , i):
            if (i % j) == 0:
                break
            elif j == i - 1:
                s += i
    return s
num = int(input("请输入一个正整数："))
print(add(num))
'''

#  水仙花数 100 到1000
'''
for i in range(100,1000):
    a = i // 100
    b = (i - a * 100) // 10
    c = i - a * 100 - b * 10
    s1 = a * a * a
    s2 = b * b * b
    s3 = c * c * c
    s = s1 + s2 + s3
    if s == i:
        print(f'水仙花有：{i}')
        
        
def sxh():
    for i in range(100,1000):
        a = i // 100
        b = (i - a * 100) // 10
        c = i - a * 100 - b * 10
        s1 = a * a * a
        s2 = b * b * b
        s3 = c * c * c
        s = s1 + s2 + s3
        if s == i:
            print(f"水仙花数为{i}")
sxh()
'''

#  任意数阶乘之和
'''
sum = 0
while 1:
    num = input("请输入一个数：")
    if num.isdigit() and int(num) >= 0 and type(num) != float:
        break
v = int(num)
for b in range(1,v + 1):
    a = 1
    for c in range(1,b + 1):
        a *= c
    sum += a
    print(sum)


# a = input('请输入一个正整数:')
# b = 0
# c = 1
# for i in range(1,int(a)+1):
#     c = c * i
#     b = b + c
# print(b)

def jc(x):
    a = 1
    s = 0
    for i in range(1,x + 1):
        a = a * i
        s += a
    return s
x = int(input("请输入一个正整数:"))
print(f"{x}的阶乘和是：{jc(x)}")
'''

#  验证码 数字 字母 大小写  随机6个数 组成验证码  看不清 换个验证码  输入验证码 正确 输出正确 没有输入正确 ①再次输入 ② 不再输入 退出
'''
import random
a = []
str = '0123456789abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(6):
    a.append(random.choice(str))
    b = ''.join(a)
    # print(b)
print(f'随机产生的验证码是：{b}')
while True:
    look_1 = input("是否更换验证码(输入y就是更换，输入其他就是不更换):")
    if look_1 == 'y':
        a.clear()
        for i in range(6):
            a.append(random.choice(str))
        # print(a)
        b = ''.join(a)
        print(b)
    else:
        b = ''.join(a)
        print(b)
        break
shuru = input("请输入你看到的验证码：")
print(f'我们输入的验证码是：{shuru}')
while True:
    # 不会区分大小写
    b.upper()
    shuru.upper()
    if b == shuru:
        print("你输入的正确")
        break
    else:
        print('输入错误')
        chioce = input("请选择你下面的操作（q 标识 你放弃 e 标识你再次输入）:")
        if chioce == 'q':
            break
        else:
            print("请重新输入")
            shuru = list(input("请输入你看到的验证码："))
            continue
'''

# [1,3,4,7] 转 [3,4,7,1]
'''
a = [1,3,4,7]
b = []
# 右移
# for i in range(len(a)):
#     b.append(a[i - 1])
# print(b)
# 左移
# for i in range(1,len(a)):
#     print(i)
#     b.append(a[i])
# b.append(a[0])
# print(b)
'''

#  定义一个可以输入可变长参数的函数
#  如果输入的参数个数为0，提示信息“请为参数赋值，输入2个或者4个数字，英文逗号分隔”
#  如果输入的参数为2个，求这个两个数范围内的阶乘之和，例如输入的是1,5 就是求1到5的阶乘
#  如果有四个数，求能组成多少个不同的数
#  其他情况一律提示该函数不执行
'''
# def func(*args):
#     a = len(args)
#     if a == 0:
#         return "请为参数赋值，输入2个或者4个数字，英文逗号分隔"
#     elif a == 2:
#         start = min(args)
#         stop  = max(args)
#         s = 0
#         b = 1
#         for i in range(start , stop + 1):
#             b *= i
#             s += b
#         return s
#     elif a == 4:
#         list_1 = []
#         s = 0
#         for a1 in args:
#             for a2 in args:
#                 for a3 in args:
#                     for a4 in args:
#                         if a1 != a2 and a1 != a3 and a1 != a4 and a2 != a3 and a2 != a4 and a3 != a4:
#                         # if a1 != a2 != a3 != a4:
#                             list_1.append(f'{a1}{a2}{a3}{a4}')
#                             s += 1
#         return s
#     else:
#         return "该函数不执行"
# print(func())
# print(func(1,5))
# print(func(2,4,3,1))
# print(func(1))
'''

#  定义一个函数，函数有一个可变长参数：kwargs
#  问题一：获取kwargs传入的所有键和值
#  问题二：判断kwargs的所有的值的类型，统计有多少字符串，列表和元组 集合 数字 字典类型的个数
#  问题三：如果有某个类型的值大于3，函数终止，并返回由这些类型的值组成的列表
'''
# def func(**kwargs):
#     print(kwargs.items())
#     s = 0
#     a = []
#     count = 0
#     q, w, e, r, t, y = 0, 0, 0, 0, 0, 0
#     # for i,j in kwargs.items():
#     #     # print(type(j))
#     #     if type(j) == str:
#     #         q += 1
#     #     elif type(j) == list:
#     #         w += 1
#     #     elif type(j) == dict:
#     #         e += 1
#     #     elif type(j) == set:
#     #         r += 1
#     #     elif type(j) == tuple:
#     #         t += 1
#     #     else:
#     #         y += 1
#     # print(f'字符串的个数{q}')
#     # print(f'列表的个数{w}')
#     # print(f'字典的个数{e}')
#     # print(f'集合的个数{r}')
#     # print(f'元组的个数{t}')
#     # print(f'整型的个数{y}')
#     c = {}
#     for i, j in kwargs.items():
#         # print(type(j))
#         if type(j) == str:
#             q += 1
#             c[i] = j
#             if q > 3:
#                 print(c)
#                 break
#         elif type(j) == list:
#             w += 1
#             c[i] = j
#             if w > 3:
#                 print(c)
#                 break
#         elif type(j) == dict:
#             e += 1
#             c[i] = j
#             if e > 3:
#                 print(c)
#                 break
#         elif type(j) == set:
#             r += 1
#             c[i] = j
#             if r > 3:
#                 print(c)
#                 break
#         elif type(j) == tuple:
#             t += 1
#             c[i] = j
#             if t > 3:
#                 print(c)
#                 break
#         else:
#             y += 1
#             c[i] = j
#             if y > 3:
#                 print(c)
#                 break
#
#
# func(a1 = 1,a2 = 2,a3 = [1,2,3],a4  = 'a',a5 = 'b',a6 = ['p'],
#            a7 = {1,2},a8 = {'a':1},a9 = ['a'],a10 = ['n'],a11 = 7,a12=('a',) )

# def func(**kwargs):
#     print(kwargs.keys())
#     print(kwargs.values())
#     yz=[]
#     list_1=[]
#     str_1=[]
#     jih=[]
#     dict_1=[]
#     int_1=[]
#     for i in kwargs.values():
#         if type(i) == tuple:
#             yz.append(i)
#             if len(yz) > 3:
#                 break
#         elif type(i) == list:
#             list_1.append(i)
#             if len(list_1) > 3:
#                 break
#         elif  type(i) == str:
#             str_1.append(i)
#             if len(str_1) > 3:
#                 break
#         elif type(i) == dict:
#             dict_1.append(i)
#             if len(dict_1) > 3:
#                 break
#         elif type(i) == int:
#             int_1.append(i)
#             if len(int_1) > 3:
#                 break
#         else:
#             jih.append(i)
#             if len(jih) > 3:
#                 break
#     print('字符串元素有', len(str_1), '个')
#     print('元组元素有', len(yz), '个')
#     print('数值元素有', len(int_1), '个')
#     print('字典元素有', len(dict_1), '个')
#     print('列表元素有', len(list_1), '个')
#     print('集合元素有', len(jih), '个')
#     print(str_1)
#     print(yz)
#     print(int_1)
#     print(dict_1)
#     print(list_1)
#     print(jih)
# func(a1 = 1,a2 = 2,a3 = [1,2,3],a4  = 'a',a5 = 'b',a6 = ['p'],
#            a7 = {1,2},a8 = {'a':1},a9 = ['a'],a10 = ['n'],a11 = 7,a12=('a',))
'''

#  定义一个函数，函数：有个必填参数x，一个默认参数y = 【1,2,3,4,5,6,7,8,9】
#  问题一： 如果必填的参数在默认参数内，则将有中对应的该数字的索引值之前的所有元素依次放到列表的后面
#  例如：x传入的值是2 那么新列表y是 【3,4,5,6,7,8,9,1,2】
#  问题二：如果不在列表中，随机删除2个元素，再将x的值插入到列表索引值为5的位置
'''
# import random
#
# k = []
# v = []
#
#
# def func(x, y=[1, 2, 3, 4, 5, 6, 7, 8, 9]):
#     print(f'x的值为：{x} , y的值为：{y}')
#     if x in y:
#         for j in range(x, len(y)):
#             v.append(y[j])
#         for q in range(0, x):
#             v.append(y[q])
#         return f'x的值为：{x} , y的值为：{v}'
#         # weizhi = y.index(x)
#         # for i in range(weizhi + 1):
#         #     y.append(y[0])
#         #     y.pop(0)
#         # return y
#     else:
#         for i in range(2):
#             a = random.choice(y)
#             k.append(a)
#         print(f'随机数为：{k}')
#         y.remove(k[0]),y.remove(k[1]),y.insert(5, x)
#         return f'x的值为：{x} , y的值为：{y}'
#
# # print(func(2))
# # print(func(0))
# b = input("请输入:")
# if b.isdigit():
#     print(func(int(b)))
'''

#  定义函数一：参数x为必填参数，参数y为可变参数
#  求函数一传入的x的值 + 传入y 的值的和
#  定义函数二： 必填参数z，z传入的是个列表，例如z --》【'a','b',1】
#  要求：以z作为字典的键，函数一的返回值作为字典的值，组成新字典
'''
d = {}
def func1(x , *args):
    # print(x,args)
    b = sum(args)
    s = x + b
    return s

def func2(z):kik
    return z

i = func1(1,1,2)
y = func2([1,2,3])
e = d.fromkeys(y,i)
print(e)
'''

#  设计一个用户登录都生成session的函数，x为用户名，y为密码
#  当用户密码都输入正确时，将用户名和密码组成一个新的字符串。随机取6~8位字符作为用户登录后的session
#  当用户名和密码组成的字符串‘A’长度小于8位时，自动添加0到9任意数字到‘A’，再随机生成6到8位字符作为用户登录的session
'''
import random
d = {'admin':'12345','abc':'123','user':'54321'}


def session(x, y):
    A = ''
    for i, c in d.items():
        if x == i and d[i] == y:
            A = x + y
            while True:
                if len(A) >= 8:
                    a = random.randint(6, 8)
                    b = ''
                    for j in range(a):
                        q = random.choice(A)
                        b += q
                    return f'这是session：{b}'
                else:
                    e = random.randint(0, 9)
                    f = str(e)
                    A += f
    else:
        return '请重新输入用户名和密码'

print(session('admin', '12345'))
print(session('abc', '123'))
print(session('admin', 2))
'''

#  写两个函数，函数一：读取电脑中任意位置的txt文件，读取文件所有的内容
#  函数2：向TXT文件中写入数据，可以追加写入数据，保存文件位置由使用者自己选择
'''
# 查找所有的文件文件名字
# import os
# # file_1 = os.listdir(path='E:\培训\二阶段学习\linux学习')
# # for i in file_1:
# #     print(i)
# # print(file_1)
#
#
# def func1():
#     file_1 = os.listdir(path='E:\培训\二阶段学习\linux学习\新建文件夹')
#     for i in file_1:
#         f1 = open(file=i,encoding='utf-8')
#     print(f1.read())
#
#
# def func2(filename,x):
#     f2 = open(file=filename,mode='w',encoding='utf-8')
#     f2.write(x)
#
# print(func1())
# # print(func2('d.txt','adadad'))

'''

# 创建一个狗类，将狗的行为定义成方法，狗的行为有吃 喝 跑 叫
# 将狗的特征定义成属性，狗的特征有毛色 品种  几条腿  狗的身高  体重
# 定义方法输出狗的特征【可以是一个或者多个】
# 思考：狗的几条腿是定义成类属性还是对象属性合适？
# 要求：
# 1. 定义类
# 2. 定义属性【类属性】
# 3. 定义方法
# 4. 不同的对象对应不同的狗
#
# 例如：藏獒作为狗对象;4 条腿  灰色  140cm  50 kg  遇到人会叫  饿了会吃 渴了会喝水 挨打会逃跑
'''
class Dog(object):
    dog_leg = '4 条腿'

    def __init__(self, dog_name, dog_color, dog_height, dog_weight):
        self.dog_name = dog_name
        self.dog_color = dog_color
        self.dog_height = dog_height
        self.dog_weight = dog_weight

    def eat(self, e):
        self.e = e
        if self.e == '饿':
            print(f'{self.dog_name}饿了要吃东西了')
        else:
            print(f'{self.dog_name}不饿，不需要吃东西')

    def thirst(self, k):
        self.k = k
        if self.k == '渴':
            print(f'{self.dog_name}渴了要喝水了')
        else:
            print(f'{self.dog_name}不渴，不需要喝水')

    def do(self, d):
        self.d = d
        if self.d == '跑':
            print(f'{self.dog_name}挨打了会逃跑')
        else:
            print(f'{self.dog_name}没有人打，很乖')

    def call(self, r):
        self.r = r
        if self.r == '人':
            print(f'{self.dog_name}看到人了，要叫')
        else:
            print(f'{self.dog_name}没有看到人，不会叫')

    def tedian(self):
        print(f'dog的名字是:{self.dog_name}')
        print(f'dog的颜色是：{self.dog_color}')
        print(f'dog的高度是：{self.dog_height}')
        print(f'dog的体重是：{self.dog_weight}')
        print(f'dog腿的个数是：{self.dog_leg}')


a = Dog('藏獒','黑色','140cm','50kg')
a.tedian()
a.do('跑')
a.call('人')
a.thirst('渴')
a.eat('饿')

'''

# 图书管理系统
# 1.查询图书
# 2.增加图书
# 3.借阅图书
# 4.归还图书
# 5.退出系统
# 书：书名 作者 状态
# d = {1: ['','',''],2:['','',''],3:['','',''],4:['','','']}
"""
class Book(object):

    d = {1: ['小', '王', 'in'], 2: ['鸡', '网', 'in'], 3: ['吃', '忘', 'out'], 4: ['米', '往', 'in']}

    def look(self):   #  查看所有图书
        for i, j in self.d.items():
            print(f'所有的图书编号为:{i}\t\t图书信息为：{j}')

    def add(self, j):  # 添加图书
        self.j = j
        if self.j == 'j':
            e = input("请输入一个字典（格式：self.con: [self.book_name, self.book_writer, self.book_in]）：")
            # print(e)
            # print(type(e))
            a = e.split(':')
            # print(a)
            b = {}
            c = b.fromkeys(a[0],a[1])
            # print(c)
            self.d.update(c)
            # for i, j in self.d.items():
            #     print(f'所有的图书编号为:{i}\t\t图书信息为：{j}')
            print('添加成功')

    def chaxue(self, q):  # 查询图书，按编号查询，或者按书名
        self.q = q
        if self.q == 'q':
            a = int(input("请输入你要查询的内容："))
            print(a)
            for i, j in self.d.items():
                if i == a:
                    print(f'图书编号为:{i}\t\t图书信息为：{j}')
                    break
                else:
                    print('本图书馆没有此图书')
                    break

    def jeiyue(self, w):   # 借阅图书，把状态改为out
        self.w = w
        a = int (input("输入你想借的书："))
        for i, j in self.d.items():
            if i == a:
                j.pop(2)
                j.append('out')
                for i, j in self.d.items():
                    print(f'所有的图书编号为:{i}\t\t图书信息为：{j}')
                break
            else:
                print('不借书')
                break

    def guihuai(self, e):  # 归还图书，把状态改为in
        self.e = e
        a = int(input("输入你想还的书："))
        for i, j in self.d.items():
            if i == a:
                j.pop(2)
                j.append('in')
                for i, j in self.d.items():
                    print(f'所有的图书编号为:{i}\t\t图书信息为：{j}')
                break
            else:
                print('不还书')
                break

    def exit(self, r):     #退出系统，显示谢谢使用
        self.r = r
        if self.r == 'r':
            print("谢谢您的使用，欢迎下次使用！！！")
        else:
            print('请继续使用')


# book1 = Book(1, '小', '王', 'in')
book1 = Book()
book1.look()

# 添加操作
book1.add('j')
# 5:['一', '望', 'in']

# 查询操作
# book1.chaxue('q')
# 1   小

# 借阅操作
# book1.jeiyue('w')

# 还书操作
book1.guihuai('e')
"""


"""
功能描述：
   1.图书管理系统中的用户分为三类：管理员，已注册学生和未注册学生
   2.进入图书管理系统后首先选择身份，并且进行密码验证
     管理员的密码唯一且给定；
     学生的用户名和密码提前存储在字典中，以键和键值（键值对）的形式；
     输入密码错误提示重新输入；
     未注册学生先注册帐号，再进行登陆。
   3.管理员的功能有(1)显示所有图书(2)增加图书(3)退出，可以循环输入操作
   4.学生的功能有(1)显示所有图书(2)借书(3)还书(4)退出，可以循环输入操作

   面向对象，类，对象，描述：
   1.定义书类，保存书名，书的作者，书的数量(书的初始数量自由设定，大于0表示还有)和书所在的楼层
   2.定义identity类，定义两种用户的认证方法
   3.定义Menu类，定义两种用户的功能(静态方法)，不用实例化对象就可调用
     管理员用户有(1)查看所有图书(2)查找图书(3)增加图书(4)退出系统 4个功能
     学生用户有 (1)查看所有图书(2)借阅图书(3)归还图书(4)退出系统 4个功能
   4.定义choice类，里边保存管理员和用户的各种方法（全部定义为静态）
   5.实例化书的对象，调用identity类中的方法
"""
"""
class Book(object):
    def __init__(self, name, author, count, place):
        # 定义属性书名
        self.name = name
        # 定义属性书的作者
        self.author = author
        # 定义书的数量
        self.count = count
        # 定义书的位置，便于读者找到
        self.place = place

    def __str__(self):
        if self.count == 0:
            count = 'OUT'
        else:
            count ='IN'
        return f'{self.name}'


class identity(object):
    # 定义存储用户名和密码的字典
    StudentDict = {'lily': '123',
                   'lucy': '456',
                   'jay': '789'}

    # 定义静态方法选择身份
    @staticmethod
    def Choice():
        print('*' * 50)
        print('\033[5;31;2m\t\t\t\t欢迎使用图书管理系统\033[0m\n')
        answer = input('  请选择您的身份:[1] 管理员 [2] 学生帐号 [3] 注册帐号\n')
        if answer == '1':
            # 如果选择是1，调用管理员的验证函数
            identity.ManagerIdentity()
        elif answer == '3':
            # 如果选择是3，选择注册一个新的学生帐号，并调用验证函数登陆
            name = input('注册新用户———请输入您的姓名：')
            code = input('注册新用户———请输入您的密码：')
            identity.StudentDict[name] = code
            print('***您已成功注册图书管理系统学生用户，请登陆：***')
            identity.StudentIdentity()
        elif answer =='2':
            # 如果选择是2，调用学生用户的验证函数
            identity.StudentIdentity()
        else:
            print('***您的选择错误，不能登陆！***')

    # 定义类方法验证管理员信息，管理员的密码是123456，身份唯一
    @classmethod
    def ManagerIdentity(cls):
        # 管理员的验证函数
        passwd1 = input('请输入您的密码：')
        print ('')
        print('*' * 50)
        if passwd1 == '123456':
            print('\033[5;31;2m\t\t您的身份是管理员，欢迎进入图书管理系统\033[0m')
            Menu.ManagerMenu()
        else:
            print('您的密码错误！请重新输入：')
            cls.ManagerIdentity()

    # 定义类方法验证学生信息
    @classmethod
    def StudentIdentity(cls):
        # 学生信息的验证函数
        username =input('请输入您的帐号：')
        passwd2 = input('请输入您的密码：')
        print (' ')
        print ('*' * 50)
        for key in cls.StudentDict:
            if (key == username and cls.StudentDict[key] == passwd2):
                print('\033[5;31;2m\t\t您的身份是学生，欢迎您进入图书管理系统\033[0m')
                Menu.StudentMenu()
                return
        print('您的用户名或身份不正确！请重新输入：')
        cls.StudentIdentity()


class Menu(object):
    # 定义菜单类，学生和管理员有不同的选择
    @staticmethod
    def StudentMenu():
        # 定义学生选择菜单函数,这是静态方法，不用实例化对象即可调用
        print('')
        print('[1]查看所有藏书\n')
        print('[2]借阅图书\n')
        print('[3]归还图书\n')
        print('[0]退出系统\n')
        while True:
            studentchoice = input('请选择您要进行的操作：')
            if studentchoice == '1':
                # 学生查看所有图书部分
                choice.StudentSee()
            elif studentchoice =='2':
                # 学生借书部分
                choice.StudentBorrow()
            elif studentchoice == '3':
                choice.StudentGive()
            elif studentchoice =='0':
                # 学生退出菜单部分
                print('')
                print('\033[5;31;2m***欢迎再次使用图书管理系统***\033[0m')
                break
            else:
                print('您的输入不正确，请输入[1]查看所有藏书[2]借书[3]还书[0]退出系统\n')


    @staticmethod
    def ManagerMenu():
        # 定义管理员选择菜单函数
        print('')
        print('[1]查看所有藏书\n')
        print('[2]查询图书\n')
        print('[3]增加图书\n')
        print('[0]退出系统\n')
        while True:
            managerchoice = input('请选择您要进行的操作：')
            if managerchoice == '1':
                # 管理员查看图书部分
                choice.StudentSee()
            elif managerchoice == '2':
                # 管理员查询图书部分
                choice.ManagerFind()
            elif managerchoice == '3':
                # 管理员增加图书部分
                choice.ManagerAdd()
            elif managerchoice == '0':
                # 退出菜单部分
                print('')
                print('\033[5;31;2m***欢迎再次使用图书管理系统***\033[0m')
                break
            else:
                print('您的输入不正确，请输入[1]查看所有图书[2]查询图书[3]增加图书[0]退出系统\n')


class choice(object):

    # 增加图书
    @staticmethod
    def ManagerAdd():
        name = input('请输入书籍的名称：')
        author = input('请输入书的作者：')
        count = input('请输入书的数量：')
        place = input('请输入书所在的楼层：')

        BookList.append(Book(name, author, count, place))
        print('%s 添加成功！' % name)
        print('')
        print('图书馆所有的书籍有：')
        # 调用StudentSee方法，显示图书馆中所有的书
        choice.StudentSee()

    # 查询图书
    @staticmethod
    def ManagerFind():
        name = input('请输入要查询的书名：')
        for book in BookList:
            if name == book.name :
                print('《%s》 作者：%s  数量：%s  楼层：%s！' % (name,book.author,book.count,book.place))
                return book
        else:
            print('《%s》没有找到！' % name)
            return None
    # 遍历图书馆中的所有书
    @staticmethod
    def StudentSee():
        print('图书馆中所有的书有：')
        for book in BookList:
            print('《%s》 作者：%s \t数量：%s \t楼层：%s '% (book,book.author,book.count,book.place))

    # 学生借书部分
    @staticmethod
    def StudentBorrow():
        name = input('请输入您想借阅的书名：')
        BookResult = choice.ManagerFind()
        if BookResult:
            if BookResult.count == 0 or BookResult.count < 0:
                print('***该书已经被借出，请稍后再来！***')
            else:
                BookResult.count > 0
                print('您已成功借到《%s》...' % (name))
                BookResult.count  -= 1

        else:
            print('抱歉，图书馆暂时没有《%s》这本书...' % name)

    # 学生还书部分
    @staticmethod
    def StudentGive():
        name = input('请输入您要归还的书名：')
        BookResult1 = choice.ManagerFind()
        BookResult1.count += 1
        print('您的书已经归还成功,欢迎下次使用...')


# 类外主程序部分
# 定义一个存放书籍信息的列表
BookList = []

# 实例化初始书籍信息，存放在列表中
book1 = BookList.append(Book('C语言设计','齐朝怡',5,'1Floor'))
book2 = BookList.append(Book('人机交互','周杰伦',2, '2Floor'))
book3 = BookList.append(Book('数据库','方文山',1,'3Floor'))

# 调用identity类中的静态方法
identity.Choice()
"""

# 图书管理系统
# 1.查询图书
# 2.增加图书
# 3.借阅图书
# 4.归还图书
# 5.退出系统
# 书：书名 作者 状态
# d = {1: ['','',''],2:['','',''],3:['','',''],4:['','','']}
'''
class Book(object):

    def __init__(self, con, book_name, book_writer, book_in):
        self.con = con
        self.book_name = book_name
        self.book_writer = book_writer
        self.book_in = book_in

    #  自动将对象属性对应的值输出出来  输出的时候是个字符串
    def __str__(self):
        return f"{self.con}{self.book_name}{self.book_writer}{self.book_in}"

class People(object):
    student = {'a': '123', 'b': '456', 'c': '789'}

    @staticmethod
    def student_1():
        while True:
            name = input('请输入你的姓名：')
            password = input('请输入你的密码：')
            if name in People.student.keys() and password == People.student[name]:
                print("欢迎进入学生图书管理系统")
                print("请选择操作：1.查看所有图书  2.查询图书  3.借阅图书 4.归还图书 5.退出系统")
                while True:
                    a = int(input("请输入你要进行的操作:"))
                    if a == 1:
                        Jicao.look()
                    elif a == 2:
                        Jicao.souyin()
                    elif a == 3:
                        Jicao.jeishu()
                    elif a == 4:
                        Jicao.huanshu()
                    elif a == 5:
                        print(f"欢迎下次使用图书管理系统")
                        return 0
                    else:
                        print("请重新选择操作")
            else:
                print('请重新输入！！！')

    @staticmethod
    def admin():
        admin = {'admin':'123456'}
        while True:
            name = input('请输入你的姓名：')
            password = input('请输入你的密码：')
            if name == 'admin' and password == '123456':
                print("欢迎进入管理员图书管理系统")
                print("请选择操作： 1.添加图书  2.删除图书 3.退出系统")
                while True:
                    a = int(input("请输入你要进行的操作:"))
                    if a == 1:
                        Jicao.add()
                    elif a == 2:
                        Jicao.shanchu()
                    elif a == 3:
                        print(f"欢迎下次使用图书管理系统")
                        return 0
                    else:
                        print("请重新选择操作！！！")
            else:
                print('请重新输入！！！')

    @staticmethod
    def chioce():
        print("*************登录界面****************")
        print("****1表示你是管理员**2表示你是学生****")
        a = int(input("请选择你是学生或者是管理员:"))
        if a == 1:
            People.admin()
        else:
            People.student_1()


class Jicao(object):

    @staticmethod
    def add():
        con = input("请输入编号：")
        book_name = input("请输入书名：")
        book_writer = input("请输入书的作者：")
        book_in = input("请输入是否被借出：")
        book_list.append(Book(con, book_name, book_writer, book_in))
        print("添加成功")
        print("")
        Jicao.look()

    @staticmethod
    def shanchu():
        Jicao.look()
        print("请从上面的书籍中进行删除操作")
        a = input("请选择书的编号：")
        for book in book_list:
            if a == book.book_name:
                book_list.remove(book)
                break
        else:
            print("没有你要删除的图书")

    @staticmethod
    def souyin():
        print("请对书籍中进行查询操作")
        a = input("请选择书的名字：")
        for book in book_list:
            if a == book.book_name:
                print(f'书的编号是：{book.con}，书的名字为：{book.book_name}，书的作者为：{book.book_writer}，'
                      f'书的状态为：{book.book_in}')
                break
        else:
            print("没有你要查询的图书")

    @staticmethod
    def jeishu():
        print("请选择书籍进行借阅操作")
        a = input("请选择书的名字：")
        for book in book_list:
            if a == book.book_name:
                book_list.remove(book.book_in)
                book_list.append('out')
                break
        else:
            print("你要查询的图书已被借出")

    @staticmethod
    def huanshu():
        print("请进行归还书籍操作")
        a = input("请选择书的名字：")
        for book in book_list:
            if a == book.book_name:
                book_list.remove(book.book_in)
                book_list.append('in')
                break
        else:
            print("没有你要归还的图书")

    @staticmethod
    def look():
        print("所有的图书为：")
        for book in book_list:
            print(f'书的编号是：{book.con}，书的名字为：{book.book_name}，书的作者为：{book.book_writer}，'
                  f'书的状态为：{book.book_in}')
        print("书的状态为in表示，图书馆有此书，out表示图书馆此书以被借阅")


book_list = []
book_list.append(Book(1, '水浒传', '施耐庵', 'in'))
book_list.append(Book(2, '西游记', '吴承恩', 'in'))
book_list.append(Book(3, '红楼梦', '曹雪芹', 'out'))
book_list.append(Book(4, '三国演义', '罗贯中', 'in'))

People.chioce()
'''

# 用面向对象来写
# 定义一个类：
# 1.可以打开不同的excel表格
# 2.按照行读取任意行数据  2到3
# 3.读取指定格的数据
# 4.按照列读取任意行数据
# 5.指定读取某个表格的数据
'''
import xlrd


class Excel(object):

    def __init__(self,name,i):
        self.name = name
        self.i = i
        self.d = xlrd.open_workbook(filename=self.name)
        self.table = self.d.sheets()[self.i]

    def readhang(self):
        a = self.table.nrows
        while True:
            c = int(input("请输入你要查询的行号："))
            if 0 <= c < a:
                print(self.table.row_values(c))
                return None
            else:
                print(f"行请输入0到之间{a}的数")

    def renyi(self):
        a = self.table.nrows
        b = self.table.ncols
        while True:
            c = int(input("请输入你要查询的行："))
            d = int(input("请输入你要查询的列："))
            if 0 <= c < a and 0 <= d < b:
                print(self.table.cell(c,d).value)
                return None
            else:
                print(f"行请输入0到之间{a}的数")
                print(f"列请输入0到之间{b}的数")

    def readlie(self):
        b = self.table.ncols
        while True:
            d = int(input("请输入你要查询的列："))
            if 0 <= d < b:
                print(self.table.col_values(d))
                return None
            else:
                print(f"列请输入0到之间{b}的数")

    def readbiao(self):
        a = self.table.nrows
        for i in range(a):
            print(self.table.row_values(i))

    def choice(self):
        print("欢迎操作excel表格")
        print("请选择下面操作")
        print("1. 按照行读取任意行数据 2. 读取指定单元格的数据")
        print("3. 按照列读取任意列数据 4. 指定读取某个表格的数据")
        print("5. 退出系统")
        while True:
            a = int (input("请选择你的操作："))
            if a == 1:
                self.readhang()
            elif a == 2:
                self.renyi()
            elif a == 3:
                self.readlie()
            elif a == 4:
                self.readbiao()
            elif a == 5:
                print("欢迎下次使用")
                return None
            else:
                print("请选择正确操作")


excel1 = Excel('lianxibiaoge.xlsx',0)
excel1.choice()
'''

# 读取a.txt的文件 并把它写入excel表格中  ‪C:\Users\wangxiao\Desktop\a.txt
"""
import xlwt
d = open(file=r'C:/Users/wangxiao/Desktop/a.txt',encoding='utf-8',mode='r')
# print(d.read())
# print(type(d.read()))
a = d.read().split(")")
# print(len(a))
# print(type(a))
# print(a)
# print(a[0])
# print(a[30])
a.pop(30)
d = []
for i in a:
    b = i.replace("'",'').replace("'",'').split("(")
    # print(type(b[1]))
    c = b[1].split(",")
    d.append(c)
print(d)

class Excel(object):

    name = "d2.xls"

    def xwrite(self):
        f = xlwt.Workbook()
        table = f.add_sheet('d1.xls')
        for i in range(len(d)):
            for j in range(len(d[i])):
                table.write(i, j, d[i][j])
        f.save(self.name)


b = Excel()
b.xwrite()
"""

# 统计顶级目录下有多少个目录，文件个数
"""
import os


class Count_1(object):

    def __init__(self,f):
        self.f = f
        self.d = os.listdir(self.f)

    def count_dir(self):
        s = 0
        for i in self.d:
            if os.path.isdir(i):
                s +=1
        print(f"该目录下有{s}个目录")

    def count_file(self):
        s = 0
        for i in self.d:
            if os.path.isfile(i):
                s += 1
        print(f"该目录下有{s}个文件")

    def choice(self):
        print("***********请选择你需要统计的类型*************")
        print("***1.统计目录个数  2.统计文件个数  3.退出系统***")
        while True:
            a = int(input("请选择你的操作："))
            if a == 1:
                self.count_dir()
            elif a == 2:
                self.count_file()
            elif a == 3:
                print("退出该系统")
                return None
            else:
                print("请重新选择操作")

d = Count_1(r'C')
d.choice()
"""

# 写入数据到mysql
import pymysql,time,xlwt

# print(d)
# for i in d:
#     print(i[0])
#     print(i[1])
#     print(i[2])
#     print(i[3])
#     time.sleep(5)

class MysqlSty(object):

    def __init__(self):
        self.d = pymysql.connect(host='192.168.10.3',
                                 port=3306,
                                 user='root',
                                 password='123456',
                                 database='info',
                                 charset='utf8')
        self.e = self.d.cursor()

        d = open(file=r'C:/Users/wangxiao/Desktop/a.txt', encoding='utf-8', mode='r')
        a = d.read().split(")")
        a.pop(30)
        self.g = []
        for i in a:
            b = i.replace("'",'').replace("'",'').split("(")
            c = b[1].split(",")
            self.g.append(c)

    def write_mysql(self):
        # sql_1 = "create database info character set utf8"
        # self.e.execute(sql_1)
        # sql_2 = "create table a (con char(8), company varchar(255), work varchar(255), web varchar(255), " \
        #         "pro varchar(255),shangshi varchar(255), num varchar(255), address varchar(255), year varchar(255), xueli varchar(255))"
        # # self.e.execute(sql_2)
        # for i in self.g:
        #     sql_3 = "insert into a  values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        #     self.e.execute(sql_3,(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
        #     self.d.commit()

        sql_4 = "select *from a where con < 5"
        self.e.execute(sql_4)
        a = self.e.fetchall()
        d = xlwt.Workbook()
        table = d.add_sheet('d1')
        for i in range(len(a)):
            for j in range(len(a[0])):
                table.write(i,j,a[i][j])
        d.save("d4.xls")


a = MysqlSty()
a.write_mysql()




























