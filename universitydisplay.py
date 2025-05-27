# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Subclass - Student
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")

# Subclass - Lecturer
class Lecturer(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")

# Subclass - Staff
class Staff(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

# Example usage
people = [
    Student("Alice", 20, "S123"),
    Lecturer("Dr. Bob", 45, "Mathematics"),
    Staff("Charlie", 38, "Administration")
]

for person in people:
    person.display_info()

