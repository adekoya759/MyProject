new_pizza_list = []

pizzas = ['Neapolitan', 'Silician', 'Roman-style', 'Chicago Deep-dish', 'York-style', 'Californian',
          'Detriot', 'St. Louis', 'Canadian', 'Mexican','Scachatta', 'Moroccan', 'South American', 'French', 'Spanish', 'Bagel', 
          'Breakfast', 'Bagel','Breakfast', 'Dessert', 'Calzone', 'Bresaola', 'Crudaiola', 'Caviar']

friend_pizzas = ['Sauerkraut', 'Bone Marrow', 'Chicken Tikka','Nutella', 'Avocado Biltong','Dessert', 'Calzone', 'Harissa', 'Zapiekanka', 
          'Tarte Flambee', 'Scachatta', 'Moroccan', 'Lahmajoun', 'Crocodile', 'Emu', 'Eggplant', 'Iranian Beef']

for pizza in pizzas:
    if pizza in friend_pizzas:
        new_pizza_list.append(pizza)

print(new_pizza_list)

    
     
