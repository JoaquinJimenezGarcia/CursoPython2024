num = 1

while num < 100:
    print(num)
    num *= 2
    
command = ""

while command.lower() != "exit":
    command = input("> ")
    print(command)