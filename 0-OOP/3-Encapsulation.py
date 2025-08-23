class Student:
    def __init__(self, sid, name, course):
        self._sid = sid #_ make attribute private
        self._name = name
        self._course = course

    @property
    def sid(self):
        return self._sid

    @sid.setter
    def sid(self, value):
        if isinstance(value, int) and value > 0:
            self._sid = value
        else:
            print("Invalid sid, must be a positive integer!")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.strip() != "":
            self._name = value
        else:
            print("Inavalid")

        # Example usage
s = Student(1, "Bibek", "CS")
print(s.sid)   # calls getter
s.sid = 10     # calls setter
print(s.sid)
s.sid = ""     # invalid

print(s.name)
