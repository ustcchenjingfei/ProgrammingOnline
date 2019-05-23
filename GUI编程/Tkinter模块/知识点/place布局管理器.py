#!usr/bin/env python
# -*-coding:utf-8-*-

"""
@Author: jingfei Chen
@Time: 2019-05-15 20:24 
@Email: 953209336@qq.com
"""

import tkinter as tk

win = tk.Tk()  # 创建一个窗口对象
win.title('登录')  # 设置窗口标题
# 设置窗口宽高
win['width'] = 200
win['height'] = 80
# python中坐标系是左上角为原点(0,0)，向右x坐标正方向，向下y坐标正方向
tk.Label(win, text='用户名', width=6).place(x=1, y=1)  # 绝对坐标(1,1)
tk.Entry(win, width=20).place(x=45, y=1)
tk.Label(win, text='密码是', width=6).place(x=1, y=20)
tk.Entry(win, width=20, show='*').place(x=45, y=20)
tk.Button(win, text='登录', width=8).place(x=40, y=40)
tk.Button(win, text='取消', width=8).place(x=110, y=40)

win.mainloop()  # 进入消息循环，也就是显示窗口
