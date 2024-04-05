class Dog:
    legs = 4

    # 'self' references the instances of the classes
    def __init__(self, name, age): # '__init__' is used as a constructor to do something when the object is created
        self.name = name
        self.age = age
    
    @classmethod
    def speak(cls): # This is no longer a function, this a method because belongs to the class
        print("guau!")
    
    # Factory method - will create instances of dog
    @classmethod
    def factory(cls):
        return cls("Dobby", 4)

my_dog = Dog("Dobby", 5)
my_dog.speak()

another_dog = Dog.factory()
print(another_dog.name, another_dog.age)

Dog.speak()