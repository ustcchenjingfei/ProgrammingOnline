"""
题目：斐波那契数列。

程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：
0、1、1、2、3、5、8、13、21、34、……。
"""


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


n = int(input("Please input a Num:"))
print(fib(n))

aList = []
for i in range(1, 11):
    aList.append(fib(i))
print('\n', aList)
