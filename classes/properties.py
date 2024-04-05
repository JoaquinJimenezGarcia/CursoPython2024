class Dog:
    legs = 4

    # 'self' references the instances of the classes
    def __init__(self, name, age): # '__init__' is used as a constructor to do something when the object is created
        self.name = name
        self.age = age
    
    def speak(self): # This is no longer a function, this a method because belongs to the class
        print(f"{self.name} said: guau!")

my_dog = Dog("Tom", 1)
another_dog = Dog("Dob", 5)

print(my_dog.name)
print(another_dog.name)

my_dog.speak()
another_dog.speak()

my_dog.legs = 3

print(Dog.legs)
print(my_dog.legs)
print(another_dog.legs)