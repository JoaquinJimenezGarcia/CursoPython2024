class Dog:
    # Magic methogs are those who start with "__"
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Class Dog: {self.name}"
    
    def __del__(self):
        print(f"Bye dog: {self.name}")

    def speak(self):
        print(f"{self.name}: says: Hello world!")

dog = Dog("Chachito", 7)
print(dog)

del dog