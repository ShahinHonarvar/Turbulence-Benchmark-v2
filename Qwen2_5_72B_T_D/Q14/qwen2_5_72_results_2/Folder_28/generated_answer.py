def find_second_smallest_num(numbers):
    if len(numbers) < 51:
        return None
    sliced_numbers = numbers[22:51]
    if len(sliced_numbers) < 2:
        return None
    min_num = min(sliced_numbers)
    second_smallest = None
    for num in sliced_numbers:
        if num > min_num:
            if second_smallest is None or num < second_smallest:
                second_smallest = num
    return second_smallest