# Logic operators = and, or, not

fuel = True
turned_on = True
running = False

if fuel and turned_on:
    print("Able to run")
else:
    print("Something is missing")
    
if turned_on or running: print("Consuming fuel")

if not running: print("You are stopped")

if fuel and (turned_on or running): print("Lets go somewhere")