"""

3. Round-robin time processing

TODO: You have a queue of tasks. Each task is a tuple (name, time_needed).

Each round:
Take the front task.
Give it 2 time units of work.
If it still needs time, put it back to the end with updated remaining time.
If it finishes, remove it and record its name.

Return/print: the order in which tasks finish.

Example:
Tasks: [("A", 3), ("B", 6), ("C", 1)]
Completion order (one possible expected result): ["A", "C", "B"]

Tips:

Use a while queue: loop.

Subtract 2 each time you process a task.

If remaining time is > 0, re-enqueue it.

Otherwise, append its name to a finished list.

"""
from collections import deque

def round_robin(tasks):
    queue = deque(tasks)
    finished = []

    while queue:
        name, time_needed = queue.popleft()
        time_needed -= 2  # process 2 time units
        if time_needed > 0:
            queue.append((name, time_needed))  # re-enqueue with remaining time
        else:
            finished.append(name)  # task finished

    return finished

tasks = [("A", 3), ("B", 6), ("C", 1)]
result = round_robin(tasks)
print(result)
