nums = [2, 4, 1, 45, 75, 22]

nums.sort(reverse=True) # Sort the actual list
nums2 = sorted(nums) # Doesnt sort the list, returns a copy of the original one sorted

print(nums)
print(nums2)

users = [[4, "Joaquin"], [1, "Admin"], [5, "Wolfgang"]]

users.sort(key=lambda element:element[1], reverse=True)

print(users)