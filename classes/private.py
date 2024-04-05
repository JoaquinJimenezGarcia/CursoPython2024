class Dog:
    legs = 4

    # 'self' references the instances of the classes
    def __init__(self, name, age): # '__init__' is used as a constructor to do something when the object is created
        self.__name = name # prefix '__' makes an attribute private and can only be accesed by the functions in the class
        self.age = age

    def get_name(self):
        return self.__name
    
    def speak(self): # This is no longer a function, this a method because belongs to the class
        print(f"{self.__name} said: guau!")
    
    # Factory method - will create instances of dog
    @classmethod
    def factory(cls):
        return cls("Dobby", 4)

my_dog = Dog("Dobby", 5)
my_dog.speak()

another_dog = Dog.factory()

print(my_dog.get_name())
print(my_dog.__dict__)
print(another_dog.__dict__)