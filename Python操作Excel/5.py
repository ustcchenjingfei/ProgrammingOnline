import openpyxl
import datetime
from openpyxl.styles.colors import RED, GREEN, BLUE, YELLOW

wb = openpyxl.Workbook()
wt = wb.active

wt.append(['文本', '数字'])  # append是追加一行内容
wt['A2'] = '520'
wt['B2'] = 520
wb.save(r'5.py_example.xlsx')


# 数字格式
wt['A1'] = 88.8
wt['A1'].number_format = '#,###.00元'
wt['A2'] = datetime.datetime.today()
wt['A2'].number_format = 'yyyy-mm-dd'
wb.save(r'5.py_example.xlsx')


# 数字颜色
wt['A1'].number_format = '[RED]+#,###.00;[GREEN]-#,###.00'  # 顺序：正值，负值
wt['A1'] = 99

wt['A2'].number_format = '[RED]+#,###.00;[GREEN]-#,###.00'  # 顺序：正值，负值
wt['A2'] = -99

wt['A3'].number_format = '[RED];[GREEN];[BLUE];[YELLOW]'  # 顺序：正值，负值，零值，文本
wt['A3'] = 0

wt['A4'].number_format = '[RED];[GREEN];[BLUE];[YELLOW]'  # 顺序：正值，负值，零值，文本
wt['A4'] = 'FishC'
wb.save(r'5.py_example.xlsx')


# 替换
wt['A5'].number_format = '[=1]男;[=0]女'
wt['A5'] = 0
wt['A6'].number_format = '[=1]男;[=0]女'
wt['A6'] = 1
wt['A7'].number_format = '[=1]男;[=0]女'  # 其他用'#'替换
wt['A7'] = 2
wb.save(r'5.py_example.xlsx')

#加判断条件，进行替换
wt['A8'].number_format = '[<60][RED]不及格;[>=60][GREEN]及格'
wt['A8'] = 59
wt['A9'].number_format = '[<60][RED]不及格;[>=60][GREEN]及格'
wt['A9'] = 60
wb.save(r'5.py_example.xlsx')
