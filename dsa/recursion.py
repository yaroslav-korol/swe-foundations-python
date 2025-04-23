'''
            DIVIDE AND CONQUER ALGORITHMS

I. 
Divide problem into several smaller subproblems
Normally, the subproblems are similar to the original

II. 
Conquer the subproblems by solving them recursively
Base case: solve small enough problems by brute force

III.
Combine the solutions to get a solution to the subproblems
And finally a solution to the original problem

IV.
Divide and Conquer algorithms are normally recursive
'''

    ### REVERSE STRING ###

# string = input('Get string: ')

# def reverse_string(str):
#     if str == "":
#         return ""
#     return reverse_string(str[1:]) + str[0]

# reversed_string = reverse_string(string)
# print(reversed_string)



    ### PALINDROME ###

# string = input('Get string: ')

# def is_palindrome(str):
#     length = len(str)
#     # Define the base-case / stopping condition
#     if length in (0, 1):
#         return True   
#     # Do some work to shrink the problem space
#     if str[0] == str[length - 1]:
#         return is_palindrome(str[1:length - 1])
#     # Additional base-case to handle non-palindromes
#     return False

# palindrome = is_palindrome(string)
# print(palindrome)



    ### DECIMAL TO BINARY ###

# decimal = int(input("Decimal number: "))

# def decimal_to_binary(dec, bin):
#     if dec == 0:
#         return bin
#     bin = str(dec % 2) + bin
#     return (decimal_to_binary (dec // 2, bin))
    
# find_binary = decimal_to_binary(decimal, '')
# print(find_binary)




    ### SUM OF NATURAL NUMBERS ###

# number = int(input("Decimal number: "))

# def sum_of_numbers(num):
#     if num == 1:
#         return num
#     return num + sum_of_numbers(num - 1)

# summ = sum_of_numbers(number)
# print(summ)





    ### BINARY SEARCH ###

# sorted_list = [-1, 0, 1, 2, 3, 4, 7, 9, 10, 12, 20]

# def binary_search(arr, left, right, x):
#     if left > right:
#         return -1
#     mid = (left + right) // 2
#     if x == arr[mid]:
#         return mid
#     if x < arr[mid]:
#         return binary_search(arr, left, mid - 1, x)
#     return binary_search(arr, mid + 1, right, x)

# start, end = 0, len(sorted_list)
# number_to_search = int(input("Decimal number: "))
# found = binary_search(sorted_list, start, end, number_to_search)
# print(found)



    ### FIBONACCI (Non-Optimized) ###

# fibonacci_number = int(input("Decimal number: "))

# def fibonacci(num):
#     if num in (0, 1):
#         return num
#     return fibonacci(num - 1) + fibonacci(num - 2)

# answer = fibonacci(fibonacci_number)
# print(answer)




    ### TAIL-CALL OPTIMIZATION ###

# NOT OPTIMIZED
# factorial_number = int(input("Decimal number: "))

# def factorial(numb):
#     if numb > 0:
#         return numb * factorial(numb - 1)
#     return 1

# result = factorial(factorial_number)
# print(result)


# OPTIMIZED
factorial_number = int(input("Decimal number: "))

def factorial(numb):
    return tail_factorial(numb, 1)

def tail_factorial(numb, multiplier):
    if numb > 0:
        return tail_factorial(numb - 1, numb * multiplier)
    return multiplier

result = factorial(factorial_number)
print(result)