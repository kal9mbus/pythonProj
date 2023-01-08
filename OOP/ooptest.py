class Cat:
    def __init__(self, name , breed='pers', age=1, color='white'):
        print(f'Hello new cat is {name}, he is  {breed}, and {age} years old. His color is {color}')
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

tom = Cat('Tom')
walt = Cat("Walt", 'britain', 2, 'black')

class Laptop():
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

hp = Laptop('hp','15-3321', 5600)
print(hp.price)
    
class SoccerPlayer():
    def __init__(self, name, surname, goals=0, assists=0 ):
        self.name = name
        self.surname = surname
        self.goals = goals
        self.assists = assists
    def score(self, goals = 1):
        self.goals = goals
    def make_assists(self, assists = 1):
        self.assists = assists
    def statistics(self):
        print(f"{self.name} {self.surname}  - голы {self.goals}, передачи {self.assists}")
cris = SoccerPlayer("Cristiano", "Ronaldo")

cris.score(2)
cris.make_assists(2)
cris.statistics()
messi = SoccerPlayer('Lionel', "Messi")
messi.make_assists(20)
messi.score(30)
messi.statistics()

class Zebra():
    def __init__(self, stripe = 'Полоска белая'):
        self.stripe = stripe
    def which_stripe(self):
        if self.stripe == 'Полоска белая':
            print('Полоска белая')
            self.stripe = 'Полоска черная'
        else:
            print('Полоская черная')
            self.stripe = 'Полоска белая'

z1 = Zebra()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()

z2 = Zebra()
print()
z2.which_stripe()

class Person():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def full_name(self):
        print(f"{self.first_name} {self.last_name}")
    def is_adult(self):
        if self.age >=18:
            print("Больше 18 лет")
        elif self.age <18 and self.age >=0:
            print("Возраст меньше 18")
        else:
            print("Возраст не подходит")

p1 = Person('Jimmy', 'Hendrix', -2)
p1.full_name()
p1.is_adult()

class Point():
    list_points = []

    def __init__(self, coord_x=0, coord_y=0):
        self.move_to(coord_x, coord_y)
        Point.list_points.append(self)
    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def go_home(self):
        self.move_to(0,0)
    def location(self):
        print(f"X = {self.x} and y = {self.y}")

p1 = Point(2)
p1.location()
p2 = Point(2,2)
p2.location()
p2.move_to(44,22)
p2.location()
print(Point.list_points[1].x)

class Stack():
    def __init__(self):
        self.values = []
    def push(self, item):
        self.values.append(item)
    def size(self):
        print(len(self.values))
    def pop(self):
        del(self.values[-1])
    def is_empty(self):
        if not self.values:
            return True
        else:
            return False
st = Stack()
st.push('cat')
st.push('dog')
st.size()
st.pop()
st.size()
print(st.is_empty())
st.pop()
print(st.is_empty())

