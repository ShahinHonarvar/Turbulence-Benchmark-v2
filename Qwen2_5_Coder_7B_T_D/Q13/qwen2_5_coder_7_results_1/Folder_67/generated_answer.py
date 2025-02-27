def find_second_largest_num(numbers):
    if len(numbers) < 51:
        return None
    subset = numbers[22:51]
    if len(subset) < 2:
        return None
    largest = max(subset[0], subset[1])
    second_largest = min(subset[0], subset[1])
    for num in subset[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    return second_largest