#!usr/bin/env python
# -*-coding:utf-8-*-

"""
@Author: jingfei Chen
@Time: 2019-05-16 19:04 
@Email: 953209336@qq.com
"""

import tkinter as tk

win = tk.Tk()  # 创建一个窗口对象
win.title('我的第一个Windows窗口')  # 设置窗口标题

checkoutbutton=tk.Radiobutton(win,text='China')
checkoutbutton.pack()

win.mainloop()  # 进入消息循环，也就是显示窗口