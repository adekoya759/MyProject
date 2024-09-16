import car 

my_tesla = car.ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print('\n')

my_beetle = car.Car('volkwagen', 'b2', 1992)
print(my_beetle.get_descriptive_name())
my_beetle.update_odometer(20_00)
my_beetle.increment_odometer(50)
my_beetle.read_odometer()