"""
题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。
a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
"""
# 分析：c说他不和x,z比,那么c只能和y比赛了。a说他不和x比，那只能和z比啦

list1 = ['a', 'b', 'c']
list2 = ['x', 'y', 'z']

for i in range(3):
    for j in range(3):
        if (list1[i] == 'a' and list2[j] == 'z') or (list1[i] == 'b' and list2[j] == 'x') or (list1[i] == 'c' and list2[j] == 'y'):
            print('{0}---{1}'.format(list1[i], list2[j]))
            list1[i] = ' '
            list2[j] = ' '
