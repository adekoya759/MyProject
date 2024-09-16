
with open(r'C:\Users\HP\Documents\Python\pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)



with open(r'C:\Users\HP\Documents\Python\pi_digits.txt') as file_object:
    lines = file_object.readlines()
    
    for line in lines:
        print(line.rstrip())


with open(r'C:\Users\HP\Documents\Python\pi_digits.txt') as file_object:
    lines = file_object.readlines()
    
    pi_string = ''

    for line in lines:
        
        pi_string += line.rstrip()

    print(pi_string)

print(len(pi_string))

birthday = input('Enter your birthday(DMYY): ')

if birthday in pi_string:
    print('Your birthday can be found in the pi string')

else:
    print("Your birthday is no where to be found")