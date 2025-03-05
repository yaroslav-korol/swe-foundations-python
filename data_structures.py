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
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head: ListNode = None
        self.tail: ListNode = self.head

    def get(self, index: int) -> int:
        current_node = self.head
        initial_index = 0

        while current_node:
            if initial_index == index:
                return current_node.value

            current_node = current_node.next
            initial_index += 1

        return -1

    def insertHead(self, val: int) -> None:
        new_head: ListNode = ListNode(val)
        if not self.head:
            self.head = self.tail = new_head
        else:
            new_head.next = self.head
            self.head = new_head

    def insertTail(self, val: int) -> None:
        new_tail: ListNode = ListNode(val)
        if not self.tail:
            self.tail = new_tail
        else:
            self.tail.next = new_tail
            self.tail = new_tail

    def remove(self, index: int) -> bool:
        current_node = self.head
        initial_index = 0

        while current_node:
            previous = current_node
            initial_index += 1

            if initial_index == index:
                previous.next = current_node.next.next
                return True

        return False

    def getValues(self) -> list[int]:
        current_node = self.head
        list_values = []
        while current_node:
            list_values.append(current_node.value)
            current_node = current_node.next

        return list_values


linked_list_1: LinkedList = LinkedList()
linked_list_1: LinkedList = LinkedList()

# Debug test case
print(linked_list_1.get(0))

linked_list_1.insertHead(1)
linked_list_1.insertTail(2)
linked_list_1.insertHead(0)
linked_list_1.remove(1)
print(linked_list_1.getValues())

print(linked_list_1.get(1))
print(linked_list_1.get(3))


check_value = None
