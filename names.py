from name_function import get_formatted_name

print("Press 'q' to quit")

while True:
    first = input('Enter your first name:').lower()
    if first == 'q':
        break

    last = input('Enter your last name:').lower()
    if last == 'q':
        break
    fullname = get_formatted_name(first, last)

    print(fullname)


