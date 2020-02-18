#sample test code sub-part of the entire code
#it checks which element doesnt belong in the pre-defined list.
#obviously only works for integers,gotta change to str for string values.

lst1=[1,2,3]
a = input().split(' ')

user_input = [int(i) for i in a]

for _input in user_input:
    for num in [int(i) for i in str(_input)]:
        if num not in lst1:
            print(f"{num} does not belong to lst1")
