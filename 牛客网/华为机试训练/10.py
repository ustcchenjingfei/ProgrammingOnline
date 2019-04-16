"""
编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)。不在范围内的不作统计。
"""
s = input()

aList = list(set(s))

for i in aList:
    if ord(i) >= 0 and ord(i) <= 127:
        pass
    else:
        aList.remove(i)

print(len(aList))
