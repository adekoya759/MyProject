          
def build_profile(first, last, **user_profile):
   
    user_profile['first_name'] = first
    user_profile['last_name'] = last
    return user_profile
    
users_profile = build_profile("Oluwatobi", "Adekoya", location='Lagos', field='computer engineering')
    
print(users_profile)
    
    

