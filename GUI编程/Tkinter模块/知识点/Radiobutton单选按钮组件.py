#!usr/bin/env python
# -*-coding:utf-8-*-

"""
@Author: jingfei Chen
@Time: 2019-05-16 19:03 
@Email: 953209336@qq.com
"""


import tkinter as tk

win = tk.Tk()  # 创建一个窗口对象
win.title('我的第一个Windows窗口')  # 设置窗口标题

r = tk.StringVar()
r.set('2')

radiobutton = tk.Radiobutton(win, variable=r, value='1', text='中国')
radiobutton.pack()

radiobutton = tk.Radiobutton(win, variable=r, value='2', text='美国')
radiobutton.pack()

radiobutton = tk.Radiobutton(win, variable=r, value='3', text='日本')
radiobutton.pack()

radiobutton = tk.Radiobutton(win, variable=r, value='4', text='加拿大')
radiobutton.pack()

radiobutton = tk.Radiobutton(win, variable=r, value='5', text='韩国')
radiobutton.pack()

print(r.get())

win.mainloop()  # 进入消息循环，也就是显示窗口
