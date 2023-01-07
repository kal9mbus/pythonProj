class Cat:
    def __init__(self, name , breed='pers', age=1, color='white'):
        print(f'Hello new cat is {name}, he is  {breed}, and {age} years old. His color is {color}')
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

tom = Cat('Tom')
walt = Cat("Walt", 'britain', 2, 'black')