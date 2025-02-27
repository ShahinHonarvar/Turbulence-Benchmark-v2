def find_second_largest_num(numbers):
    if len(numbers) < 6:
        return None
    sliced_numbers = numbers[:6]
    if len(set(sliced_numbers)) < 2:
        return None
    largest = max(sliced_numbers)
    second_largest = None
    for num in sliced_numbers:
        if num != largest:
            if second_largest is None or num > second_largest:
                second_largest = num
    return second_largest