#!usr/bin/env python
# -*-coding:utf-8-*-

"""
@Author: jingfei Chen
@Time: 2019-05-16 21:12 
@Email: 953209336@qq.com
"""
# 通过Font对象表示字体
import tkinter as tk
import tkinter.font  # 引入字体模块

win = tk.Tk()  # 创建一个窗口对象
print(tkinter.font.families())  # 打印所有可用字体

win.title('我的第一个Windows窗口')  # 设置窗口标题

ft = tk.font.Font(family='Fixdsys', size=20, weight='bold', slant='italic', underline=1, overstrike=1)
# 字体名，大小，加粗，倾斜，下划线，删除线

lab = tk.Label(win, text='USTC', font=ft).grid()

win.mainloop()  # 进入消息循环，也就是显示窗口
