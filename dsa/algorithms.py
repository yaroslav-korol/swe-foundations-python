# LOGARITHMS

# log10 100 is like asking, “How many 10s do we multiply together to get 100?”
# The answer is 2: 10 × 10. So log10 100 = 2.
# Logs are the flip of exponentials.

# When we talk about running time in Big O notation, log always means log2.

# When you search for an element using simple search,
# in the worst case you might have to look at every single element.
# So for a list of 8 numbers, you’d have to check 8 numbers at most.

# For binary search, you have to check log n elements in the worst case.
# For a list of 8 elements, log 8 == 3, because 23 == 8.
# So for a list of 8 numbers, you would have to check 3 numbers at most.
# For a list of 1,024 elements, log 1,024 = 10, because 210 == 1,024.
# So for a list of 1,024 numbers, you’d have to check 10 numbers at most.


# ALGORITHM RUN TIME. BIG O NOTATION

# Algorithm speed isn’t measured in seconds, but in growth of the number of operations.
# • Instead, we talk about how quickly the run time of an algorithm increases as the size of the input increases.
# • Run time of algorithms is expressed in Big O notation.
# • Binary search is a lot faster than simple search.
# • O(log n) is faster than O(n), but it gets a lot faster once the list of items you’re searching through grows.


# CONSTANTS
UNORDERED_NUMS: list[int] = [7, 5656, 3, 1, 11, 23, 34, 345, 123, 456, 89, 1001, 134, 567, 11]
TARGET_PRESENT: int = 34
TARGET_ABSENT: int = 340


# SEARCHING ALGORITHMS


# LINEAR SEARCH


# Manual implementation
def linear_search_manual(sequence: list[int], target: int) -> bool:
    for i in range(len(sequence)):
        if sequence[i] == target:
            return True
    return False


# Pythonic implementation
def linear_search_pythonic(sequence: list[int], target: int) -> bool:
    return target in sequence


# BINARY SEARCH


# SORTING ALGORITHMS


# SELECTION SORT
def selection_sort(sequence: list[int]) -> int:
    sequence_len: int = len(sequence)
    for i in range(sequence_len):
        min_index: int = i

        for j in range(i + 1, sequence_len):
            if sequence[j] < sequence[min_index]:
                min_index = j
        sequence[min_index], sequence[i] = sequence[i], sequence[min_index]

    return 0


# BUBBLE SORT
def bubble_sort(sequence: list[int]) -> int:
    sequence_len: int = len(sequence)
    for i in range(sequence_len):
        swapped: bool = False
        for j in range(sequence_len - 1 - i):
            if sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
                swapped = True

        if not swapped:
            return 0

    return 1


# INSERTION SORT
def insertion_sort(iterable: list) -> list:
    for i in range(len(iterable)):
        j = i - 1
        while j >= 0 and iterable[j] > iterable[j + 1]:
            iterable[j], iterable[j + 1] = iterable[j + 1], iterable[j]
            j -= 1

    return iterable


# MERGE SORT
def merge_sort(sequence: list, start: int, end: int) -> int:
    # base case
    pass


# QUICK SORT


def main():
    # Linear search

    # linear_manual_present: bool = linear_search_manual(UNORDERED_NUMS, TARGET_PRESENT)
    # linear_manual_absent: bool = linear_search_manual(UNORDERED_NUMS, TARGET_ABSENT)
    # print(linear_manual_present)
    # print(linear_manual_absent)

    # linear_pythonic_present: bool = linear_search_manual(UNORDERED_NUMS, TARGET_PRESENT)
    # linear_pythonic_absent: bool = linear_search_manual(UNORDERED_NUMS, TARGET_ABSENT)
    # print(linear_pythonic_present)
    # print(linear_pythonic_absent)

    # Selection sort

    # list_for_selection_sort: list[int] = [i for i in UNORDERED_NUMS]
    # print(list_for_selection_sort)

    # selection_sort(list_for_selection_sort)
    # print(list_for_selection_sort)
    # print(UNORDERED_NUMS)

    # Bubble sort

    # list_for_bubble_sort: list[int] = [i for i in UNORDERED_NUMS]
    # print(list_for_bubble_sort)

    # bubble_sort(list_for_bubble_sort)
    # print(bubble_sort(list_for_bubble_sort))
    # print(list_for_bubble_sort)
    # print(UNORDERED_NUMS)

    # Merge sort

    list_for_merge_sort: list[int] = [i for i in UNORDERED_NUMS]
    print(list_for_merge_sort)

    # merge_sort(list_for_merge_sort)

    # print(list_for_merge_sort)

    # Insertion sort
    # list_for_insertion_sort: list[int] = [i for i in UNORDERED_NUMS]
    # print(f"Before insertion sort: {list_for_insertion_sort}")

    # sorting_history = insertion_sort(list_for_insertion_sort)
    # print(f"Insertion sort return result: {sorting_history}")
    # print(f"Original list after sorting: {list_for_insertion_sort}")

    pass


if __name__ == "__main__":
    main()
