responses = {}

active = True

while active:

    name = input("What is your name please?")
    response = input("Where are you from?")

    responses[name] = response

    
    repeat = input("Do you still want to add another name? yes/no ")
    
    if(repeat == "no"):
        active = False
for name, response in responses.items():
    print(f"\nYour name is {name.title()} and your country is {response.title()}")


