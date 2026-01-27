"""
1. Find the minimum value in a stack

TODO: Given a stack of numbers (a Python list), print the smallest number in it.

Example:
Stack: [5, 2, 9, 1, 7]
Output: 1

Tips:

Python has a built-in function that finds the smallest number in a list.

Make sure the stack is not empty before trying to find a minimum.

"""

stack = [5, 2, 9, 1, 7]

if stack:
    print(min(stack))
else:
    print("Stack is empty")
