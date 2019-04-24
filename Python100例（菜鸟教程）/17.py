"""
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

程序分析：利用  for 语句,条件为输入的字符不为 '\n'。
"""

def cnt(string):
    letters = 0
    space = 0
    digit = 0
    others = 0

    for i in string:
        if i.isalpha():
            letters += 1
        elif i.isspace():
            space += 1
        elif i.isdigit():
            digit += 1
        else:
            others += 1

    return letters, space, digit, others


s = '123runoobc  kdf235*(dfl'
letters, space, digit, others = cnt(s)
print('letters={0}, space={1}, digit={2}, others={3}'.format(letters, space, digit, others))
