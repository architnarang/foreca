# foreca
Approach to the spell-checker : Ive predefined a list which contains the name of all the vegetables supplied by foreca , when a person
                               inputs a set of vegetables then the program checks for each vegetable in the pre defined list and if it 
                               doesnt find a match , then it prints out the element which didnt match along with a message like the spelling
                               is incorrect or something similiar.

final product 1.0:contains the whole program except that it doesnt specify which spelling is incorrect, it just prints out that there is a spelling error.
final product 1.1:contains the whole program and it returns exactly which spelling is incorrect
                  problem:  let predefined list be tomato,onion,potato
                  and if i input cabbage 
                  instead of getting 'cabbage':check spelling im getting
                  'c':spelling incorrect
                  'a':spelling incorrect 
                  ...
                  'e':spelling incorrect

this seems like a small issue and can be resolved within some time.


test 1.0:code which checks the value input by the user doesnt match with a pre defined list and returns the value which didnt match as an output.(only integers)
test 1.1:this code seperates the numerical part from a text(like potato12 to 'potato' and '12')
test 1.2:extension of previous ,addition; it exports to an xlsx file
test 1.3:extension of test1.0 but this takes in str values 
test 1.4:seperates the input text to a list(like potato,onion to ['potato','onion'])
test 1.5:sample code which exports a list to an xlsx file
