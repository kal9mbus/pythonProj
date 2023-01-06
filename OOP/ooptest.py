class Cat:
    breed = 'pers'

    def set_value(self, value, age=0):
        self.name = value
        self.age = age
    
    def __init__(self):
        print('Hello new object is ', self)
tom = Cat()
