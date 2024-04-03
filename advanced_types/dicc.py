point = { "x": 25, "y": 50 } # The key of a dict must be always a string
print(point)
print(point["x"])

point["z"] = 45

print(point)

if "w" in point:
    print(point["w"])
else:
    print("Point W does not exist")
    
print(point.get("x"))
print(point.get("w"))
print(point.get("w", 97))

del point["x"]

print(point)

point["x"] = 25

for value in point:
    print(value, point[value])
    
for value in point.items():
    print(value) # returns a tuple key-value
    
for key, value in point.items():
    print(key, value)
    
users = [
    {"id": 1, "name": "Joaquin"},
    {"id": 2, "name": "Felipe"},
    {"id": 3, "name": "Charles"}
]

for user in users:
    print(user["name"])