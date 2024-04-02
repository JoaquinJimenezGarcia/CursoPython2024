pets = ["Wolfgang", "Pelusa", "Copioto", "Rex"]

for pet in pets:
    print(pet)
    
for pet in enumerate(pets):
    print(f"Index: {pet[0]} - Name: {pet[1]}")

for i, petName in enumerate(pets):
    print(i, petName)