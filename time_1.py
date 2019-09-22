#!/usr/bin/python
#-*-coding:utf-8-*-
# 时间模块  操作的是时间和日期  time datetime
# 时间模块
# sleep(浮点数、整数)
import time
# print('adad')
time.sleep(5)
print("ad")

# clock() 计算的是执行代码时cup花费的时间
# print(time.clock())

# ctime()  asctime() 获取当前时间
# print(time.ctime())
# print(time.asctime())

# 获取本地时区  localtime（）
# print(time.localtime())

# 格式化输出时间  strftime("关于时间的字符串")
# %a    本地化的缩写星期中每日的名称。
# %A    本地化的星期中每日的完整名称。
# %b    本地化的月缩写名称。
# %B    本地化的月完整名称。
# %c    本地化的适当日期和时间表示。
# %d    十进制数 [01,31] 表示的月中日。
# %H    十进制数 [00,23] 表示的小时（24小时制）。
# %I    十进制数 [01,12] 表示的小时（12小时制）。
# %j    十进制数 [001,366] 表示的年中日。
# %m    十进制数 [01,12] 表示的月。
# %M    十进制数 [00,59] 表示的分钟。
# %p    本地化的 AM 或 PM 。
# %S    十进制数 [00,61] 表示的秒。
# %U    十进制数 [00,53] 表示的一年中的周数（星期日作为一周的第一天）作为。在第一个星期日之前的新年中的所有日子都被认为是在第0周
# %w    十进制数 [0(星期日),6] 表示的周中日。
# %W    十进制数 [00,53] 表示的一年中的周数（星期一作为一周的第一天）作为。在第一个星期一之前的新年中的所有日子被认为是在第0周。
# %x    本地化的适当日期表示。
# %X    本地化的适当时间表示。
# %y    十进制数 [00,99] 表示的没有世纪的年份。
# %Y    十进制数表示的带世纪的年份。
# %z    时区偏移以格式 +HHMM 或 -HHMM 形式的 UTC/GMT 的正或负时差指示，其中H表示十进制小时数字，M表示小数分钟数字 [-23:59, +23:59] 。
# %Z    时区名称（如果不存在时区，则不包含字符）。
# %%    字面的 '%' 字符
print(time.strftime("%A %B %H: %M: %S"))

# strptime("关于时间的字符串")  计算时间
# %y 年份 %b 表示月份月份 %d 一个月的第几天
print(time.strptime("30 Nov 00","%d  %b %y"))

# 计算计算机元年到现在过去了多少秒
# print(time.time())


from _datetime import datetime,date,timedelta  # 精确导入
# import datetime 整体导入
# 求精准日期
print(datetime.now())

# 获取指定的时间，日期  datetime(整数) 必须是整数  把传入的数字变成时间
print(datetime(2019,7,30,12))

# 字符串时间转化datetime的日期  strptime（）
print(datetime.strptime("1923 1 2 12:1:2" ,"%Y %m %d %H:%M:%S"))

# 将时间转化为字符串  strftime（）
print(datetime.now().strftime("%H:%M:%S"))

# 日期的加减
# 求当前时间
# a = datetime.now()
# print(a)
# 加上3个小时  hours=3  seconds=23  minutes=23
# b = a + timedelta(minutes=23)
# print(b)

# 获取当前的日期today（）
# print(date.today())

# 对日期进行加减
# 首先获取当前日期，然后加减日期
# f = date.today() - timedelta(days=1)
# print(f)























