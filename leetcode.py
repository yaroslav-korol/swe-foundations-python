# # 1.
# # Input:
numbers_1 = [3, 2, 2, 3]
value_1 = 3

# # Output: 2, nums = [2,2,_,_]


numbers_2 = [0, 1, 2, 2, 3, 0, 4, 2]
value_2 = 2

numbers_3 = [2]
value_3 = 3


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left: int = 0

        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1

        return left


#         left_index: int = 0
#         right_index: int = len(nums) - 1
#         swap_counter: int = 0

#         while left_index < right_index:
#             left: int = nums[left_index]
#             right: int = nums[right_index]

#             if left != val:
#                 left_index += 1

#             if right == val:
#                 right_index -= 1
#                 swap_counter += 1
#                 continue

#             nums[left_index], nums[right_index] = nums[right_index], nums[left_index]
#             left_index += 1
#             right_index -= 1
#             swap_counter += 1

#         print(f"Swap counter: {swap_counter}")
#         print(f"New nums len: {len(nums)}")
#         print(f"Right index: {right_index}")
#         print(f"Left index: {left_index}")

#         return nums[: len(nums) - swap_counter]


# solution_1: Solution = Solution()
# solution_2: Solution = Solution()
# solution_3: Solution = Solution()

# result_1: list[int] = solution_1.removeElement(nums=numbers_1, val=value_1)
# result_2: list[int] = solution_2.removeElement(nums=numbers_2, val=value_2)
# result_3: list[int] = solution_2.removeElement(nums=numbers_3, val=value_3)
# print(result_1)
# print(result_2)
# print(result_3)


# Leetcode 26:

# Input:
nums_1 = [1, 1, 2]
# Output: 2, nums = [1,2,_]

nums_2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]


# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         left_index: int = 0
#         right_index: int = 1
#         arr_len: int = len(nums)

#         while right_index < arr_len:
#             if nums[right_index] <= nums[left_index]:
#                 right_index += 1
#             else:
#                 left_index += 1
#                 nums[left_index], nums[right_index] = nums[right_index], nums[left_index]

#         return left_index + 1


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left: int = 0

        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1

            if nums[right] > nums[right - 1]:
                nums[left], nums[right] = nums[right], nums[left]

        return left + 1


# solution_1: Solution = Solution()
# solution_2: Solution = Solution()

# print(nums_1)
# print(nums_2)
# print()

# result_1: list[int] = solution_1.removeDuplicates(nums=nums_1)
# result_2: list[int] = solution_2.removeDuplicates(nums=nums_2)


# print(result_1)
# print(nums_1, end="\n\n")

# print(result_2)
# print(nums_2, end="\n\n")


# Valid Parentheses

# Example 1:
parentheses_str_1: str = "()"
Output_1: bool = True

# Example 2:
parentheses_str_2: str = "()[]{}"
Output_2: bool = True

# Example 3:
parentheses_str_3: str = "(]"
Output_3: bool = False

# Example 4:
parentheses_str_4: str = "([])"
Output_4: bool = True


class SolutionParentheses:
    def isValid(self, s: str) -> bool:
        stack: list = []

        for char in s:
            if char in ("(", "[", "{"):
                stack.append(ord(char))
            else:
                close_char_addition: int = 1 if char == ")" else 2
                if stack[-1] != ord(char) - close_char_addition:
                    return False
                stack.pop()

        return len(stack) == 0


# solution_par_1: SolutionParentheses = SolutionParentheses()
# solution_par_2: SolutionParentheses = SolutionParentheses()
# solution_par_3: SolutionParentheses = SolutionParentheses()
# solution_par_4: SolutionParentheses = SolutionParentheses()

# print(parentheses_str_1)
# print(parentheses_str_2)
# print(parentheses_str_3)
# print(parentheses_str_4)
# print()

# result_par_1: list[int] = solution_par_1.isValid(s=parentheses_str_1)
# result_par_2: list[int] = solution_par_2.isValid(s=parentheses_str_2)
# result_par_3: list[int] = solution_par_3.isValid(s=parentheses_str_3)
# result_par_4: list[int] = solution_par_4.isValid(s=parentheses_str_4)


# print(result_par_1)
# print(parentheses_str_1, end="\n\n")

# print(result_par_2)
# print(parentheses_str_2, end="\n\n")

# print(result_par_3)
# print(parentheses_str_3, end="\n\n")

# print(result_par_4)
# print(parentheses_str_4, end="\n\n")
