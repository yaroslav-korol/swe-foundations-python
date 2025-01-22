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
        print(f"Debug values")
        print(f"Middle: {middle}, Current guess: {current_guess}")

        if current_guess == target:
            return middle
        
        if current_guess < target:
            low = middle
        
        if current_guess > target:
            high = middle

    return None
    


nums = [1, 3, 7, 11, 21, 22, 23, 34, 111, 123, 345, 456, 489, 666, 999, 1001, 1234, 2334, 67567, 569056]

target_object = 2334
result = binary_search(nums, target_object)

print(result)
