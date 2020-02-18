#checks the input and prints spelling incorrect if input doesnt match with the elements of the pre defied (lst1) list.
#this code only takes in non numeric data.
#the output instead of showing 'banana':spelling incorrect shows 'b':spelling incorrect 'a':spelling incorrect...so on 
#id like your help in tackling that issue 
lst1=['tomato','potato','onion']
a1=input().strip()
a=a1.split(',')

user_input=[str(i) for i in a]

for _input in user_input:
    for veg in [str(i) for i in str(_input)]:
        if veg not in lst1:
            print(f"{veg}:spelling incorrect")

            
