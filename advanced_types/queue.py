from collections import deque

file = deque([1, 2])
file.append(3)
file.append(4)
file.append(5)

print(file)

file.popleft()
print(file)

if not file:
    print("Queue is empty")