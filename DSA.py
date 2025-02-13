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


# BINARY SEARCH


def binary_search(iter_object: list, target: any):
    print("Enter binary search")
    low: int = 0
    high: int = len(iter_object) - 1

    print(f"Low: {low}, High: {high}")

    while low <= high:
        middle: int = int((high + low) / 2)  # bug here
        current_guess: any = iter_object[middle]

        # debug
        print("Debug values")
        print(f"Middle: {middle}, Current guess: {current_guess}")

        if current_guess == target:
            return middle

        if current_guess < target:
            low = middle

        if current_guess > target:
            high = middle

    return None


def selection_sort(unsorted_list: list) -> list:
    list_len: int = len(unsorted_list) - 1

    for i in range(list_len):
        for j in range(i + 1, list_len + 1):
            current_value: int = unsorted_list[j]
            if current_value < unsorted_list[i]:
                unsorted_list[j] = unsorted_list[i]
                unsorted_list[i] = current_value

    return unsorted_list


def main():
    unordered_nums: list[int] = [7, 3, 1, 11, 23, 34, 345, 123, 456, 89, 1001, 134, 567, 5656]

    ordered_nums: list[int] = selection_sort(unordered_nums)
    print(ordered_nums)

    target_object = 2334
    # target_object = 11
    result = binary_search(ordered_nums, target_object)

    print(result)


if __name__ == "__main__":
    main()
