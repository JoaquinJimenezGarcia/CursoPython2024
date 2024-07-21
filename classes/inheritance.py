class Animal:
    def eat(self):
        print("eating...")

class Dog(Animal):
    def walk(self):
        print("walking...")
    
class Superdog(Dog):
    def code(self):
        print("I can code too!")

dog = Dog()
dog.eat()

mydog = Superdog()
mydog.walk()
mydog.eat()
mydog.code()