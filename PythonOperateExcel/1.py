import openpyxl
import datetime

workbook = openpyxl.Workbook()  # 创建工作簿 （工作簿、工作表、单元格）
worktable = workbook.active  # 激活工作表

# print(worktable.title) #获取工作表名（默认Sheet）

worktable['A1'] = 520  # 第A列，第1行，(A1 字母和数字顺序不能变)
worktable.append([1, 2, 3])  # 对应 A2 B2 C2 (按行追加)
worktable['A3'] = datetime.datetime.now()  # A3
workbook.save('1.py_example.xlsx')  # 保存工作簿
