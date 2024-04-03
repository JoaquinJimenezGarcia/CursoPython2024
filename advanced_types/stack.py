stack = []
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)

last_item = stack.pop()
print(last_item)
print(stack)
print(stack[-1])

stack.pop()
stack.pop()

if not stack:
    print("Stack is empty")