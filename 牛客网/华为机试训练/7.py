"""
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
"""

# 方法一

float_num = float(input())
int_num = int(float_num)

if float_num - int_num >= 0.5:
    print(int_num + 1)
else:
    print(int_num)

"""
# 方法二
import math

def approximate_number(float_num):
    float_num_list = list(float_num)
    index = float_num_list.index(".")
    n = int(float_num_list[index + 1])

    if n >= 5:
        print(math.ceil(float(float_num)))
    else:
        print(math.floor(float(float_num)))


float_num = input()
approximate_number(float_num)
"""
