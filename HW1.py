selection = 1
Inputs = []

for item in range(5) :
    
    print('\nTHIS IS  {}. SELECTION'.format(selection))
    print('\nPlease select type of your input! \n\nEnter 1 for integer number \nEnter 2 for float number  \nEnter 3 for string or character')
    type_selection = int(input('\nYour selection is : '))
    
    if type_selection ==1 :
        my_input = int(input('\nPlease enter your input :'))
        Inputs.append(my_input)
                 
    if type_selection == 2 :
        my_input = float(input('\nPlease enter your input :'))
        Inputs.append(my_input)
    
    if type_selection == 3 :
        my_input = str(input('\nPlease enter your input :'))
        Inputs.append(my_input)
    
    selection+=1
    
selection = 1 
print('\n\n')
for item in range(5) :
    print ('My {}. input is : {} | type of it is : '.format(selection , Inputs[item]) , type(Inputs[item]))
    selection+=1
