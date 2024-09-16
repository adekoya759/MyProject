"""A program that performs addition"""

print("This program performs addition.")

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

while True:
    try:
        first_number = input("Enter the first number: ")

        for alphabet in alphabets:
         if first_number != alphabet:
            break
        second_number = input("Enter the second number: ")

        if second_number in alphabet:
             print("Please input a number")
        
        total = int(first_number) + int(second_number)
    except ValueError:
        print('Please input an integer')
    
    else:
        break
print(total)
    
