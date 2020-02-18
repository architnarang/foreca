#this code inputs the order,seperates the numerical part from the text and then exports it into a xlsx file.
#change line 16 according to the location of the xlsx file in your computer.

import re
import xlsxwriter
print("Please seperate vegetables using a comma(,)")
order=input("Enter order here:")
order1=order.strip()
order2=order1.replace(" ","")

order_sep=order2.split(',')

final_order=[re.findall(r'(\w+?)(\d+)', s)[0] for s in order_sep]


workbook=xlsxwriter.Workbook('C:\\Users\\sahay\\Desktop\\python\\order_placement.xlsx')
worksheet=workbook.add_worksheet("Sample")

vegetables=final_order

row=0
col=0

for vegetable,quantity in(vegetables):
    worksheet.write(row,col,vegetable)
    worksheet.write(row, col + 1,quantity)
    row +=1

workbook.close()


