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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = ListNode(-1)
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
        new_node = ListNode(val, self.head.next)
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insert_at_tail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def insert_at_index(self, index: int, val: int) -> None:
        i = 0
        current = self.head
        while current and i < index:
            i += 1
            current = current.next
        current.next = ListNode(val=val, next=current.next)

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


# Explanation
my_linked_list: MyLinkedList = MyLinkedList()
my_linked_list.insert_at_head(1)
my_linked_list.insert_at_tail(3)
print(my_linked_list.get(1))
my_linked_list.insert_at_head(2)
print(my_linked_list.get(1))
my_linked_list.insert_at_head(4)
my_linked_list.insert_at_head(6)
my_linked_list.insert_at_head(8)
my_linked_list.insert_at_index(1, 11)
my_linked_list.insert_at_index(3, 15)
my_linked_list.print_list()

my_linked_list.delete_at_index(1)
my_linked_list.delete_at_index(2)
my_linked_list.print_list()

# Edge cases

# Out of bounds
my_linked_list.delete_at_index(7)
my_linked_list.delete_at_index(6)

# Index at tail
my_linked_list.delete_at_index(5)
my_linked_list.print_list()
my_linked_list.insert_at_tail(3)
my_linked_list.print_list()

print(my_linked_list.get_values())
