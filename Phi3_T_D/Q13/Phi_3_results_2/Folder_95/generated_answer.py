def find_second_largest_num(numbers):
    if len(numbers) < 6:
        return None
    index_range = numbers[82:87]
    second_largest = None
    for num in index_range:
        if num > second_largest:
            second_largest = num
    if second_largest is None:
        return None
    largest = max(numbers)
    for num in index_range:
        if num != largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest