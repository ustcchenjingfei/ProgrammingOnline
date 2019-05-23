#!usr/bin/env python
# -*-coding:utf-8-*-

"""
@Author: jingfei Chen
@Time: 2019-05-15 21:43 
@Email: 953209336@qq.com
"""

import tkinter as tk

win = tk.Tk()  # 创建一个窗口对象
win.title('我的第一个Windows窗口')  # 设置窗口标题


def callbutton1():
    for i in listbox1.curselection():
        print(i)
        listbox2.insert(0, listbox1.get(i))


def callbutton2():
    for i in listbox2.curselection():
        listbox2.delete(i)


li = ['C', 'python', 'php', 'html', 'SQL', 'java']
listbox1 = tk.Listbox(win)
listbox2 = tk.Listbox(win)
b1 = tk.Button(win, text='添加>>', command=callbutton1, width=20)
b2 = tk.Button(win, text='删除<<', command=callbutton2, width=20)

for item in li:
    listbox1.insert(0, item)
    # listbox1.insert(tk.END, item)

listbox1.grid(row=0, column=0, rowspan=2)  # 表格单元横跨两行的表格

b1.grid(row=0, column=1, rowspan=2)
b2.grid(row=1, column=1, rowspan=2)

listbox2.grid(row=0, column=2, rowspan=2)

win.mainloop()  # 进入消息循环，也就是显示窗口
