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
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class MergeSolution:
#     def mergeTwoLists(self, list1: list[ListNode], list2: list[ListNode]) -> list[ListNode]:
#         current_l1 = list1
#         current_l2 = list2

#         merged_head = ListNode()
#         merged_tail = merged_head

#         while current_l1 or current_l2:
#             if not current_l1:
#                 merged_tail.next = current_l2
#                 break

#             elif not current_l2:
#                 merged_tail.next = current_l1
#                 break

#             else:
#                 if current_l1.val < current_l2.val:
#                     merged_tail.next = current_l1
#                     merged_tail = merged_tail.next
#                     current_l1 = current_l1.next

#                 else:
#                     merged_tail.next = current_l2
#                     merged_tail = merged_tail.next
#                     # merged_tail = current_l1
#                     current_l2 = current_l2.next

#         return merged_head.next


class MergeSolution:
    def mergeTwoLists(self, list1: list[ListNode], list2: list[ListNode]) -> list[ListNode]:
        merged_head: ListNode = ListNode()
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
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head: list[ListNode]):
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
