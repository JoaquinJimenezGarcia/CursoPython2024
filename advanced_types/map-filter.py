users = [[4, "Joaquin"], [1, "Admin"], [5, "Wolfgang"]]

names = list(map(lambda user: user[1], users))
print(names)

filteredUsers = list(filter(lambda user: user[0] > 2, users))
print(filteredUsers)