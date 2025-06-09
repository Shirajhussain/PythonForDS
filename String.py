#string
from os import lseek

#STRING REPLICATION

print('Ashish '*2)
print('-'*20)


#STRING LENGTH
print("Shiraj Hussain")
print(len('shiraj hussain'))
print('-'*20)


#STRING SLICING
print('shiraj hussain')
print('Ashish'[2])
print('Shiraj'[-6])
print('Shiraj Hussain'[0:6])
print('Shiraj Hussain'[7:14])
print('Shiraj Hussain'[3:6])
print('Shiraj Hussain'[7:14])
print('Shiraj Hussain'[3:14])
print('Shiraj Hussain'[3:])
print('Shiraj Hussain'[:14])
print('Shiraj Hussain'[-14:])
print('-'*20)

#STRING case CONVERSION
print('Shiraj Hussain'.lower())
print('Shiraj Hussain'.upper())
print('-'*20)


#STRING STRIPPING
print('       Shiraj Hussain      ')
print('       Shiraj Hussain      '.strip())
print('       Shiraj       Hussain      '.strip())
print('-'*20)

#STRING REPLACING
print('Shiraj Hussain')
print('shiraj Hussain'.replace('s','1'))
print('-'*20)


#STRING COUNT
print('Shiraj Hussain')
print('shiraj hussain'.count('s'))
print('Shiraj hussain'.lower().count('s'))
print('-'*20)



#STRING FIND
print('shiraj hussain')
print('shiraj hussain'.find('raj'))

print('-'*20)



#STRING CHECK
print('shiraj'.isalpha())
print('123'.isdigit())
print('shiraj'.islower())
print('SHIRAJ'.isupper())
print('-'*20)




#STRING CAPITALIZATION
print('shiraj hussain'.capitalize())
print('shiraj hussain'.title())
print('-'*20)


#CHECK FOR START AND END
print('Shiraj hussain'.startswith('Shi'))
print('hussain'.endswith('in'))
print('-'*20)



#SOME BASIC OPERATION IN STRING
print('Shiraj hussain'.center(20,"-"))
print('shiraj hussain'.ljust(20,"-"))
print('shiraj hussain'.rjust(20,"-"))
print('-'*20)

