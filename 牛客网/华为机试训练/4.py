"""
连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
"""


def string_out(string):

    if len(string) == 0:
        return
    elif len(string) <= 8:
        print(string + ("0" * (8 - len(string))))

    else:
        while len(string) > 8:
            print(string[:8])
            string = string[8:]
        print(string + "0" * (8 - len(string)))

    return


s1 = input()
s2 = input()
string_out(s1)
string_out(s2)
