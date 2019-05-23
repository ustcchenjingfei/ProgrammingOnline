#!usr/bin/env python
# -*-coding:utf-8-*-

"""
@Author: jingfei Chen
@Time: 2019-05-15 20:52 
@Email: 953209336@qq.com
"""

import tkinter as tk

win = tk.Tk()  # 创建一个窗口对象
win.title('我的第一个Windows窗口')  # 设置窗口标题
win.geometry('800x600')  # 设置窗口大小(宽高)，x是小写的字母，不是乘号

lab1 = tk.Label(win, text='你好', anchor='nw')  # anchor指定text在lab1的位置,注意是在标签中
lab1.pack()  # 显示 lab1组件

lab2 = tk.Label(win, bitmap='question')  # 创建疑问图标内置的位图标签
lab2.pack()  # 显示内置的位图

bm = tk.PhotoImage(file=r'C:\Users\Administrator\Desktop\demo\着火.gif')
lab3 = tk.Label(win, image=bm)
lab3.bm = bm
lab3.pack()  # 显示自选的图片

win.mainloop()  # 进入消息循环，也就是显示窗口
