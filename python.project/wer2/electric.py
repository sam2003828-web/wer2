class ElectricCar:
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year, battery_size=None):
        """Initialize attributes of the parent class."""
        self.make = make
        self.model = model
        self.year = year
        self.show_battery = battery_size is not None
        self.battery = 75 if battery_size is None else battery_size
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        if self.show_battery:
            long_name += f" with a {self.battery}-kWh battery"
        return long_name.title()
"""is not None 是用來檢查 battery_size 是否有被賦值，
如果有就把它加到 long_name 中，如果沒有就不加。
這樣就可以讓 get_descriptive_name 方法在 battery_size 
沒有被賦值的情況下仍然能夠正常運作，而不會出現錯誤。
not none 是一個常見的 Python 表達式，用來檢查一個變量是否為 None。
"""
#class ElectricCar(Car1):
#   """Represent aspects of a car, specific to electric vehicles."""
#   def __init__(self, make, model, year, battery_size=None):
#        """Initialize attributes of the parent class."""
#        super().__init__(make, model, year)
#        self.battery = Battery(battery_size)  # 在 ElectricCar 中創建一個 Battery 實例
#    def get_descriptive_name(self):
#      """Return a neatly formatted descriptive name.""
#        long_name = f"{self.year} {self.make} {self.model}"
#        if self.battery.battery_size is not None:
#            long_name += f" with a {self.battery.battery_size}-kWh battery"
#        return long_name.title()
"""is not None 是用來檢查 battery_size 是否有被賦值，
如果有就把它加到 long_name 中，如果沒有就不加。
這樣就可以讓 get_descriptive_name 方法在 battery_size 
沒有被賦值的情況下仍然能夠正常運作，而不會出現錯誤。
not none 是一個常見的 Python 表達式，用來檢查一個變量是否為 None。
"""
