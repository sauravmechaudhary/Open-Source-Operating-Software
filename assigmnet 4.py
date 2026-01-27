# Queues Exercises
# 1. Reverse the first 3 elements of a queue

# TODO: Reverse only the first 3 items in the queue. Keep the rest in the same order.

# Example:
# Input queue: [1, 2, 3, 4, 5]
# Output queue: [3, 2, 1, 4, 5]

# Tips:

# Queues remove from the front (index 0).

# A stack is useful for reversing order.

# Steps idea: take 3 items off the queue -> then push to a stack -> pop from stack back to the front.

def reverse_first_3(queue):
    stack = []

    
    for _ in range(min(3, len(queue))):
        stack.append(queue.pop(0))

    
    while stack:
        queue.append(stack.pop())

        n = len(queue) - 3 
    for _ in range(max(0, n)):
        queue.append(queue.pop(0))

    return queue


# 2. Rolling queue (keep only last 5 numbers)

# TODO: Ask the user for numbers until they enter an empty string. Store them in a queue, but keep only the last 5 numbers entered.

# Example:
# User enters: 1, 2, 3, 4, 5, 6, 7
# Queue at the end should contain: [3, 4, 5, 6, 7]

# Tips:

# Use input() in a loop.

# When the queue grows beyond length 5, remove from the front.

# Convert input to int after checking it’s not empty.

queue = []

while True:
    s = input("Enter a number (or press Enter to stop): ")
    if s == '':
        break
    num = int(s)
    queue.append(num)  # enqueue at the back

    # Keep only last 5 elements
    if len(queue) > 5:
        queue.pop(0)  # remove from front

print("Final queue:", queue)


# 3. Round-robin time processing

# TODO: You have a queue of tasks. Each task is a tuple (name, time_needed).

# Each round:
# Take the front task.
# Give it 2 time units of work.
# If it still needs time, put it back to the end with updated remaining time.
# If it finishes, remove it and record its name.

# Return/print: the order in which tasks finish.

# Example:
# Tasks: [("A", 3), ("B", 6), ("C", 1)]
# Completion order (one possible expected result): ["A", "C", "B"]

# Tips:

# Use a while queue: loop.

# Subtract 2 each time you process a task.

# If remaining time is > 0, re-enqueue it.

# Otherwise, append its name to a finished list.

def round_robin(tasks):
    queue = tasks[:] 
    finished = []

    while queue:
        task_name, time_needed = queue.pop(0)  

        
        time_needed -= 2

        if time_needed > 0:
            
            queue.append((task_name, time_needed))
        else:
            
            finished.append(task_name)

    return finished


# Stack exercises
# 1. Find the minimum value in a stack

# TODO: Given a stack of numbers (a Python list), print the smallest number in it.

# Example:
# Stack: [5, 2, 9, 1, 7]
# Output: 1

# Tips:

# Python has a built-in function that finds the smallest number in a list.

# Make sure the stack is not empty before trying to find a minimum.

stack = [5, 2, 9, 1, 7]

if stack:  # check if the stack is not empty
    smallest = min(stack)
    print(smallest)
else:
    print("Stack is empty")

# 2. Undo last N actions

# TODO: You have a stack of actions (strings). Undo the last n actions safely:

# Pop up to n items from the stack.

# If n is larger than the stack size, just undo what exists.

# Example:
# Actions: ["open", "edit", "save", "close"], n = 2
# Undone: ["close", "save"]
# Left in stack: ["open", "edit"]

# Tips:

# Use a for loop that runs n times.

# Before popping, check if the stack is empty.

# Store undone actions in a separate list.

# Stack of actions
actions = ["open", "edit", "save", "close"]
n = 2

undone = []

# Pop up to n actions
for _ in range(n):
    if actions:
        undone.append(actions.pop())
    else:
        break

print("Undone:", undone)
print("Left in stack:", actions)


# 3. Simplify a file path using a stack

# TODO: Simplify a Unix-like path:

# "." means "stay here" -> ignore it

# ".." means "go back one folder" -> pop from stack if possible

# Folder names push onto the stack
# Ignore extra slashes

# Example:
# Input: "/home//user/.././docs"
# Output: "/home/docs"

# Tips:

# Split the path by "/" to get parts.

# Skip empty parts and ".".

# On "..", pop if the stack isn’t empty.

# At the end, join the stack back into a path starting with "/".

def simplify_path(path):
    parts = path.split('/')
    stack = []

    for part in parts:
        if part == '' or part == '.':
            
            continue
        elif part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)

    
    simplified = '/' + '/'.join(stack)
    return simplified
