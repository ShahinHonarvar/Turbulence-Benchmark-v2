def find_second_largest_num(numbers):
    subset = numbers[527:539]
    if len(subset) < 2:
        return None
    largest = max(subset[0], subset[1])
    second_largest = min(subset[0], subset[1])
    for num in subset[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest