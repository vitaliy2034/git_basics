class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'


class Employee(Person):
    def __init__(self, name, age, employee_id, position):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.position = position

    def __repr__(self):
        return (f'Employee(name={self.name}, age={self.age}, '
                f'employee_id={self.employee_id}, position={self.position})')


class Company:
    def __init__(self, name, employees=None):
        self.name = name
        self.employees = employees if employees is not None else []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)

    def __repr__(self):
        return f'Company(name={self.name}, employees={self.employees})'
