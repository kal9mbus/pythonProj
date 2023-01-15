import re
class UserMail():
    def __init__(self, login, email):
        self.login = login
        self.__email = email
    def get_email(self):
        return self.__email
    def set_email(self, email):
        if re.search("[\w'._=-]+@[\w'._=-]+$", email):
            self.__email = email
        else:
            "Нет специальных символов"
    email = property(fget=get_email, fset=set_email)

e = UserMail('sssss','eeee@.com')
e.email = 'eeee@ds.co@m'
print(e.email)
e.email = 'dddddddddddd@....c'
print(e.email)


class BankAccount():
    def __init__(self, name, balance):
        self.name = name 
        self.__balance = balance
    
    @property
    def my_balance(self):
        print("Get balance")
        return self.__balance
    
    @my_balance.setter
    def my_balance(self, value):
        print("Set balance")
        if not isinstance(value, (int, float)):
            raise ValueError()
        self.__balance = value
    @my_balance.deleter
    def my_balance(self):
        print("delete balance")
        del self.__balance
    
    
    # my_balance = property()
    # my_balance = my_balance.getter(get_balance)
    # my_balance = my_balance.setter(set_balance)
    # my_balance = my_balance.deleter(delete_balance)

    #balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)

b1 = BankAccount('Misha', 200)

print(b1.my_balance)
b1.my_balance = 300
print(b1.my_balance)
del b1.my_balance
print()
print()
# class Person():
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#     @property
#     def name(self):
#         return self._name
    
#     @property
#     def age(self):
#         return self._age

# p1 = Person('Kela', 30)

# print()
# print()

class Notebook():
    def __init__(self, notes):
        self._notes = notes
    @property
    def print_notes(self):
        for i in range(len(self._notes)):
            print(self._notes[i])

n1 = Notebook(['Buy potato', 'Buy Carrot', 'Wash car'])
n1.print_notes


class Square():
    def __init__(self, s):
        self.__side = s
        self.__area = None
    
    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, num):
        self.__side = num
        self.__area = None


    @property
    def area(self):
        if self.__area is None:
            print("ras4et")
            self.__area = self.side ** 2
        return self.__area

s = Square(4)

print(s.area)
s.side = 2

print(s.area)

one_dollar = 20
print(f"{one_dollar:05}")

print()

class Robot():
    population = 0
    def __init__(self, name):
        self.name = name
        Robot.population += 1
        print(f"Робот {self.name} был создан")
    def say_hello(self):
        print(f"Робот {self.name} приветствует тебя, особь человеческого рода")
    
    @staticmethod
    def how_many():
        print(f"Нас {Robot.population}")

a = Robot("R2D2")
a.say_hello()
Robot.how_many()

print()
print()
class Person():
    def __init__(self, name, surname, gender = 'male'):
        self.name = name
        self.surname = surname
        self.gender = gender

    def __str__(self):
        if self.gender == 'male':
            return(f"Гражданин {self.name} {self.surname}")
        elif self.gender == 'female':
            return(f"Гражданка {self.name} {self.surname}")
        else:
            self.gender = 'male'
            return(f"Пусть будет гражданин с этого момента {self.name} {self.surname}")

a = Person("valera", 'kak skazat', 'female')
print(a)

print()
print()

class Vector():
    def __init__(self, *args):
        self.values = sorted(args)
        print(self.values)
    
    def __str__(self):
        if self.values:
            return f" Вектор({self.values})"
        else:
            return "Пустой вектор"
a = Vector(1,2,3,4)
b = Vector(2,3,4,5,6,7)
c = Vector()

