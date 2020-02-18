#sample program which exports the list to xlsx file
import xlsxwriter
workbook=xlsxwriter.Workbook('C:\\Users\\sahay\\Desktop\\python\\order_placement.xlsx')
worksheet=workbook.add_worksheet("Sample")
vegetables=[('potato', '2'), ('cabbage', '3'), ('brocolli', '5')]

row=0
col=0

for vegetable,quantity in(vegetables):
    worksheet.write(row,col,vegetable)
    worksheet.write(row, col + 1,quantity)
    row +=1

workbook.close()
