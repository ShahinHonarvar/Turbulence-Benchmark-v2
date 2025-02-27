def find_second_largest_num(numbers):
    if len(numbers) < 101 or len(numbers) < 11:
        return None
    sliced_numbers = numbers[10:101]
    if len(sliced_numbers) < 2:
        return None
    max_num = max(sliced_numbers)
    sliced_numbers.remove(max_num)
    second_max = max(sliced_numbers) if sliced_numbers else None
    return second_max