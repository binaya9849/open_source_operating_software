"""
3. Simplify a file path using a stack

TODO: Simplify a Unix-like path:

"." means "stay here" -> ignore it

".." means "go back one folder" -> pop from stack if possible

Folder names push onto the stack
Ignore extra slashes

Example:
Input: "/home//user/.././docs"
Output: "/home/docs"

Tips:

Split the path by "/" to get parts.

Skip empty parts and ".".

On "..", pop if the stack isn’t empty.

At the end, join the stack back into a path starting with "/".
"""
def simplify_path(path):
    stack = []
    parts = path.split("/")

    for part in parts:
        if part == "" or part == ".":
            continue
        elif part == "..":
            if stack:
                stack.pop()
        else:
            stack.append(part)

    simplified = "/" + "/".join(stack)
    return simplified


path = "/home//user/.././docs"
print(simplify_path(path))
