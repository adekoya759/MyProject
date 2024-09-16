class User:
    
    def __init__(self, first_name, last_name, **user_profile):
        self.first_name = first_name
        self.last_name = last_name
        self.user_profile = user_profile
        self.login_attempts = 0
    
    def describe_user(self):

        self.user_profile['first_name'] = self.first_name
        self.user_profile['last_name'] = self.last_name

        print(f"The user's information include {self.user_profile}")
    
    def greet_user(self):

        print(f"Hello {self.first_name} {self.last_name}. I hope you are great!")

    def increment_login_attempts(self):

        self.login_attempts += 1
        print(self.login_attempts)


class Privileges:

    def __init__(self):
        self.privileges =  ["can add post", "can delete post", "can ban user"]

class Admin(User):

    def __init__(self, first_name, last_name, **user_profile):
        super().__init__(first_name, last_name, **user_profile)

        self.privileges = Privileges()

    def show_privileges(self):
        
        print (f"{self.first_name}")
        print (f"\t{self.privileges}")






my_admin = Admin('Femi', 'Adekoya', location = 'London', university = 'Abu Dhabi')
my_admin.describe_user()
my_admin.greet_user()
my_admin.show_privileges()

print('\n')
my_user = User('Oluwatobi', 'Adekoya', location='Lagos', field='computer engineering')
my_user1 = User('Tunde', 'Onokoya', Country = "Nigeria", Age=27, Postal_Code = "A101", support_area ="EMEA")

       
my_user.describe_user()
my_user.greet_user()
my_user.increment_login_attempts()
print('\n')
my_user1.describe_user()
my_user1.greet_user()