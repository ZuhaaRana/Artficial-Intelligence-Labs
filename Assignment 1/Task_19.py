

# Task 19
# Implement Stack and Queue in Python
# Write separate functions for inserting and deleting and ask the user 
#to input the values.

class Stack:

    def __init__(self) -> None:
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, n):
        self.stack.append(n)

    def size(self):
        return len(self.stack)

    def disp(self):
        return self.stack


class Queue:

    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, n):
        self.queue.append(n)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def disp(self):
        return self.queue


Scheck = False
Qcheck = False
while True:
    print("Please choose from the following:-\n")
    print("1. Implement a Stack")
    print("2. Implement a Queue")

    choice = input('Enter your choice: ')
    if choice == '1':
        S = Stack()
        Scheck = True
        break

    elif choice == '2':
        Q = Queue()
        Qcheck = True
        break

    else:
        print("Enter from the options")

print('How many items you want to add?: ', end="")
items = int(input())

if Scheck:
    for i in range(items):
        val = int(input('Enter value: '))
        S.push(val)

    print("Stack is: ")
    print(S.disp())

else:
    for i in range(items):
        val = int(input('Enter value: '))
        Q.enqueue(val)

    print("Queue is: ")
    print(Q.disp())
