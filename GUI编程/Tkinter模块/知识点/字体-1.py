#!usr/bin/env python
# -*-coding:utf-8-*-

"""
@Author: jingfei Chen
@Time: 2019-05-16 21:12 
@Email: 953209336@qq.com
"""
# 通过元组创建字体
import tkinter as tk

win = tk.Tk()  # 创建一个窗口对象
win.title('我的第一个Windows窗口')  # 设置窗口标题

fontList = ['Arial',
            ('Courier New', 19, 'italic'),
            ('Comic Sans MS',),
            'Fixdays',
            ('MS Sans Serif',),
            ('MS Serif',),
            'Symbol',
            'System',
            ('Times New Roman',),
            'Verdaan']

for ft in fontList:
    lab = tk.Label(win, text='USTC', font=ft).grid()

win.mainloop()  # 进入消息循环，也就是显示窗口
