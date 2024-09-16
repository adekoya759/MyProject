class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

        print(f"My new restaurant is {self.restaurant_name.title()}")

        print(f"The only available cuisine in the new restaurant is {self.cuisine_type.title()}")


    def describe_restaurant(self):

        print(f"The restaurant name is {self.restaurant_name.title()} and the cuisine available is {self.cuisine_type.title()}")

    def open_restaurant(self):

        print(f"{self.restaurant_name.title()} is open to the public. Come and have a taste of the best delicacy in town!")

