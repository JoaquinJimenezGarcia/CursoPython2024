nums = [1, 2, 3]

one, two, three = nums

nums = [1, 2, 3, 4, 5]
first, *others = nums
first, second, *others, last = nums
print(one, two, three)
print(first, second, others, last)
