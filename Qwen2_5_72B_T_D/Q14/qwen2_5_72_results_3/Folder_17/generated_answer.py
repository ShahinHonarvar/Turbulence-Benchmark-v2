def find_second_smallest_num(numbers):
    if len(numbers) < 39:
        return None
    sliced_numbers = numbers[28:39]
    if len(sliced_numbers) < 2:
        return None
    sliced_numbers.sort()
    return sliced_numbers[1] if len(sliced_numbers) > 1 else None