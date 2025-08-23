class Car:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def fullname(self):
        return f"{self.brand}-{self.model}"

class ElectricCar(Car):
    def __init__(self, model, brand, battery):
        super().__init__(model, brand)
        self.battery = battery

    def full_info(self):
        return f"{self.brand}-{self.model} with {self.battery}"


ev = ElectricCar("V", "BYD", 54)
tesla = ElectricCar("Scor E", "Mahindra", 355)
print(tesla.full_info())