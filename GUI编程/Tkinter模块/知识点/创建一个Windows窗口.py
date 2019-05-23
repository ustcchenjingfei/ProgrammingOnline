#!usr/bin/env python
# -*-coding:utf-8-*-

"""
@Author: jingfei Chen
@Time: 2019-05-15 19:27 
@Email: 953209336@qq.com
"""

import tkinter as tk

win = tk.Tk()  # 创建一个窗口对象
win.title('我的第一个Windows窗口')  # 设置窗口标题
win.geometry('800x600')  # 设置窗口大小(宽高)，x是小写的字母，不是乘号
# win.minsize('400x600')  # 设置窗口最小尺寸（宽高）
# win.maxsize('1440x800')  # 设置窗口最大尺寸（宽高）
win.mainloop()  # 进入消息循环，也就是显示窗口
