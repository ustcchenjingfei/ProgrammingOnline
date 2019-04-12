"""
数据表记录包含表索引和数值，请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，
输出按照key值升序进行输出。
"""

n = int(input())
adict = {}

while n > 0:
    s = input()
    a, b = s.split()
    a = int(a)
    b = int(b)
    if a in adict:
        adict[a] = adict[a] + b
    else:
        adict[a] = b
    n = n - 1

for k, v in adict.items():
    print(k, v)
