"""
题目：判断101-200之间有多少个素数，并输出所有素数。

程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 　　
"""

import math

cnt = 0
for i in range(101, 201):
    n = int(math.sqrt(i))
    for j in range(2, n + 1):
        if i % j == 0:
            break
        elif i % j != 0 and j == n:
            cnt += 1
            print(i, end=' ')

print('\n\n素数的个数为:{0}'.format(cnt))
