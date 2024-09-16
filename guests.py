"""A program that prompts users for their names """

filename = r'C:\Users\HP\Documents\Python\guest.txt'

while True:
    print('Press q to quit')
    full_name = input("Enter your full name: ").lower()

    if full_name == 'q':
        break
    else: 
        with open(filename, 'a') as file_object:
            your_name = file_object.write(f"\n{full_name.title()}")
