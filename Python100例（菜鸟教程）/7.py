"""
题目：将一个列表的数据复制到另一个列表中。
"""

# 方法一
a = [1, 2, 3]
b = a  # 或者b=a[:]
print(b)

# 方法二
list1 = [1, 2, 3]
list2 = list1.copy()
print(list2)

# 方法三
list1 = [1, 2, 3]
list2 = []
list2.extend(list1)
print(list2)
