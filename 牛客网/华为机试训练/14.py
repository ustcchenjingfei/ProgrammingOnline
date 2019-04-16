n = int(input())

aList = []
for i in range(n):
    s = input()
    aList.append(s)
aList.sort()

for item in aList:
    print(item, end='\n')
