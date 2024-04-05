class Dog:
    def speak(self): # This is no longer a function, this a method because belongs to the class
        print("guau!")

my_dog = Dog()
print(type(my_dog))
my_dog.speak()