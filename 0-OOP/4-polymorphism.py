class Laptop:
    total_laptop = 0

    def __init__(self, model, year, os_type):
        self.model = model
        self.year = year
        self.os_type = os_type
        Laptop.total_laptop += 1

    @staticmethod
    def desc():
        return "This is portable PC"

class WindowLaptop(Laptop):
    def __init__(self, model, year, os_type):
        super().__init__(model,year, os_type)

    def operation_system(self):
        return f"OS is {self.os_type}"


class AppleLaptop(Laptop):
    def __init__(self, model, year, os_type):
        super().__init__(model, year, os_type)

    def operation_system(self):
        return f"OS is {self.os_type}"

macbook = AppleLaptop("M4 Air", 2025, "MacOS")
dell = WindowLaptop("Vostro", 2020, "Window 11")

print(macbook.operation_system())
print(dell.operation_system())
print("Total Laptop created: ", Laptop.total_laptop)
print(Laptop.desc())
