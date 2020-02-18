from string import digits

a=input()


removed_digits=str.maketrans('','',digits)
result=a.translate(removed_digits)
result1=result.strip()
result2=result1.replace(" ","")
result3=result2.split(',')

print(result3)
