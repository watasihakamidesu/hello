import xlrd

data = xlrd.open_workbook('test.xls')
table = data.sheets()[0]
num = table.nrows
for i in range(num):
    for val in table.row_values(i):
        print val,
    print ""
    if i==0:
        print '-' * 30
