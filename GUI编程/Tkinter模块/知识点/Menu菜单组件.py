#!usr/bin/env python
# -*-coding:utf-8-*-

"""
@Author: jingfei Chen
@Time: 2019-05-16 19:23 
@Email: 953209336@qq.com
"""
import tkinter as tk

win = tk.Tk()  # 创建一个窗口对象
win.title('我的第一个Windows窗口')  # 设置窗口标题


def hello():
    print('你单击主菜单')


menu = tk.Menu(win)  # 创建主菜单对象
for item in ['文件', '编辑', '视图']:  # 添加菜单项
    menu.add_command(label=item, command=hello)

win['menu'] = menu  # 将menu对象显示在窗口中

win.mainloop()  # 进入消息循环，也就是显示窗口
