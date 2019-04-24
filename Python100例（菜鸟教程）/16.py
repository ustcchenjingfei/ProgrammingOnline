"""
题目：输出指定格式的日期。
"""
import datetime
import time

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 2019-04-24 09:22:24

print(time.strftime("%d/%m/%Y", time.localtime()))  # 24/04/2019

# 创建日期对象
a = datetime.date(2019, 4, 24)
print(a.strftime('%Y/%m/%d'))

# 日期算术运算
b = a + datetime.timedelta(days=1)
print(b.strftime('%Y/%m/%d'))

c = a + datetime.timedelta(weeks=1)
print(c.strftime('%Y/%m/%d'))

# 日期替换
d = a.replace(year=a.year + 1)  # a的年份加1
print(d.strftime('%Y/%m/%d'))
