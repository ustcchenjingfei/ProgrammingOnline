"""
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
"""


def get_factor_sum(n):
    factor_list = []
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            factor_list.append(i)

    return sum(factor_list)


for i in range(1, 1000):
    if i == get_factor_sum(i):
        print(i, end="\t")
