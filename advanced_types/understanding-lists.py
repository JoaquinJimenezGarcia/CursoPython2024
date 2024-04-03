users = [[4, "Joaquin"], [1, "Admin"], [5, "Wolfgang"]]

names = []

for user in users:
    names.append(user[1])
print(names)

names_compact = [user[1] for user in users]
print(names_compact)

filtered_users = [user for user in users if user[0] > 2]
print(filtered_users)

filtered_user_names = [user[1] for user in users if user[0] > 3]
print(filtered_user_names)