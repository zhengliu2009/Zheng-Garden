print('ATTENTION'.center(50,'*'))
print('***********PLEASE FOLLOW INSTRUCTIONS***********')
print('\n')

print("If you want to input a chemical's name, press 1.")
print('If you want to input two elements, press 2.')
print('If you want to input three elements, press 3.')
#here I tried to use \n but failded
print('\n')

user_input = input('Tell me what you want: ')
print('\n')
#part 1 is for extra credit 3 and 4; part 2 has additional compound for extracredit 1; part 3 is for extra credit 2
#Decomposing a compound name into its elements and parts.
if user_input == "1":
 print("Please choose one chemical's name from the list below: water, hydrogen peroxide, carbon dioxide, carbon monoxide, sodium chloride, ammonia, hydrochloric acid, methane, ethane, iron oxide")
 print('\n')
 name = input('I want to know how to make: ')
 print('\n')
 if name == "water":
      print('You need 2 prats of H and 1 part of O to make {}.'.format(name))
#{}is used here as an example.
      
 elif name == 'hydrogen peroxide':
      print('You need 1 part of H and 1 part of O to make {}.'.format(name))
 elif name == "carbon dioxide":
      print('You need 1 prats of C and 2 part of O to make {}.'.format(name))
 elif name == "carbon monoxide":
      print('You need 1 prats of C and 1 part of O to make {}.'.format(name))
 elif name == "sodium chloride":
      print('You need 1 prats of Na and 1 part of Cl to make {}.'.format(name))
 elif name == "ammonia":
      print('You need 1 prats of N and 3 part of H to make ammonia.')
 elif name == "hydrochloric acid":
      print('You need 1 prats of H and 1 part of Cl to make {}.'.format(name))
 elif name == "methane":
      print('You need 1 prats of C and 4 part of H to make {}.'.format(name))
 elif name == "ethane":
      print('You need 2 prats of C and 6 part of H to make {}.'.format(name))
 elif name == "iron oxide":
      print('You need 1 prats of Fe and 1 part of O to make {}.'.format(name))
 else:
   print("Is that your name? It's not in my list.")

#Compounds of two parts.
if user_input == "2":
 print('Please use only following elements: H, O, C, Na, Cl, N and Fe.')
 print('\n')
#input first element as element_1, parts_1;

 element_1 = input('Please provide an element symbol for the first element:')
 parts_1 = input('Please provide the number of parts of "{}":'. format(element_1))

#input first element as element_2, parts_2;

 element_2 = input('Please provide an element symbol for the second element:')
 parts_2 = input('Please provide the number of parts of "{}":'. format(element_2))
 print('\n')
#check whether compound is valid H2O and H2O2

 if element_1 == "H" and element_2 == "O":
  if parts_1 == "2" and parts_2 == "1":
   print('You have mixed 2 parts of "H" with 1 parts of "O" to make water.')
     
  if parts_1 == "2" and parts_2 == "2":
   print('You have mixed 2 parts of "H" with 2 parts of "O" to make Hydrogen peroxide.')

#check whether compound is valid CO and CO2
 
 elif element_1 == "C" and element_2 == "O":
    if parts_1 == "1" and parts_2 == "1":
        print('You have mixed 1 parts of "C" with 1 parts of "O" to make carbon monoxide.')
    
    if parts_1 == "1" and parts_2 == "2":
        print('You have mixed 1 parts of "C" with 2 parts of "O" to make carbon dioxide.')

#FeO

 elif element_1 == "Fe" and element_2 == "O" and parts_1 == "1" and parts_2 == "1":
  print('You have mixed 1 parts of "Fe" with 1 parts of "O" to make iron oxide (rust).')

#HCl and NaCl

 elif  parts_1 == "1" and parts_2 == "1":
    if element_1 == "Na" and element_2 == "Cl":
     print('You have mixed 1 parts of "Na" with 1 parts of "Cl" to make sodium chloride (salt).')

    if element_1 == "H" and element_2 == "Cl":
        print('You have mixed 1 parts of "H" with 1 parts of "Cl" to make hydrochloric acid.')

#check whether compound is valid CH4 and C2H6

 elif element_1 == "C" and element_2 == "H":
    if parts_1 == "1" and parts_2 == "4":
        print('You have mixed 1 parts of "C" with 3 parts of "H" to make methane.')
    
    if parts_1 == "2" and parts_2 == "6":
        print('You have mixed 1 parts of "C" with 2 parts of "H" to make ethane.')

#check whether compound is NH3

 elif element_1 == "N" and element_2 == "H":
  if parts_1 == "1" and parts_2 == "3":
   print('You have mixed 1 parts of "N" with 3 parts of "H" to make amminia.')

#handling one additional compound: Fe2O3.
 elif element_1 == "Fe" and element_2 == "O" and parts_1 == "2" and parts_2 == "3":
  print('You have mixed 2 parts of "Fe" with 3 parts of "O" to make Fe2O3. It is also rust')

 else:
   print('Sorry, I do not know how to mix those elements together.')

#Compounds of three parts.
print('\n')
if user_input == "3":
    print('\n')
    print('Programmers are not chemistry major. I can only handle compounds with Na H C O.')
    element_1 = input('Please enter your first element: ')
    element_2 = input('Please enter your second element: ')
    element_3 = input('Please enter your third element: ')
    print('\n')
    if element_1 == "H" and element_2 == "C" and element_3 == "O":
        print('The only compound you can make with H C and O is H2CO3.')
    elif element_1 == "Na" and element_2 == "C" and element_3 == "O":
        print('The only compound you can make with Na C and O is Na2CO3.')
    else:
        print('\n')
        print('We are NOT friends!')           
