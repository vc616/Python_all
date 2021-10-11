import openpyxl

# 加载 excel 文件
wb = openpyxl.load_workbook("C:/Users/VM/Desktop/信息.xlsx")

# 得到sheet对象
sheet = wb['年龄表-最前']

sheet['E10'] = '修改一下'

## 指定不同的文件名，可以另存为别的文件
wb.save("C:/Users/VM/Desktop/信息1.xlsx")
