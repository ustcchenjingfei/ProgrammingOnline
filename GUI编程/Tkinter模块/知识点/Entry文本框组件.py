#!usr/bin/env python
# -*-coding:utf-8-*-

"""
@Author: jingfei Chen
@Time: 2019-05-15 21:21 
@Email: 953209336@qq.com
"""

import tkinter as tk

win = tk.Tk()  # 创建一个窗口对象
win.title('登录')  # 设置窗口标题
# 设置窗口宽高
win['width'] = 800
win['height'] = 600

s = tk.StringVar()
s.set("hello,it's test")

entry = tk.Entry(win, textvariable=s)  # Entry组件显示"hello,it's test"
print(s.get())
entry.pack()

win.mainloop()  # 进入消息循环，也就是显示窗口
