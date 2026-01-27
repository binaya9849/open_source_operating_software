"""   
2. Rolling queue (keep only last 5 numbers)

TODO: Ask the user for numbers until they enter an empty string. Store them in a queue, but keep only the last 5 numbers entered.

Example:
User enters: 1, 2, 3, 4, 5, 6, 7
Queue at the end should contain: [3, 4, 5, 6, 7]

Tips:

Use input() in a loop.

When the queue grows beyond length 5, remove from the front.

Convert input to int after checking it’s not empty.

"""
from collections import deque

queue = deque()

while True:
    user_input = input("Enter a number (or empty to stop): ")
    if user_input == "":
        break
    number = int(user_input)
    queue.append(number)
    if len(queue) > 5:
        queue.popleft()

print("Queue contains:", list(queue))
