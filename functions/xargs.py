def sum(*nums): # The * at the beginning means the value is gonna be an iterable
    result = 0
    for num in nums:
        result += num
    
    print(result)
    
sum(2, 5)
sum(5, 7, 4, 1, 7)