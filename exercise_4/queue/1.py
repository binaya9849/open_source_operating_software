"""
1. Reverse the first 3 elements of a queue

TODO: Reverse only the first 3 items in the queue. Keep the rest in the same order.

Example:
Input queue: [1, 2, 3, 4, 5]
Output queue: [3, 2, 1, 4, 5]

Tips:

Queues remove from the front (index 0).

A stack is useful for reversing order.

Steps idea: take 3 items off the queue -> then push to a stack -> pop from stack back to the front.
"""



from collections import deque

def reverse_first_three(queue):
    n = min(3, len(queue))
    stack = []
    for _ in range(n):
        stack.append(queue.popleft())
    while stack:
        queue.appendleft(stack.pop())
    for _ in range(len(queue) - n):
        queue.append(queue.popleft())
    return queue

q = deque([1, 2, 3, 4, 5])
reverse_first_three(q)
print(list(q))  
