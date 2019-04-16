"""
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
"""

# 法一

# n = int(input())
# aList = []
# N = 0
# while n != 0:
#     m = n % 10
#     if m not in aList:
#         aList.append(m)
#         N = N * 10 + m
#     n = n // 10 #  这样写也行n = int(n / 10) 。 注: '/'是除以 。 而'/'是取整除,返回商的整数部分（向下取整）。
#
# print(N)


# 方法二(思路不错)
num = input()
num = num[::-1]  # 反转
# print(num)
num1 = list(set(num))  # 去重
# print(num1)
num1.sort(key=num.index)  # 注意，是num的index
# print(num1)
print(''.join(num1))
