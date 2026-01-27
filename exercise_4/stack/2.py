"""

2. Undo last N actions

TODO: You have a stack of actions (strings). Undo the last n actions safely:

Pop up to n items from the stack.

If n is larger than the stack size, just undo what exists.

Example:
Actions: ["open", "edit", "save", "close"], n = 2
Undone: ["close", "save"]
Left in stack: ["open", "edit"]

Tips:

Use a for loop that runs n times.

Before popping, check if the stack is empty.

Store undone actions in a separate list.

"""
actions = ["open", "edit", "save", "close"]
n = 2

undone = []

for _ in range(n):
    if actions: 
        undone.append(actions.pop())

print("Undone:", undone)
print("Left in stack:", actions)
