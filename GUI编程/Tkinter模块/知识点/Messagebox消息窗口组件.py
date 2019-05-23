#!usr/bin/env python
# -*-coding:utf-8-*-

"""
@Author: jingfei Chen
@Time: 2019-05-16 19:37 
@Email: 953209336@qq.com
"""

import tkinter as tk
from tkinter import messagebox as msgbox

win = tk.Tk()  # 创建一个窗口对象
win.title('MsgBox Test')  # 设置窗口标题


def btn1_clicked():
    msgbox.showinfo(title="Info", message="Showinfo test.")


def btn2_clicked():
    msgbox.showwarning("Warning", "Showwarning test.")


def btn3_clicked():
    msgbox.showerror("Error", "Showerror test.")


def btn4_clicked():
    msgbox.askquestion("Question", "Askquestion test.")


def btn5_clicked():
    msgbox.askokcancel("OkCancel", "Askokcancel test.")


def btn6_clicked():
    msgbox.askyesno("YesNo", "Askyesno test.")


def btn7_clicked():
    msgbox.askretrycancel("Retry", "Askretrycancel test.")


btn1 = tk.Button(win, text='Showinfo', command=btn1_clicked)

"""fill=X 当GUI窗体大小发生变化时，widget在X方向跟随GUI窗体变化 
fill=Y 当GUI窗体大小发生变化时，widget在Y方向跟随GUI窗体变化 
fill=BOTH 当GUI窗体大小发生变化时，widget在X、Y两方向跟随GUI窗体变化
"""
btn1.pack(fill=tk.X)

btn2 = tk.Button(win, text='Showwarning', command=btn2_clicked)
btn2.pack(fill=tk.X)
btn3 = tk.Button(win, text='Showerror', command=btn3_clicked)
btn3.pack(fill=tk.X)
btn4 = tk.Button(win, text='Askquestion', command=btn4_clicked)
btn4.pack(fill=tk.X)
btn5 = tk.Button(win, text='Askokcancel', command=btn5_clicked)
btn5.pack(fill=tk.X)
btn6 = tk.Button(win, text='Askyesno', command=btn6_clicked)
btn6.pack(fill=tk.X)
btn7 = tk.Button(win, text='Askretrycancel', command=btn7_clicked)
btn7.pack(fill=tk.X)

win.mainloop()  # 进入消息循环，也就是显示窗口
