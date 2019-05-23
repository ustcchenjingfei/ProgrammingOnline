#!usr/bin/env python
# -*-coding:utf-8-*-

"""
@Author: jingfei Chen
@Time: 2019-05-16 20:14 
@Email: 953209336@qq.com
"""

import tkinter as tk

win = tk.Tk()  # 创建一个窗口对象
win.title('使用Frame组件的例子')  # 设置窗口标题

f1 = tk.Frame(win)
f1.pack()

f2 = tk.Frame(win)
f2.pack()

f3 = tk.LabelFrame(win, text="LabelFrame是有标题的Frame")
f3.pack(side=tk.BOTTOM)  # 放置在窗口底部

redbutton = tk.Button(f1, text="Red", fg="red")  # 背景颜色
redbutton.pack(side=tk.LEFT)

bluebutton = tk.Button(f1, text="Blue", fg="blue")  # 背景颜色
bluebutton.pack(side=tk.LEFT)

brownbutton = tk.Button(f1, text="Brown", fg="brown")  # 背景颜色
brownbutton.pack(side=tk.LEFT)

blackbutton = tk.Button(f2, text="Black", fg="black")  # 背景颜色
blackbutton.pack()

greenbutton = tk.Button(f3, text="Green", fg="green")  # 背景颜色
greenbutton.pack()

win.mainloop()  # 进入消息循环，也就是显示窗口
