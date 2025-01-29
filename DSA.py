# BINARY SEARCH


def binary_search(iter_object: list, target: any):
    print("Enter binary search")
    low: int = 0
    high: int = len(iter_object) - 1

    print(f"Low: {low}, High: {high}")

    while low <= high:
        middle: int = int((high + low) / 2)
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
