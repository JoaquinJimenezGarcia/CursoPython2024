pets = ["Wolfgang", "Pelusa", "Wolfgang", "Copioto", "Wolfgang", "Rex", "Wolfgang"]

pets.insert(1, "Pulga") # Insert add an item to a given index
pets.append("Melvin") # Append add an item to the end of the list

print(pets)

pets.remove("Wolfgang")

print(pets)

print(pets.count("Wolfgang"))

for i in range(pets.count("Wolfgang") - 1):
    pets.remove("Wolfgang")

print(pets)

pets.pop()
print(pets)

pets.pop(0)
print(pets)

del pets[0]
print(pets)

pets.clear()
print(pets)