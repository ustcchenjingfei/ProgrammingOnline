#!usr/bin/env python
# -*-coding:utf-8-*-

"""
@Author: jingfei Chen
@Time: 2019-05-15 19:53 
@Email: 953209336@qq.com
"""
import tkinter as tk

win = tk.Tk()  # 创建一个窗口对象
win.title('计算器示例')  # 设置窗口标题
win.geometry('200x200+280+280')  # 200x200代表了初始化窗口大小(宽高)，280和280代表初始化窗口所在位置。x是小写的字母，不是乘号
L1 = tk.Button(win, text='1', width=5, bg='yellow')
L2 = tk.Button(win, text='2', width=5)
L3 = tk.Button(win, text='3', width=5)
L4 = tk.Button(win, text='4', width=5)
L5 = tk.Button(win, text='5', width=5, bg='green')
L6 = tk.Button(win, text='6', width=5)
L7 = tk.Button(win, text='7', width=5)
L8 = tk.Button(win, text='8', width=5)
L9 = tk.Button(win, text='9', width=5, bg='yellow')
L0 = tk.Button(win, text='0')
Lp = tk.Button(win, text='.')

L1.grid(row=0, column=0)  # 按钮放置在0行0列
L2.grid(row=0, column=1)
L3.grid(row=0, column=2)
L4.grid(row=1, column=0)
L5.grid(row=1, column=1)
L6.grid(row=1, column=2)
L7.grid(row=2, column=0)
L8.grid(row=2, column=1)
L9.grid(row=2, column=2)
L0.grid(row=3, column=0, columnspan=2, sticky=tk.E + tk.W)  # 夸两列，左右紧贴
Lp.grid(row=3, column=2, sticky=tk.E + tk.W)  # 左右紧贴

win.mainloop()  # 进入消息循环，也就是显示窗口
