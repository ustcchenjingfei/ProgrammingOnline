#!usr/bin/env python
# -*-coding:utf-8-*-

"""
@Author: jingfei Chen
@Time: 2019-05-20 18:59 
@Email: 953209336@qq.com
"""

import tkinter as tk



def printRect(event):
    print('rectangle左键事件')


def printRect2(event):
    print('rectangle右键事件')


def printLine(event):
    print('Line事件')

win = tk.Tk()  # 创建一个窗口对象
win.title('我的第一个Windows窗口')  # 设置窗口标题



cv = tk.Canvas(win, bg='blue')  # 创建一个画布控件
rt1 = cv.create_rectangle(10, 10, 110, 110, width=8, tags='r1')

cv.tag_bind('r1','<Button-1>',printRect)
cv.tag_bind('r1','<Button-3>',printRect2)

cv.create_line(180,70,280,70, width=10, tags='r2')
cv.tag_bind('r2','<Button-1>',printLine)
cv.pack()


win.mainloop()  # 进入消息循环，也就是显示窗口
