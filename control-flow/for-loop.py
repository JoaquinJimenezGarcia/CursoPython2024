desired_num = 3

for num in range(5):
    print("Current num", num)
    if num == desired_num:
        print("Found!", desired_num)
        break # Stops the loop
else: # Else in a loop can be used when 'break' is not called and loop has finished
    print("Number not found", desired_num)