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