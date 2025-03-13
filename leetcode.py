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


# Linked list Implementation
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
# my_linked_list.print_list()

# Index at tail
my_linked_list.delete_at_index(5)
my_linked_list.print_list()
my_linked_list.insert_at_tail(3)
my_linked_list.print_list()

print(my_linked_list.get_values())
