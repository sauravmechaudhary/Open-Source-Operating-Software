#4. Implement insert method for a Doubly linked list
def sort_characters():
    """
    Implement insert method for a Doubly linked list
You will have to implement the insert method, that inserts a new element/node in the list at the position given as a parameter.

The insert method will accept an index position where to insert a new node. The value of the node is the second parameter that have to be provided to the method. The method does not return anything, but it will raise a ValueError if the index is out of bounds.

The process is quite straight. Locate the nodes that will be before and after the new node, and update the necessary pointers. If the header pointer is affected, it should be updated. And the same happens with tail pointer.

For example:

Test	                                Result
mylist = DoublyLinkedList()             <DoublyLinkedList (6 elements): [5, 10, 20, 30, 40, 50]>

for i in range(10, 51, 10):
    mylist.append(i)
mylist.insert(0, 5)
print(mylist)

"""
class DoublyListNode:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f'<DoublyListNode: {self.data}>'


class DoublyLinkedList:
    def __init__(self):
        self._head = self._tail = None
        self._size = 0


    def __repr__(self):
        current = self._head
        values = ''

        while current:
            values += f', {current.data}'
            current = current.next

        plural = '' if self._size == 1 else 's'

        return f'<DoublyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'


    def __len__(self):
        return self._size


    def append(self, value):
        """
        Append value to the end of the list
        """

        new_node = DoublyListNode(value)

        # Empty list
        if self._head is None:
            self._head = self._tail = new_node

        # Non-empty list
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1


    def insert(self, index, value):
        """
        Insert value at given index
        """

        if index < 0 or index > self._size:
            raise ValueError("Index out of bounds")

        new_node = DoublyListNode(value)

        # Insert at beginning
        if index == 0:

            if self._head is None:
                self._head = self._tail = new_node
            else:
                new_node.next = self._head
                self._head.prev = new_node
                self._head = new_node

        # Insert at end
        elif index == self._size:

            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node

        # Insert in middle
        else:

            current = self._head

            for _ in range(index):
                current = current.next

            prev_node = current.prev

            prev_node.next = new_node
            new_node.prev = prev_node

            new_node.next = current
            current.prev = new_node

        self._size += 1


#1. Implementing a pop method for a Singly linked list
def sort_characters():
    """
Implementing a pop method for a Singly linked list
Given the base code we have seen until now and that is also provided, implement a pop method

The pop method will remove the last element from the list and return the data it contains. If the list is empty it should return None

This is a little bit trickier than the insert, as the method should take into account different cases: List is empty, list has only one node and then the rest of cases. The method should also locate the second to last node, to change its "next" pointer.

To actually remove a variable (like a node), remember you can use the del statement:

del(variable)

For example:

Test	Result
list = SinglyLinkedList()
for i in 'abc':
    list.append(i)
val = list.pop()
print(val, list)
c <SinglyLinkedList: [a, b]>

"""        

class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f'<ListNode: {self.data}>'


class SinglyLinkedList():
    def __init__(self):
        self._head = None

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        return f'<SinglyLinkedList: [{values.lstrip(", ")}]>'
     
    def append(self, value):
        """
        Append a value to the end of the list
        """
        node = ListNode(value)

        # If list is empty
        if not self._head:
            self._head = node
        else:
            current_node = self._head

            # Find last node
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = node


    def pop(self):
        """
        Remove and return the last element of the list.
        Return None if list is empty.
        """

        # Case 1: Empty list
        if self._head is None:
            return None

        # Case 2: Only one node
        if self._head.next is None:
            value = self._head.data
            del self._head
            self._head = None
            return value

        # Case 3: More than one node
        current = self._head

        # Find second-to-last node
        while current.next.next is not None:
            current = current.next

        value = current.next.data
        del current.next

        current.next = None

        return value

#2. Implementing a remove method for a Singly linked list
def sort_characters():
    """
    Now the singly linked list has two pointers: a head pointer and a tail pointer. Some things are easier and faster this way. In this exercise you will implement again a pop method to the SinglyLinkedList class.

The pop methods will remove the last element/node from the list and return its value. Same as before, if the list is empty, it should return None. The method will update the head and tail properties accordingly.

To actually remove a variable (like a node), remember you can use the del statement:

del(variable)

    """
class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f'<ListNode: {self.data}>'


class SinglyLinkedList():
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<SinglyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size


    def append(self, value):
        """
        Append a value to the end of the list
        """
        new_node = ListNode(value)

        if not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1


    def pop(self):
        """
        Remove and return the last element of the list.
        Return None if list is empty.
        """

        # Case 1: Empty list
        if self._head is None:
            return None

        # Case 2: Only one node
        if self._head == self._tail:
            value = self._head.data
            del self._head

            self._head = None
            self._tail = None
            self._size -= 1

            return value

        # Case 3: More than one node
        current = self._head

        # Find second-to-last node
        while current.next != self._tail:
            current = current.next

        value = self._tail.data
        del self._tail

        self._tail = current
        self._tail.next = None
        self._size -= 1

        return value

#3. Implementing a remove method for a Singly linked list wiht tail pointer
def sort_characters():
    """
    You will have to implement a more general remove method that can remove list's nodes from any position. 
    To help in this task an insert method is also provided that works as an example on how this method has to be implemented.

    The remove method will accept an index position of a node to be removed and it will return the value of the node being removed. 
    If the index is out of bounds, ValueError has to be raised. 
    The method should update head and tail if necessary, and the size of the list.

"""

class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f'<ListNode: {self.data}>'


class SinglyLinkedList():
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<SinglyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size


    def append(self, value):
        """
        Append a value to the end of the list
        """
        new_node = ListNode(value)

        if self._head is None:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        
        self._size += 1


    def pop(self):
        """
        Removes the last node of the list
        """

        if not self._size:
            return None
        
        # Locate previous node
        if self._size == 1:
            previous_node = None
        else:
            previous_node = self._head
            for _ in range(self._size - 2):
                previous_node = previous_node.next

        # Update head if needed
        if self._head == self._tail:
            self._head = None

        # Save value
        value = self._tail.data
        del self._tail

        # Update tail
        self._tail = previous_node

        if self._tail:
            self._tail.next = None

        self._size -= 1
        return value


    def insert(self, index, value):
        """
        Insert a new node with value in the position given by the index
        """

        if index < 0 or index > self._size:
            raise(ValueError('Index out of bounds'))

        previous_node = None
        next_node = self._head

        for _ in range(index):
            previous_node = next_node
            next_node = next_node.next

        new_node = ListNode(value, next_node)

        if previous_node is None:
            self._head = new_node
        else:
            previous_node.next = new_node
        
        if previous_node == self._tail:
            self._tail = new_node

        self._size += 1


    def remove(self, index):
        """
        Remove a node from the position given by the index
        """

        if index < 0 or index >= self._size:
            raise(ValueError('Index out of bounds'))

        previous_node = None
        current_node = self._head

        for _ in range(index):
            previous_node = current_node
            current_node = current_node.next

        value = current_node.data

        # Remove head
        if previous_node is None:
            self._head = current_node.next
        else:
            previous_node.next = current_node.next

        # Remove tail
        if current_node == self._tail:
            self._tail = previous_node

        del current_node

        self._size -= 1

        return value

#5. Implement remove method for a Doubly linked list
def sort_characters():
    """
    You will have to implement the remove method, that removes a element/node from the list at the position given as a parameter.

The remove method will accept an index position from where to remove node from the list. The method has to return the value of the node being removed or None if the list is empty. The method will raise a ValueError if the index is out of bounds.

The process is quite straight. Locate the nodes that before and after the node to be removed, and update the necessary pointers. If the header pointer is affected, it should be updated. And the same happens with tail pointer.


For example:

        Test	                                         Result
mylist = DoublyLinkedList()           <DoublyLinkedList (5 elements): [10, 20, 30, 40, 50]> 
for i in range(10, 51, 10):
    mylist.append(i)
val = mylist.remove(2)
print(val, mylist)

 """
class DoublyListNode:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f'<DoublyListNode: {self.data}>'


class DoublyLinkedList:
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        current = self._head
        values = ''
        while current:
            values += f', {current.data}'
            current = current.next
        plural = '' if self._size == 1 else 's'
        return f'<DoublyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def append(self, value):
        """Append value to the end of the list"""
        new_node = DoublyListNode(value)

        if self._head is None:
            self._head = self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1

    def insert(self, index, value):
        """Insert value at given index"""
        if index < 0 or index > self._size:
            raise ValueError("Index out of bounds")

        new_node = DoublyListNode(value)

        # Insert at beginning
        if index == 0:
            if self._head is None:
                self._head = self._tail = new_node
            else:
                new_node.next = self._head
                self._head.prev = new_node
                self._head = new_node

        # Insert at end
        elif index == self._size:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node

        # Insert in middle
        else:
            current = self._head
            for _ in range(index):
                current = current.next
            prev_node = current.prev

            prev_node.next = new_node
            new_node.prev = prev_node

            new_node.next = current
            current.prev = new_node

        self._size += 1

    def remove(self, index):
        """Remove a node from the position given by index"""
        # Raise ValueError if index is out of bounds (also covers empty list)
        if index < 0 or index >= self._size:
            raise ValueError("Index out of bounds")

        # Locate the node to remove
        current = self._head
        for _ in range(index):
            current = current.next

        # Save value
        value = current.data

        # Update previous node
        if current.prev:
            current.prev.next = current.next
        else:
            # Removing head
            self._head = current.next

        # Update next node
        if current.next:
            current.next.prev = current.prev
        else:
            # Removing tail
            self._tail = current.prev

        # Delete node and update size
        del current
        self._size -= 1

        return value


