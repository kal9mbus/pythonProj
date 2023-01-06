class Cat:
    breed = 'pers'

    def set_value(self, value, age=0):
        self.name = value
        self.age = age
    
    def __init__(self, name , breed, age, color):
        print('Hello new object is ', self, name , breed, age, color)
tom = Cat()
