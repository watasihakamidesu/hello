import xlwt

workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('My Worksheet')
column = ["username", "groups", "email"]
rows = [
    ["jhchen", "a", "watasihakamidesu@sina.cn"],
    ["haha", "a", "text@sina.cn"],
    ["test", "test", "aaaaaaa@sina.cn"]
]
for i,val in enumerate(column):
    worksheet.write(0, i, label=val)
for num,row in enumerate(rows):
    for i,v in enumerate(row):
        worksheet.write(num+1, i, label=v)
workbook.save('test.xls')
