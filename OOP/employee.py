# Python Object Oriented Programming
class Employee:

    raise_amt = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    # Magic(Dunder) methods
    # __repr__ gives an unambigious representation of the object
    # Mainly used for debugging and logging and stuff meant for other developers
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    # __str__ gives readable representation of an object
    # Meant to be used as a display to the end user
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # __len__ returns the length of the giving string
    def __len__(self):
        return len(self.fullname())

    # __add__ tells python how to handle '+' operations for objects of this class
    # You can find more of the dunder methods on the python stdlib documentation
    def __add__(self, other):
        return self.pay + other.pay

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # @property decorator is used here as a getter
    @property
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)

    # @property decorator is used here as a getter
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    # @fullname.setter decorator is a setter function for the fullname property
    # Syntax: @property_to_affect.setter
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # @fullname.setter decorator is a deleter function for the fullname property
    # Syntax: @property_to_affect.deleter
    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None

    # Class methods by convention take the first argument -
    # cls(read: class) which serves the same purpose as self
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        "Parses hyphen seperated employee data strings and returns a class object"
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # Static methods are methods that do not have to pass the instance or the class
    # but have logical connection to the class
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    "Class Developer inherits from class Employee. That above is the syntax"
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


emp_1 = Employee('Gideon', 'Anyalewechi', 20000)
emp_2 = Employee('Uchenna', 'Okeke', 25000)

# mgr_1 = Manager('Tony', 'Elumelu', 40000, [dev_1])

# print()

# Built-in. Returns T/F if arg1 is subclass(or not) of arg2
# print(issubclass(Developer, Employee))
# Built-in. Returns T/F if arg1 is instance(or not) of arg2
# print(isinstance(mgr_1, Manager))
# Built-in. Gives information about a passed-in argument(Usually a class)
# print(help(Developer))
# Built-in. Accessing an object's name space
# print(Employee.__dict__)
