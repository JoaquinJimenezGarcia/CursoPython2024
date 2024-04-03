my_list = [1, 2, 3, 4]
print(my_list)

print(*my_list)

second_list = [5, 6]

combined_lists = [*my_list, *second_list]
print(combined_lists)

p1 = {"x": 15}
p2 = {"y": 25}

points = {**p1, **p2}
print(points)