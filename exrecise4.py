#1. Implement push and pop methods for a Stack structure
def sort_characters():
    """
    You will implement the push and pop methods for a stack. You will also implement a `__repr__()` method to show the stack if necessary.

The push method will accept a value as parameter and adds a new node at the top of the stack with the given value. The pointers and size should be updated accordingly. This method does not return anything.

The pop method will remove the top node from the stack and return its value. The pointers and size should be updated accordingly. This method does not accept any parameters. If the stack is empty, the method should return None.

The __repr__() method should return (not print) a string like this:

<Stack (3 elements): ['C', 'B', 'A']>
Notice that it informs of the number of elements and prints a list with the content of the nodes. You can take a look to the previous chapter's examples if you need some inspiration.
For example:

Test	                            Result
mystack = Stack()           <Stack (1 element): [A]>
mystack.push('A')
print(mystack)


    """

class StackNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<StackNode: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, value):
        """Add a value on top of the stack"""
        new_node = StackNode(value, self._top)
        self._top = new_node
        self._size += 1

    def pop(self):
        """Remove and return the top value of the stack"""
        if self._top is None:
            return None

        value = self._top.data
        temp = self._top
        self._top = self._top.next
        del temp
        self._size -= 1
        return value

    def __repr__(self):
        current = self._top
        values = []
        while current:
            values.append(str(current.data))  # Convert to string for display
            current = current.next
        plural = 'element' if self._size == 1 else 'elements'
        return f"<Stack ({self._size} {plural}): [{', '.join(values)}]>"


#2. Write function to check the brackets balance
def sort_characters():
    """
    You have to write a function named "check_balance" that checks whether a string with different kind of bracket symbols is balanced or not using stack. The stack class is already available with the name "Stack"

The function "check_balance" accepts a string and it will check if the different sets of brackets symbols in the text are balanced, i.e. every kind of open bracket symbol is closed with the same kind of bracket symbol ('()', '[]' or '{}'). If everything checks, the function should return the text "Ok - C", being C the number of pairs found. If not, it should return the text: "Match error at position X", being X the position of the character relative to the beginning of the text.

Notice that texts should be exactly like shown and with the same capitalization.

The idea is simple, when you encounter an opening bracket symbol (`(` or a `{` or a `[`) you will push it to the stack. When you encounter a closing bracket symbol (`)` or a `}` or a `]`), pop the one in the stack and check if they match. If they don't match, you can return the error. If you get to the end of text without errors, return the "Ok" text as told before.


Some cases you want to take into account are when you encounter a closing bracket symbol before any opening one, and when the text leaves an unmatched opening bracket symbol.

For example:

Input	            Result
a(b)c[d]e{f}g       Ok - 3


    """

# Stack implementation
class StackNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<StackNode: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, value):
        """Add a value on top of the stack"""
        new_node = StackNode(value, self._top)
        self._top = new_node
        self._size += 1

    def pop(self):
        """Remove and return the top value of the stack"""
        if self._top is None:
            return None

        value = self._top.data
        temp = self._top
        self._top = self._top.next
        del temp
        self._size -= 1
        return value

    def __repr__(self):
        current = self._top
        values = []
        while current:
            values.append(str(current.data))  # Convert to string for display
            current = current.next
        plural = 'element' if self._size == 1 else 'elements'
        return f"<Stack ({self._size} {plural}): [{', '.join(values)}]>"


# Function to check brackets balance
def check_balance(text):
    stack = Stack()
    pairs_count = 0

    # Mapping of closing to opening brackets
    matching = {')': '(', ']': '[', '}': '{'}

    for pos, char in enumerate(text):
        if char in "([{":
            stack.push((char, pos))  # store bracket and its position
        elif char in ")]}":
            if stack._top is None:
                # Closing bracket without matching opening
                return f"Match error at position {pos}"
            top_char, top_pos = stack.pop()
            if matching[char] != top_char:
                # Mismatched pair
                return f"Match error at position {pos}"
            pairs_count += 1

    # Check for any unmatched opening brackets
    if stack._top is not None:
        # Find position of first unmatched opening bracket
        current = stack._top
        while current.next is not None:
            current = current.next
        return f"Match error at position {current.data[1]}"

    return f"Ok - {pairs_count}"


#3. Implement a Stack based Queue
def sort_characters():
    """
    You have to implement a stack based queue called "StackBasedQueue". A Stack class is already available. The class is already defined and you have to complete the requested methods. Notice that a "__repr__()" function is already provided so the exercise can be tested. This function forces you to use certain names for the internal properties: self._size, self._InboundStack and self._OutboundStack. You can also use whatever you prefer and rename the variables in the provided method.

The class should use two stacks as explained in the theory. The enqueue method will push to the Inbound stack and the dequeue method will pop from the Outbound stack. But if the Outbound stack is empty, it will try first to transfer all available elements from Inbound stack to Outbound stack.
    """

class StackBasedQueue:
    def __init__(self):
        self._InboundStack = Stack()
        self._OutboundStack = Stack()
        self._size = 0

    def enqueue(self, value):
        """Add an element to the queue"""
        self._InboundStack.push(value)
        self._size += 1

    def dequeue(self):
        """Remove and return the first element from the queue"""
        if self._OutboundStack._top is None:
            # Transfer all elements from Inbound to Outbound if Outbound is empty
            while self._InboundStack._top is not None:
                self._OutboundStack.push(self._InboundStack.pop())

        if self._OutboundStack._top is None:
            return None

        self._size -= 1
        return self._OutboundStack.pop()

    def __repr__(self):
        # Correct display from front to back
        front_list = []
        # OutboundStack: top is front-most
        current = self._OutboundStack._top
        temp = []
        while current:
            temp.append(str(current.data))
            current = current.next
        front_list.extend(temp[::-1])  # reverse to show front first

        # InboundStack: top is back-most
        current = self._InboundStack._top
        temp = []
        while current:
            temp.append(str(current.data))
            current = current.next
        front_list.extend(temp)  # already in correct order

        plural = 'element' if self._size == 1 else 'elements'
        return f"<StackBasedQueue ({self._size} {plural}): [{', '.join(front_list)}]>"

#4. Implement a Node based Queue
def sort_characters():
    """
    You have to implement a Queue class called Queue that uses the ListNode class to store the data. ListNode class is already available.

Queue class should implement a __init__() method that initialize internal variables/properties. It also has to implement the enqueue and dequeue methods. These methods are very similar (if not the same) that some of the methods already available in the DoublyLinkedList class. So it can be of help to get these two methods. Finally a __repr__() method should be implemented. After enqueuing 'A', 'B' and 'C' (in this order), it should show a text like this:

<Queue (3 elements): [C, B, A]>
    """

# Node class
class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<ListNode: {self.data}>'


# Queue using ListNode
class Queue:
    def __init__(self):
        self._head = None  # newest element (enqueue here)
        self._tail = None  # oldest element (dequeue from here)
        self._size = 0

    def enqueue(self, value):
        """Add a new element to the left (head)"""
        new_node = ListNode(value)

        if self._head is None:
            # Empty queue
            self._head = self._tail = new_node
        else:
            # Insert at head
            new_node.next = self._head
            self._head = new_node

        self._size += 1

    def dequeue(self):
        """Remove and return the oldest element (tail)"""
        if self._tail is None:
            return None  # empty queue

        # If queue has only one element
        if self._head == self._tail:
            value = self._tail.data
            self._head = self._tail = None
            self._size -= 1
            return value

        # Find the node before the tail
        current = self._head
        while current.next != self._tail:
            current = current.next

        value = self._tail.data
        self._tail = current
        self._tail.next = None
        self._size -= 1
        return value

    def __repr__(self):
        current = self._head
        values = []
        while current:
            values.append(str(current.data))
            current = current.next
        plural = 'element' if self._size == 1 else 'elements'
        return f"<Queue ({self._size} {plural}): [{', '.join(values)}]>"


#5. Implement a function to make pairs of even-odd numbers
def sort_characters():
    """
    You have to implement a function called get_pairs that given a list of numbers, makes pairs with them. Each pair consists in one even number and one odd number. The function will return a list containing all pairs as tuples. You have to implement the function using queues. A Queue class, that offers enqueue and dequeue methods, is already available for you to use.

The function will accept as parameter a (Python) list of integer numbers. The function will return a (Python) list containing tuples. Each tuple is a pair of even-odd numbers (first the even, then the odd number). The pairs have to be formed in order: the first available even number with the first available odd number.

To implement this function create two queues and traverse the numbers list. For each number, check is it an even number or an odd number,  and check if there is a pair available in the appropriate queue. If there is, save the pair for the output. If not, enqueue it.

    """

def get_pairs(numbers):
    even_queue = Queue()
    odd_queue = Queue()
    result = []

    for num in numbers:
        if num % 2 == 0:  # even
            if odd_queue._size > 0:
                odd_num = odd_queue.dequeue()
                result.append((num, odd_num))
            else:
                even_queue.enqueue(num)
        else:  # odd
            if even_queue._size > 0:
                even_num = even_queue.dequeue()
                result.append((even_num, num))
            else:
                odd_queue.enqueue(num)

    return result

