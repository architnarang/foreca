'''This contains the whole code'''

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


        workbook=xlsxwriter.Workbook('E:\\Aaryansh\\python\\forecaorder_placement.xlsx')
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
      user_input=[str(i) for i in vegetables]
      for _input in user_input:
          for veg in [str(i) for i in str(_input)]:
              if veg not in lst1:
                  print(f"{veg}:spelling incorrect")
          

      



    



