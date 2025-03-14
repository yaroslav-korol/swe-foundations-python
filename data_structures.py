# Design min stack
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


# 2. Singly Linked List


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


# 3. Doubly Linked list Implementation
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


# Explanation
my_doubly_linked_list: DoublyLinkedList = DoublyLinkedList()
print(my_doubly_linked_list.get(0))

my_doubly_linked_list.insert_at_head(9)
my_doubly_linked_list.print_list()

my_doubly_linked_list.insert_at_tail(111)
my_doubly_linked_list.print_list()


my_doubly_linked_list.insert_at_head(8)
my_doubly_linked_list.insert_at_tail(112)
my_doubly_linked_list.print_list()

print(my_doubly_linked_list.get(5))
print(my_doubly_linked_list.get(3))


my_doubly_linked_list.insert_at_index(2, 50)
my_doubly_linked_list.print_list()

my_doubly_linked_list.insert_at_index(3, 60)
my_doubly_linked_list.print_list()


my_doubly_linked_list.insert_at_index(my_doubly_linked_list.size, 155)
my_doubly_linked_list.print_list()

my_doubly_linked_list.insert_at_index(0, 7)
my_doubly_linked_list.print_list()

my_doubly_linked_list.delete_at_index(12)
my_doubly_linked_list.delete_at_index(2)
my_doubly_linked_list.print_list()


# Deleting edge cases
my_doubly_linked_list.delete_at_index(0)
my_doubly_linked_list.print_list()
my_doubly_linked_list.delete_at_index(my_doubly_linked_list.size - 1)
my_doubly_linked_list.print_list()

my_doubly_linked_list.insert_at_tail(212)
my_doubly_linked_list.print_list()
