class Dog:
    def __init__(self, name):
        self.name = name
    
    @property # Converts the function into a attribute
    def name(self):
        return self.__name
    
    @name.setter # Converts the function into a setter of the attribute with the same name
    def name(self, name):
        if name.strip():
            self.__name = name
        else:
            self.__name = "Unknown"
    

dog = Dog("Dobby")

print(dog.name)