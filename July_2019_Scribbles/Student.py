
class Student:

    def __init__(self, name, reg_no, gpa, is_regular):
        self.name = name
        self.reg_no = reg_no
        self.gpa = gpa
        self.is_regular = is_regular

    def on_first_class(self):
        if self.gpa >= 4.5:
            return True
        else:
            return False