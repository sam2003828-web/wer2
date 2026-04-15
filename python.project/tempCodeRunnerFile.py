class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #這裡定義了一個新的屬性odometer_reading並給它一個初始值0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")#這裡使用了odometer_reading這個屬性
my_new_car = Car('audi', 'a4', 2020)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
