class Person:
    name = 'Матроскин'
    color = 'black'
a = Person()
a.valera = 'izmen'

print("Person.__dict__ = ",Person.__dict__)
print("a.__dict__ = ", a.__dict__)

Person.valera = '222'
print("Person.__dict__ = ",Person.__dict__)
print("a.__dict__ = ", a.__dict__)

print("Person.__dict__ = ",Person.__dict__)
print("a.__dict__ = ", a.__dict__)
del a.valera
print("Person.__dict__ = ",Person.__dict__)
print("a.__dict__ = ", a.__dict__)
