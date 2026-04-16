def make_pizza(size, *toppings):
    """Make a pizza with the given size and toppings."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"  - {topping}")
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
class Car1:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):#這裡定義了一個方法update_odometer用來更新odometer_reading這個屬性的值
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print(f"odometer updated to {self.odometer_reading} miles.")
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):#這裡定義了一個方法increment_odometer用來增加odometer_reading這個屬性的值
        if miles < 0:#這裡加了一個條件如果miles是負的就不增加odometer_reading的值
            print("You can't increment the odometer with negative miles!")
        else:
            self.odometer_reading += miles
            print(f"odometer incremented by {miles} miles. Total is now {self.odometer_reading} miles.")
class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75, show_battery=True):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        self.show_battery = show_battery
    def describe_battery(self):
        """Print a statement describing the battery size."""
        if not self.show_battery:
            return
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        else:
            return
        print(f"This car can go approximately {range} miles on a full charge.")
class ElectricCar(Car1):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year, battery_size=None):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        show_battery = battery_size is not None
        actual_battery_size = 75 if battery_size is None else battery_size
        self.battery = Battery(actual_battery_size, show_battery)
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        if self.battery.show_battery:
            long_name += f" with a {self.battery.battery_size}-kWh battery"
        return long_name.title()
class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print(f"odometer updated to {self.odometer_reading} miles.")
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        if miles < 0:
            print("You can't increment the odometer with negative miles!")
        else:
            self.odometer_reading += miles
            print(f"odometer incremented by {miles} miles. Total is now {self.odometer_reading} miles.")
class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go approximately {range} miles on a full charge.")
class ElectricCar(Car1):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year, battery_size):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery(battery_size)  # 在 ElectricCar 中創建一個 Battery 實例
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model} with a {self.battery.battery_size}-kWh battery"
        return long_name.title()
class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=None):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        if self.battery_size is None:
            return
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        else:
            return
        print(f"This car can go approximately {range} miles on a full charge.")
class ElectricCar(Car1):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year, battery_size=None):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery(battery_size)  # 在 ElectricCar 中創建一個 Battery 實例
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        if self.battery.battery_size is not None:
            long_name += f" with a {self.battery.battery_size}-kWh battery"
        return long_name.title()
