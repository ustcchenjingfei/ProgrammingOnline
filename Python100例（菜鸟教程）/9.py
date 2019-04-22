"""
题目：暂停一秒输出。

程序分析：使用 time 模块的 sleep() 函数。
"""
import time

aList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in aList:
    print(i)
    time.sleep(1)  # 暂停 1 秒
