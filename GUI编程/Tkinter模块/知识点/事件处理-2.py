#!usr/bin/env python
# -*-coding:utf-8-*-

"""
@Author: jingfei Chen
@Time: 2019-05-20 18:59 
@Email: 953209336@qq.com
"""
import tkinter as tk

def printkey(event):  # 监听键盘事件
    print('你按下了:' + event.char)

win = tk.Tk()  # 创建一个窗口对象
win.title('我的第一个Windows窗口')  # 设置窗口标题


entry = tk.Entry(win)  # 实例化一个单行输入框对象
entry.bind('<KeyPress>', printkey)
entry.pack()

win.mainloop()  # 进入消息循环，也就是显示窗口
