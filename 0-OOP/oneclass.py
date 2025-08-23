class College:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class School:
    def __init__(self, name, location, stype):
        self.name = name
        self.location = location
        self.type = stype

    def print_detail(self):
        return f"{self.name} and {self.location}"