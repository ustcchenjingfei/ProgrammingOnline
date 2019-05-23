#!usr/bin/env python
# -*-coding:utf-8-*-

"""
@Author: jingfei Chen
@Time: 2019-05-20 18:59 
@Email: 953209336@qq.com
"""

import tkinter as tk


def leftClick(event):
    print("x轴坐标", event.x)
    print("y轴坐标", event.y)
    print("相对屏幕左上角x轴坐标", event.x_root)
    print("相对屏幕左上角y轴坐标", event.x_root)
    print(event.time)
    print(event.type)


win = tk.Tk()  # 创建一个窗口对象
win.title('我的第一个Windows窗口')  # 设置窗口标题

lab = tk.Label(win, text='Hello')
lab.pack()
lab.bind("<Button-1>", leftClick)

win.mainloop()  # 进入消息循环，也就是显示窗口
