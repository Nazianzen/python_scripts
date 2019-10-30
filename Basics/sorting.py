
# li = [9,1,4,5,3,6,7,8,0,2]

# s_li = sorted(li)# (li, reverse=True) - for descending order

# print('Sorted Variable:\t', s_li)
# print('Original Variable:\t', li)

# li.sort() # (reverse=True) - for descending order

# print('Original Variable:\t', li)

# tup = (9,1,8,2,7,3,6,4,5,0)
# s_tup = sorted(tup) returns a sorted tup as a list

# print('Tuple\t', s_tup)

# di = {'name': 'Gideon', 'job': 'programming', 'age': 45, 'os': 'Windows'}
# s_di = sorted(di) # sorts the keys for dictionaries and returns them as a list

# print('Dict\t', s_di)

# li = [-6,-5,-4,1,2,3]
# s_li = sorted(li, key=abs)
# print(s_li)

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

from operator import attrgetter

e1 = Employee('Uchenna', 23, 35000)
e2 = Employee('Blessing', 35, 65000)
e3 = Employee('Orji', 30, 45000)

emps = [e1,e2,e3]

def e_sort(emp):# Returns the key with which to sort the employee list
    return emp.salary # Or .name, .age

s_emps = sorted(emps, key=e_sort, reverse=True)# This method is best for very
#   complicated situations

# s_emps = sorted(emps, key=lambda e: e.salary, reverse=True) # This lambda
#   function could be used to create quick anonymous functions in less
#   complicated situations

# s_emps = sorted(emps, key=attrgetter('name')) # This method uses the attrgetter
#   function in the operator module to get the passed-in attributes of the given
#   list

print(s_emps)
