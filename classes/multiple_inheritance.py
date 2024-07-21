class Animal:
    def eat(self):
        print("eating...")

class Dog:
    def walk(self):
        print("walking...")
    
class Superdog(Dog,Animal):
    def code(self):
        print("I can code too!")

dog = Dog()
dog.walk()

mydog = Superdog()
mydog.walk()
mydog.eat()
mydog.code()