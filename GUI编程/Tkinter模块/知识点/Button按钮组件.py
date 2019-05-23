#!usr/bin/env python
# -*-coding:utf-8-*-

"""
@Author: jingfei Chen
@Time: 2019-05-15 21:12 
@Email: 953209336@qq.com
"""

import tkinter as tk

win = tk.Tk()  # 创建一个窗口对象
win.title('我的第一个Windows窗口')  # 设置窗口标题
win.geometry('800x600')  # 设置窗口大小(宽高)，x是小写的字母，不是乘号

button1 = tk.Button(win, text='BUTTON1')
"""
也可以通过已下方式之一设置组件
1、button=Button(win,text='BUTTON1')
2、button.config(text='BUTTON1')
3、button[text]='BUTTON1'
"""

button1.pack(side=tk.LEFT)  # 将button1添加到窗口中，左停靠
button2 = tk.Button(win, text='BUTTON2')
button2.pack(side=tk.RIGHT)  # 将button2添加到窗口中，右停靠

win.mainloop()  # 进入消息循环，也就是显示窗口
