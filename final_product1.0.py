#the code w/o the spell checker
#it just shows that there is an incorrect spelling but doesnt specify which one.

import re
import xlsxwriter
from string import digits


print("Please seperate vegetables using a comma(,)")
order=input("Enter order here:")
order1=order.strip()
order2=order1.replace(" ","")

order_sep=order2.split(',')
removed_digits=str.maketrans('','',digits)
vegetables=order.translate(removed_digits)

vegetables_in_list=['potato','onion','cabbage']


if vegetables in vegetables_in_list:
        
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
else:
      print("The spelling is incorrect, please check for the spelling")

    



