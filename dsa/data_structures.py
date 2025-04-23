# DATA STRUCTURES IMPLEMENTATION


# DYNAMIC ARRAY (RESIZABLE ARRAY)
class DynamicArray:
    """ "Initialize an empty array
    with a capacity of capacity, where capacity > 0.
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [-99] * self.capacity

    def get(self, i: int) -> int:
        """Return the element at index i. Assume that index i is valid."""
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        """Set the element at index i to n."""
        self.array[i] = n

    def pushback(self, n: int) -> None:
        """Push the element n to the end of the array.
        If the array is full, resize the array first.
        """
        if self.size == self.capacity:
            self.resize()

        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        """Pop and return the element at the end of the array.
        Assume that the array is non-empty.
        """
        self.size -= 1 if self.size > 0 else 0
        popped_value = self.array[self.size]
        self.array[self.size] = -99
        return popped_value

    def resize(self) -> None:
        """Double the capacity of the array."""
        self.capacity *= 2
        new_array = [-99] * self.capacity

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array

    def getSize(self) -> int:
        """Return the number of elements in the array."""
        return self.size

    def getCapacity(self) -> int:
        """Return the capacity of the array."""
        return self.capacity


# TEST CASES

# Example 1:
print("Test 1")
arr_1: DynamicArray = DynamicArray(1)
print(arr_1.getSize() == 0)  # should return 0
print(arr_1.getCapacity() == 1)  # should return 1

# # Example 2:
print("\n\nTest 2")
arr_2: DynamicArray = DynamicArray(1)
arr_2.pushback(1)
print(arr_2.getCapacity() == 1)  # should return 1
arr_2.pushback(2)
# print(arr_2.getCapacity())  # should return 2
print(f"Capacity: {arr_2.getCapacity()} is correct - {arr_2.getCapacity() == 2}")


# # Example 3:
print("\n\nTest 3")
arr_3: DynamicArray = DynamicArray(1)
print(arr_3.getSize())  # should return 0
# print(arr_3.getCapacity())  # should return 1
print(f"Capacity: {arr_3.getCapacity()} is correct - {arr_3.getCapacity() == 1}\n")

arr_3.pushback(1)
print(arr_3.getSize())  # should return 1
# print(arr_3.getCapacity())  # should return 1
print(f"Capacity: {arr_3.getCapacity()} is correct - {arr_3.getCapacity() == 1}\n")

arr_3.pushback(2)
print(arr_3.getSize())  # should return 2
# print(arr_3.getCapacity())  # should return 2
print(f"Capacity: {arr_3.getCapacity()} is correct - {arr_3.getCapacity() == 2}\n")

# print(arr_3.get(1))  # should return 2
print(f"self.get(): {arr_3.get(1)} is correct - {arr_3.get(1) == 2}")
arr_3.set(1, 3)
# print(arr_3.get(1))  # should return 3
print(f"self.get(): {arr_3.get(1)} is correct - {arr_3.get(1) == 3}\n")

print(arr_3.popback())  # should return 3
print(arr_3.getSize())  # should return 1
# print(arr_3.getCapacity())  # should return 2
print(f"Capacity: {arr_3.getCapacity()} is correct - {arr_3.getCapacity() == 2}")


# MIN STACK
class MinStack:
    def __init__(self):
        self.stack: list[int] = []
        self.min_values_stack: list[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        min_value = val if not self.min_values_stack else min(val, self.min_values_stack[-1])
        self.min_values_stack.append(min_value)

    def pop(self) -> None:
        self.stack.pop()
        self.min_values_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_values_stack[-1]


# min_stack: MinStack = MinStack()
# min_stack.push(1)
# min_stack.push(2)
# min_stack.push(0)
# print(min_stack.getMin())  # return 0
# min_stack.pop()
# print(min_stack.top())  # return 2
# print(min_stack.getMin())  # return 1

# print(min_stack.stack)
# print(min_stack.min_values_stack)


# SINGLY LINKED LIST
class SinglyLinkedNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = SinglyLinkedNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        i = 0
        head = self.head.next
        while head:
            if i == index:
                return head.val
            i += 1
            head = head.next
        return -1

    def insert_at_head(self, val: int) -> None:
        new_node = SinglyLinkedNode(val, self.head.next)
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insert_at_tail(self, val: int) -> None:
        self.tail.next = SinglyLinkedNode(val)
        self.tail = self.tail.next

    def insert_at_index(self, index: int, val: int) -> None:
        i = 0
        current = self.head
        while current and i < index:
            i += 1
            current = current.next

        # Out of bounds check
        if not current:
            return

        new_node = SinglyLinkedNode(val=val, next=current.next)
        current.next = new_node

        # If inserted at the end, update tail
        if not new_node.next:
            self.tail = new_node

    def delete_at_index(self, index: int) -> None:
        i = 0
        previous = self.head
        while previous and i < index:
            i += 1
            previous = previous.next
        # Out of bounds
        if not previous or not previous.next:
            return
        # Deleting at tail index
        if previous.next == self.tail:
            self.tail = previous

        previous.next = previous.next.next

    def get_values(self) -> list[int]:
        values: list[int] = []
        current = self.head.next
        while current:
            values.append(current.val)
            current = current.next
        return values

    def print_list(self):
        values = []
        head = self.head.next
        while head:
            values.append(str(head.val))
            head = head.next
        print(" -> ".join(values))


# my_linked_list: SinglyLinkedList = SinglyLinkedList()
# my_linked_list.insert_at_head(7)
# my_linked_list.insert_at_head(2)
# my_linked_list.insert_at_head(1)
# my_linked_list.print_list()

# my_linked_list.insert_at_index(3, 0)
# my_linked_list.insert_at_index(15, 15)
# my_linked_list.print_list()
# my_linked_list.delete_at_index(2)
# my_linked_list.print_list()

# my_linked_list.insert_at_head(6)
# my_linked_list.print_list()
# my_linked_list.insert_at_tail(4)

# my_linked_list.print_list()
# print(my_linked_list.get(4))
# my_linked_list.print_list()


# my_linked_list.insert_at_head(4)
# my_linked_list.insert_at_index(5, 0)
# my_linked_list.print_list()

# my_linked_list.insert_at_head(6)
# my_linked_list.print_list()


# # Edge cases

# # Out of bounds
# my_linked_list.delete_at_index(7)
# my_linked_list.delete_at_index(6)

# # Index at tail
# my_linked_list.delete_at_index(5)
# my_linked_list.print_list()
# my_linked_list.insert_at_tail(3)
# my_linked_list.print_list()

# print(my_linked_list.get_values())


# DOUBLY LINKED LIST
class DoublyLinkedNode:
    def __init__(self, value=0, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous


class DoublyLinkedList:
    def __init__(self):
        self.head = DoublyLinkedNode(-99)
        self.tail = DoublyLinkedNode(99)
        self.head.next = self.tail
        self.tail.previous = self.head
        self.size = 0

    def get_previous(self, index):
        current = self.head.next
        for _ in range(index):
            current = current.next
        return current

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1

        current = self.get_previous(index)
        return current.value

    def insert_at_head(self, val: int) -> None:
        head = self.head.next

        new_node = DoublyLinkedNode(value=val, previous=head.previous, next=head)
        head.previous = new_node
        self.head.next = new_node

        self.size += 1

    def insert_at_tail(self, val: int) -> None:
        tail = self.tail

        new_node = DoublyLinkedNode(value=val, previous=tail.previous, next=tail)
        tail.previous.next = new_node
        tail.previous = new_node

        self.size += 1

    def insert_at_index(self, index: int, val: int) -> None:
        if index > self.size:
            return

        if index == self.size:
            return self.insert_at_tail(val)

        current = self.get_previous(index)
        new_node = DoublyLinkedNode(value=val, previous=current.previous, next=current)
        current.previous.next = new_node
        current.previous = new_node
        self.size += 1
        return

    def delete_at_tail(self):
        self.tail = self.tail.previous
        self.tail.next = None
        self.size -= 1
        return

    def delete_at_index(self, index: int) -> None:
        if index >= self.size:
            return

        if index == self.size - 1:
            return self.delete_at_tail()

        current = self.get_previous(index)
        current.previous.next = current.next
        current.next.previous = current.previous

        self.size -= 1

    def print_list(self):
        values = []
        head = self.head.next
        while head.next:
            values.append(str(head.value))
            head = head.next
        print(" -> ".join(values))


# # Explanation
# my_doubly_linked_list: DoublyLinkedList = DoublyLinkedList()
# print(my_doubly_linked_list.get(0))

# my_doubly_linked_list.insert_at_head(9)
# my_doubly_linked_list.print_list()

# my_doubly_linked_list.insert_at_tail(111)
# my_doubly_linked_list.print_list()


# my_doubly_linked_list.insert_at_head(8)
# my_doubly_linked_list.insert_at_tail(112)
# my_doubly_linked_list.print_list()

# print(my_doubly_linked_list.get(5))
# print(my_doubly_linked_list.get(3))


# my_doubly_linked_list.insert_at_index(2, 50)
# my_doubly_linked_list.print_list()

# my_doubly_linked_list.insert_at_index(3, 60)
# my_doubly_linked_list.print_list()


# my_doubly_linked_list.insert_at_index(my_doubly_linked_list.size, 155)
# my_doubly_linked_list.print_list()

# my_doubly_linked_list.insert_at_index(0, 7)
# my_doubly_linked_list.print_list()

# my_doubly_linked_list.delete_at_index(12)
# my_doubly_linked_list.delete_at_index(2)
# my_doubly_linked_list.print_list()


# # Deleting edge cases
# my_doubly_linked_list.delete_at_index(0)
# my_doubly_linked_list.print_list()
# my_doubly_linked_list.delete_at_index(my_doubly_linked_list.size - 1)
# my_doubly_linked_list.print_list()

# my_doubly_linked_list.insert_at_tail(212)
# my_doubly_linked_list.print_list()
