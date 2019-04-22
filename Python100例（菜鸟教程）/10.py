"""
题目：暂停一秒输出，并格式化当前时间
"""

import time
import datetime

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

time.sleep(1)  # 暂停一秒

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))



# 方法二
d = datetime.datetime.today()
print(d.strftime('%Y-%m-%d %H:%M:%S'))

time.sleep(1)  # 暂停一秒

d1 = datetime.datetime.today()
print(d1.strftime('%Y-%m-%d %H:%M:%S'))
