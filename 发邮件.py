#!/usr/bin/python
#-*-coding:utf-8-*-
#smtplib  email 作用：用于接收发送邮件

import   smtplib
from   email.mime.text import MIMEText
from   email.header import  Header
from  email.mime.multipart import   MIMEMultipart
from  email.mime.image import  MIMEImage

#设置服务器所需的信息
#邮件服务器的地址
mail_host ='smtp.163.com'     #服务器端信息
mail_port ='465'
mail_user = '18238797727@163.com'   #用户信息
mail_pass ='mw19981130'    #用户信息
sender ='18238797727@163.com'  #发送方地址
receivers=['w18003827633@163.com']  #接收方地址

#邮件正文
subject='哈哈哈哈'  #邮件主题
content='蹦迪嗨起来' #邮件正文
message=MIMEText(content,'plain','utf-8')  #三个参数： 文本内容，文本格式， 编码

Header()  #类，作用：对方送的邮件添加头部信息
# #发送邮件的过程
message['From']=Header()  #添加发送者头部
message['To']=Header(str(';'.join(receivers))) #添加接受者头部
message['Subject']=Header(subject)  #添加邮件主题
#
# #连接邮件服务器并发送
s=smtplib.SMTP_SSL(host=mail_host,port=mail_port)#登陆邮箱
s.login(mail_user,mail_pass)#输入账号密码
s.sendmail(sender,receivers,message.as_string())#发送邮件
print('ok')
#
# #退出
s.close()
# #s.quit()

#带有附件的邮件发送
message=MIMEMultipart()#将正文及附件添加到邮件里

message['From']=Header()  #添加发送者头部
message['To']=Header(str(';'.join(receivers))) #添加接受者头部
message['Subject']=Header(subject)  #添加邮件主题
# 准备要发送的正文，HTML网页的形式
with open(file='aaaa.html',mode='r',encoding='utf-8') as  f:
    content=f.read()
# 设置HTML格式
p1=MIMEText(content,'html','utf-8')
#准备一个要发送的附件
with open(file='aaa.txt',mode='r',encoding='utf-8') as f:
    d=f.read()
#
p2=MIMEText(d,'plain','utf-8')
p2['Content-Type']= 'application/octet-stream'#将文本转成二进制流
p2['Content-Disposition'] = 'attachment;filename="abc.txt"'#对附加添加一个名字
#添加一个照片作为附件
with open(file='a.jpg',mode='rb') as f:
    p3=MIMEImage(f.read())
p3['Content-Type'] = 'application/octet-stream'  # 将文本转成二进制流
p3['Content-Disposition'] = 'attachment;filename="a.jpg"'  # 对附加添加一个名字

message.attach(p1)
message.attach(p2)
message.attach(p3)

s=smtplib.SMTP_SSL(host=mail_host,port=mail_port)#登陆邮箱
s.login(mail_user,mail_pass)#输入账号密码
s.sendmail(sender,receivers,message.as_string())#发送邮件
print('ok')

# #退出
s.close()

# import   smtplib
# from   email.mime.text import MIMEText
# from   email.header import  Header
# from  email.mime.multipart import   MIMEMultipart
# from  email.mime.image import  MIMEImage
#
#
# class  Mail(object):
#
#     mail_host = 'smtp.163.com'  # 服务器端信息
#     mail_port = 465
#     mail_user = '18238797727@163.com'   #用户信息
#     mail_pass ='mw19981130'    #用户信息
#     sender ='18238797727@163.com'  #发送方地址
#     receivers=['w18003827633@163.com']  #接收方地址

    # def  __init__(self,mail_host,mail_port,mail_user,mail_pass,sender,receivers):
        # self.mail_host=mail_host
        # self.mail_port=mail_port
        # self.mail_user=mail_user
        # self.mail_pass=mail_pass
        # self.sender=sender
        # self.receivers=receivers
    # def  address(self):
    #     if mail_host =='smtp.163.com':
    #         print(mail_pass)
    #     else:
    #         print('重新输入')
    # def  message(self):
#         a=input('输入主题')
#         subject= a
#         b=input('输入正文')
#         content= b
#         message = MIMEText(content, 'plain', 'utf-8')
#         message['From'] = Header(self.sender)  # 添加发送者头部
#         message['To']=Header(str(';'.join(self.receivers))) #添加接受者头部
#         message['Subject']=Header(subject)
#         s = smtplib.SMTP_SSL(host=self.mail_host, port=self.mail_port)  # 登陆邮箱
#         s.login(self.mail_user,self.mail_pass)#输入账号密码
#         s.sendmail(self.sender,self.receivers,message.as_string())#发送邮件
#         print('ok')
#         s.close()
# a=Mail()