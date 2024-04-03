# A set is a group which cannot have duplicated
my_set = {1, 1, 2, 2, 3, 4}
print(my_set)

my_set.add(5)
my_set.remove(1)

print(my_set)

second_set = [5, 6, 7, 8]
second_set = set(second_set)

print(my_set | second_set) # Unify two sets
print(my_set & second_set) # Get the commmon values between two sets
print(my_set - second_set) # Get the values of the first set that are not in the second one
print(my_set  ^ second_set) # Get the elements in first and second set that are not in both sets

if 5 in second_set:
    print("Value found")