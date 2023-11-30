# Create a new class Employee that inherits from the Person class.
# The Employee class will have additional attributes related to employment, such as employee_id and position.
# We'll also override the display_info method in the Employee class to include the new attributes.

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, first_name, last_name, age, employee_id, position):
        super().__init__(first_name, last_name, age)
        self.employee_id = employee_id
        self.position = position

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}, Position: {self.position}")



person = Person("John", "Doe", 30)
person.display_info()

employee = Employee("Lachezar", "Lazarov", 33, 101010, "QA")
employee.display_info()