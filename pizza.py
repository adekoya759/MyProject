
pizzas = ['Neapolitan', 'Silician', 'Roman-style', 'Chicago Deep-dish', 'York-style', 'Californian',
          'Detriot', 'St. Louis', 'Canadian', 'Mexican', 'South American', 'French', 'Spanish', 'Bagel', 
          'Breakfast', 'Bagel','Breakfast', 'Dessert', 'Calzone', 'Bresaola', 'Crudaiola', 'Caviar', 
          'Sauerkraut', 'Bone Marrow', 'Chicken Tikka','Nutella', 'Avocado Biltong', 'Harissa', 'Zapiekanka', 
          'Tarte Flambee', 'Scachatta', 'Moroccan', 'Lahmajoun', 'Crocodile', 'Emu', 'Eggplant', 'Iranian Beef']

for pizza in pizzas:
    print(f"\nI like {pizza} pizza")

print(len(pizzas))

print(f"The first three items in the list are: {pizzas[:3]}")

print(f"\nThe three items from the middle of  the list are: {pizzas[17:20]}")

print(f"\n The last three items in the list are: {pizzas[-3:]}")