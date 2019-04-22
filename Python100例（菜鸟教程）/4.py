"""
题目：输入某年某月某日，判断这一天是这一年的第几天？

程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
"""

year = int(input('year:'))
month = int(input('month:'))
day = int(input('day:'))

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
# 平年2月28天
# 闰年2月29天
# 四年一闰

if 0 < month <= 12:
    sum = months[month - 1]

sum += day
if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))) and (month > 2):
    sum += 1

print('{0}年{1}月{2}日是第{3}天'.format(year, month, day, sum))
