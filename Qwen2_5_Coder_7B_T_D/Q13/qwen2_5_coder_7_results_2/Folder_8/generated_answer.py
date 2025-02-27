def find_second_largest_num(numbers):
    if len(numbers) < 24:
        return None
    subset = numbers[23:24]
    if len(subset) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in subset:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    return second_largest