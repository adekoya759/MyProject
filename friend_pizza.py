pizzas = ['Neapolitan', 'Silician', 'Roman-style', 'Chicago Deep-dish', 'York-style', 'Californian',
          'Detriot', 'St. Louis', 'Canadian', 'Mexican', 'South American', 'French', 'Spanish', 'Bagel', 
          'Breakfast', 'Bagel','Breakfast', 'Dessert', 'Calzone', 'Bresaola', 'Crudaiola', 'Caviar']

friend_pizzas = ['Sauerkraut', 'Bone Marrow', 'Chicken Tikka','Nutella', 'Avocado Biltong', 'Harissa', 'Zapiekanka', 
          'Tarte Flambee', 'Scachatta', 'Moroccan', 'Lahmajoun', 'Crocodile', 'Emu', 'Eggplant', 'Iranian Beef']

for pizza in pizzas:
    if pizza in friend_pizzas:
        print(f"{pizza} pizza is available in both lists")

else:
    print("The list is unique")
