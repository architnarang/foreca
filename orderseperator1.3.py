lst1=['tomato','potato','onion']
a1=input().strip()
a=a1.split(',')

user_input=[str(i) for i in a]

for _input in user_input:
    for veg in [str(i) for i in str(_input)]:
        if veg not in lst1:
            print(f"{veg}:spelling incorrect")

            
