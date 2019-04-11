"""
功能:输入一个正整数，按照从小到大的顺序输出它的所有质数的因子（如180的质数因子为2 2 3 3 5 ）
最后一个数后面也要有空格
"""


def prime_number(n):
    # m = int(math.pow(n, 0.5))  判断素数用的

    for i in range(2, n + 1):
        while n % i == 0:
            n = n / i
            print(str(i) + " ", end='')
        if i == n:
            print(str(n) + " ", end='')
    return


n = int(input())
prime_number(n)
