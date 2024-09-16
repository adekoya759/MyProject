"""A program that prompts users for their names """

filename = r'C:\Users\HP\Documents\Python\response.txt'

while True:
    print('Press q to quit')
    full_name = input("Enter your full name: ").lower()
  
    if full_name == 'q':
        break
    
    y_programming = input("Why do you link programming? ").lower()

    if y_programming == 'q':
         break
    else: 
        print (f"Welcome {full_name.title()}. {y_programming}")

    with open(filename, 'a') as file_object:
            your_name = file_object.writelines(f"\n{full_name.title()}, {y_programming}")
