# # # 1.
# # # Input:
# numbers_1 = [3, 2, 2, 3]
# value_1 = 3

# # # Output: 2, nums = [2,2,_,_]


# numbers_2 = [0, 1, 2, 2, 3, 0, 4, 2]
# value_2 = 2

# numbers_3 = [2]
# value_3 = 3


# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         left: int = 0

#         for right in range(len(nums)):
#             if nums[right] != val:
#                 nums[left] = nums[right]
#                 left += 1

#         return left


# #         left_index: int = 0
# #         right_index: int = len(nums) - 1
# #         swap_counter: int = 0

# #         while left_index < right_index:
# #             left: int = nums[left_index]
# #             right: int = nums[right_index]

# #             if left != val:
# #                 left_index += 1

# #             if right == val:
# #                 right_index -= 1
# #                 swap_counter += 1
# #                 continue

# #             nums[left_index], nums[right_index] = nums[right_index], nums[left_index]
# #             left_index += 1
# #             right_index -= 1
# #             swap_counter += 1

# #         print(f"Swap counter: {swap_counter}")
# #         print(f"New nums len: {len(nums)}")
# #         print(f"Right index: {right_index}")
# #         print(f"Left index: {left_index}")

# #         return nums[: len(nums) - swap_counter]


# # solution_1: Solution = Solution()
# # solution_2: Solution = Solution()
# # solution_3: Solution = Solution()

# # result_1: list[int] = solution_1.removeElement(nums=numbers_1, val=value_1)
# # result_2: list[int] = solution_2.removeElement(nums=numbers_2, val=value_2)
# # result_3: list[int] = solution_2.removeElement(nums=numbers_3, val=value_3)
# # print(result_1)
# # print(result_2)
# # print(result_3)


# # Leetcode 26:

# # Input:
# nums_1 = [1, 1, 2]
# # Output: 2, nums = [1,2,_]

# nums_2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# # Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]


# # class Solution:
# #     def removeDuplicates(self, nums: list[int]) -> int:
# #         left_index: int = 0
# #         right_index: int = 1
# #         arr_len: int = len(nums)

# #         while right_index < arr_len:
# #             if nums[right_index] <= nums[left_index]:
# #                 right_index += 1
# #             else:
# #                 left_index += 1
# #                 nums[left_index], nums[right_index] = nums[right_index], nums[left_index]

# #         return left_index + 1


# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         left: int = 0

#         for right in range(1, len(nums)):
#             if nums[left] != nums[right]:
#                 left += 1

#             if nums[right] > nums[right - 1]:
#                 nums[left], nums[right] = nums[right], nums[left]

#         return left + 1


# # solution_1: Solution = Solution()
# # solution_2: Solution = Solution()

# # print(nums_1)
# # print(nums_2)
# # print()

# # result_1: list[int] = solution_1.removeDuplicates(nums=nums_1)
# # result_2: list[int] = solution_2.removeDuplicates(nums=nums_2)


# # print(result_1)
# # print(nums_1, end="\n\n")

# # print(result_2)
# # print(nums_2, end="\n\n")


# # Valid Parentheses

# # Example 1:
# parentheses_str_1: str = "()"
# Output_1: bool = True

# # Example 2:
# parentheses_str_2: str = "()[]{}"
# Output_2: bool = True

# # Example 3:
# parentheses_str_3: str = "(]"
# Output_3: bool = False

# # Example 4:
# parentheses_str_4: str = "([])"
# Output_4: bool = True


# class SolutionParentheses:
#     def isValid(self, s: str) -> bool:
#         stack: list = []

#         for char in s:
#             if char in ("(", "[", "{"):
#                 stack.append(ord(char))
#             else:
#                 close_char_addition: int = 1 if char == ")" else 2
#                 if stack[-1] != ord(char) - close_char_addition:
#                     return False
#                 stack.pop()

#         return len(stack) == 0


# # solution_par_1: SolutionParentheses = SolutionParentheses()
# # solution_par_2: SolutionParentheses = SolutionParentheses()
# # solution_par_3: SolutionParentheses = SolutionParentheses()
# # solution_par_4: SolutionParentheses = SolutionParentheses()

# # print(parentheses_str_1)
# # print(parentheses_str_2)
# # print(parentheses_str_3)
# # print(parentheses_str_4)
# # print()

# # result_par_1: list[int] = solution_par_1.isValid(s=parentheses_str_1)
# # result_par_2: list[int] = solution_par_2.isValid(s=parentheses_str_2)
# # result_par_3: list[int] = solution_par_3.isValid(s=parentheses_str_3)
# # result_par_4: list[int] = solution_par_4.isValid(s=parentheses_str_4)


# # print(result_par_1)
# # print(parentheses_str_1, end="\n\n")

# # print(result_par_2)
# # print(parentheses_str_2, end="\n\n")

# # print(result_par_3)
# # print(parentheses_str_3, end="\n\n")

# # print(result_par_4)
# # print(parentheses_str_4, end="\n\n")


# Merge 2 linked lists
# Definition for singly-linked list.
class SinglyLinkedNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MergeSolution:
    def mergeTwoLists(
        self, list1: list[SinglyLinkedNode], list2: list[SinglyLinkedNode]
    ) -> list[SinglyLinkedNode]:
        merged_head: SinglyLinkedNode = SinglyLinkedNode()
        merged_tail = merged_head

        while list1 and list2:
            if list1.val < list2.val:
                merged_tail.next = list1
                list1 = list1.next

            else:
                merged_tail.next = list2
                list2 = list2.next

            merged_tail = merged_tail.next

        if not list1:
            merged_tail.next = list2

        if not list2:
            merged_tail.next = list1

        return merged_head.next


def create_linked_list(values):
    if not values:
        return None
    head = SinglyLinkedNode(values[0])
    current = head
    for val in values[1:]:
        current.next = SinglyLinkedNode(val)
        current = current.next
    return head


def print_linked_list(head: list[SinglyLinkedNode]):
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print(" -> ".join(values))

    # # Create linked lists
    # list1 = create_linked_list([1, 2, 4])
    # list2 = create_linked_list([1, 3, 5])

    # # Print linked lists
    # print("List 1:")
    # print_linked_list(list1)
    # print("List 2:")
    # print_linked_list(list2)

    # merge_list_instance = MergeSolution()
    # merged_list = merge_list_instance.mergeTwoLists(list1, list2)
    # print_linked_list(merged_list)


# Doubly Linked list Implementation
class DoublyLinkedNode:
    def __init__(self, value="", next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous


# Implement Browser history
class BrowserHistory:
    def __init__(self, homepage: str):
        """Initializes the object with the homepage of the browser."""
        self.head = DoublyLinkedNode(value=homepage)
        self.tail = self.head
        self.head.next = self.tail
        self.tail.previous = self.head
        self.current_position = self.head
        self.current_index = 0
        self.size = 1

    def visit(self, url: str) -> None:
        """
        Visits url from the current page. It clears up all the forward history.
        """
        new_node = DoublyLinkedNode(value=url, previous=self.current_position)
        self.current_position.next = new_node
        self.current_position = new_node
        self.tail = new_node
        self.current_index += 1
        self.size = self.current_index + 1

    def back(self, steps: int) -> str:
        """
        Move steps back in history. If you can only return x steps in the history and steps > x,
        you will return only x steps. Return the current url after moving back in history at most steps.
        """
        if steps >= self.current_index:
            self.current_index = 0
            self.current_position = self.head
            return self.current_position.value

        for _ in range(steps):
            self.current_index -= 1
            self.current_position = self.current_position.previous

        return self.current_position.value

    def forward(self, steps: int) -> str:
        """
        Move steps forward in history. If you can only forward x steps in the history and steps > x,
        you will forward only x steps. Return the current url after forwarding in history at most steps.
        """
        if steps >= self.size - self.current_index:
            self.current_index = self.size - 1
            self.current_position = self.tail
            return self.current_position.value

        for _ in range(steps):
            self.current_index += 1
            self.current_position = self.current_position.next

        return self.current_position.value

    def print_list(self):
        values = []
        head = self.head
        while head:
            values.append(str(head.value))
            head = head.next
        print(" -> ".join(values))


# TEST CASE 1
# browser_history: BrowserHistory = BrowserHistory("leetcode.com")
# print(browser_history.current_position.value)

# browser_history.visit("google.com")
# browser_history.visit("facebook.com")
# browser_history.visit("youtube.com")
# browser_history.print_list()
# print(f"Current position: {browser_history.current_position.value}", end="\n\n")

# # Back and forward
# print(browser_history.back(1))  #       Should return "facebook.com"
# print(browser_history.back(1))  #       Should return "google.com"
# print(browser_history.forward(1))  #    Should return "facebook.com"
# print(f"Current position: {browser_history.current_position.value}", end="\n\n")

# browser_history.visit("linkedin.com")
# print(f"Current position: {browser_history.current_position.value}", end="\n\n")
# browser_history.print_list()

# print(browser_history.forward(2))  #    Cannot forward - should return "linkedin.com"
# print(browser_history.back(2))  #       Should return "google.com"
# print(browser_history.back(7))  #       Should return "leetcode.com"


# TEST CASE 2
# browser_history_2: BrowserHistory = BrowserHistory("zav.com")
# browser_history_2.visit("kni.com")
# print(f"Current position: {browser_history_2.current_position.value}", end="\n\n")
# browser_history_2.print_list()

# print(browser_history_2.back(7))  #       Should return "zav.com"
# print(browser_history_2.back(7))  #       Should return "zav.com"
# print(f"Current position: {browser_history_2.current_position.value}", end="\n\n")

# print(browser_history_2.forward(5))  #    Cannot forward - should return "kni.com"
# print(f"Current position: {browser_history_2.current_position.value}", end="\n\n")
# print(browser_history_2.forward(1))  #    Cannot forward - should return "kni.com"

# browser_history_2.visit("pwrrbnw.com")
# browser_history_2.visit("mosohif.com")
# print(browser_history_2.back(9))  #       Should return "zav.com"


# 225.a Implement Stack using Singly Linked List
class MyLinkedListStack:
    def __init__(self):
        self.head = SinglyLinkedNode(-99)

    def push(self, x: int) -> None:
        """Pushes element x to the top of the stack."""
        new_node = SinglyLinkedNode(val=x, next=self.head.next)
        self.head.next = new_node

    def pop(self) -> int:
        """Removes the element on the top of the stack and returns it."""
        val = self.head.next.val
        self.head.next = self.head.next.next
        return val

    def top(self) -> int:
        """Returns the element on the top of the stack."""
        return self.head.next.val

    def empty(self) -> bool:
        """Returns true if the stack is empty, false otherwise."""
        return False if self.head.next else True
        # return self.head.next

    def print_list(self):
        values = []
        head = self.head.next
        while head:
            values.append(str(head.val))
            head = head.next
        print(" -> ".join(values))


# TEST CASE 1:
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

# my_stack: MyLinkedListStack = MyLinkedListStack()

# # EDGE CASE
# print(my_stack.empty())

# my_stack.push(1)
# my_stack.push(2)
# my_stack.print_list()

# print(my_stack.top())  #       return 2
# print(my_stack.pop())  #       return 2
# print(my_stack.empty())  #     return False


# 225.b Implement Stack using Queue
from collections import deque


class MyQueueStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        """Pushes element x to the top of the stack."""
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        """Removes the element on the top of the stack and returns it."""
        return self.queue.popleft() if not self.empty() else -1

    def top(self) -> int:
        """Returns the element on the top of the stack."""
        return self.queue[0] if not self.empty() else -1

    def empty(self) -> bool:
        """Returns true if the stack is empty, false otherwise."""
        return len(self.queue) == 0


# TEST CASE 1:
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

my_queue_stack: MyQueueStack = MyQueueStack()

# # EDGE CASE
print(my_queue_stack.empty())

my_queue_stack.push(1)
my_queue_stack.push(2)
print(my_queue_stack.queue)

print(my_queue_stack.top())  #       return 2
print(my_queue_stack.pop())  #       return 2
print(my_queue_stack.empty())  #     return False
