n1 = input("Write first number\n")
n2 = input("Write second number\n")

n1 = int(n1)
n2 = int(n2)

sum = n1 + n2
rest = n1 - n2
mult = n1 * n2
div = n1 / n2

results = f"""
    Sum = {sum},
    Rest = {rest},
    Mult = {mult},
    Div = {div} 
"""

print(results)