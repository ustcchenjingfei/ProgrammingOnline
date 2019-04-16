"""
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。即这个数转换成2进制后，输出1的个数。
"""

# 法一：
# n = int(input())
# aList = []
# while n > 0:
#     m = n % 2
#     aList.append(str(m))
#     n = n // 2
#
# print(''.join(aList).count('1'))


# 法二：
# from collections import Counter
#
# n = int(input())
# aList = []
# while n > 0:
#     m = n % 2
#     aList.append(m)
#     n = n // 2
#
# result = Counter(aList)  # 转为字典
# print(dict(result)[1])

#法三
n = int(input())
m=bin(n)
print(m.count('1'))
