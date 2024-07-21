class Animal:
    def eat(self):
        print("eating...")

class Dog:
    def walk(self):
        print("walking...")
    
# Python starts inheriting by right side to left side. So if the methods are
# called the same, only the ones in the first position will stay
class Superdog(Dog,Animal):
    def code(self):
        print("I can code too!")

dog = Dog()
dog.walk()

mydog = Superdog()
mydog.walk()
mydog.eat()
mydog.code()